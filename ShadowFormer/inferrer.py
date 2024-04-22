import cv2
import os
import argparse
from tqdm import tqdm

import torch.nn as nn
import torch
from torch.utils.data import DataLoader
import torch.nn.functional as F

import scipy.io as sio
from utils.loader import get_validation_data
import utils
from model import UNet

parser = argparse.ArgumentParser(description='RGB denoising on shadowed images')
parser.add_argument('--input_dir', default='/teamspace/studios/this_studio/SAM-Adapter-PyTorch/ISTD_remastered/',
    type=str, help='Directory of shadowed images')
parser.add_argument('--result_dir', default='./results/',
    type=str, help='Directory for denoised results')
parser.add_argument('--weights', default='/teamspace/studios/this_studio/ShadowFormer/ISTD_model_latest.pth',
    type=str, help='Path to weights')
parser.add_argument('--gpus', default='0', type=str, help='CUDA_VISIBLE_DEVICES')
parser.add_argument('--tile', type=int, default=None, help='Tile size (e.g 720). None means testing on the original resolution image')
parser.add_argument('--tile_overlap', type=int, default=32, help='Overlapping of different tiles')
args = parser.parse_args()

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = args.gpus

utils.mkdir(args.result_dir)

test_dataset = get_validation_data(args.input_dir)
test_loader = DataLoader(dataset=test_dataset, batch_size=1, shuffle=False, num_workers=8, drop_last=False)

model_restoration = UNet()
model_restoration = torch.nn.DataParallel(model_restoration)

utils.load_checkpoint(model_restoration, args.weights)
print("===>Testing using weights: ", args.weights)

model_restoration.cuda()
model_restoration.eval()

img_multiple_of = 8 * args.win_size

with torch.no_grad():
    for ii, data_test in enumerate(tqdm(test_loader), 0):
        rgb_noisy = data_test[1].cuda()
        mask = data_test[2].cuda()
        filenames = data_test[3]

        # Inference
        rgb_restored = model_restoration(rgb_noisy, mask)

        # Unpad the output
        rgb_restored = torch.clamp(rgb_restored, 0, 1).cpu().numpy().squeeze().transpose((1, 2, 0))

        if args.tile is not None:
            # Post-process tiled images
            # Add your post-processing code here if needed
            pass

        # Save denoised images
        utils.save_img(rgb_restored*255.0, os.path.join(args.result_dir, filenames[0]))

print("Denoising completed and results saved in:", args.result_dir)
