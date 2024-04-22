import cv2
import os
import argparse
from glob import glob

# Function to resize an image
def resize_image(input_path, output_path, target_width, target_height):
    # Load the image
    image = cv2.imread(input_path)
    
    # Resize the image to the desired shape
    resized_image = cv2.resize(image, (target_width, target_height))
    
    # Save the resized image as PNG
    cv2.imwrite(output_path, resized_image, [cv2.IMWRITE_PNG_COMPRESSION, 9])

# Argument parser
parser = argparse.ArgumentParser(description="Resize images to a specified width and height and save them as PNG.")
parser.add_argument("--input_dir", help="Path to the directory containing input images.")
parser.add_argument("--output_dir", default= "/teamspace/studios/this_studio/SAM-Adapter-PyTorch/ISTD_remastered/test_A", help="Path to the directory where resized images will be saved.")
parser.add_argument("--target_width", type=int, default=480, help="Width of the resized images.")
parser.add_argument("--target_height", type=int, default=640, help="Height of the resized images.")
args = parser.parse_args()

# Create the output directory if it doesn't exist
os.makedirs(args.output_dir, exist_ok=True)

# Loop through each image file in the input directory
for filename in os.listdir(args.input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        # Get the full path of the input image
        input_path = os.path.join(args.input_dir, filename)
        
        # Construct the output path for the resized image
        output_path = os.path.join(args.output_dir, os.path.splitext(filename)[0] + ".png")
        
        # Resize the image and save it
        resize_image(input_path, output_path, args.target_width, args.target_height)
        print(f"Resized image '{filename}' saved to '{output_path}'")
