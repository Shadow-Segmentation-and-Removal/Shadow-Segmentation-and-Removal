import cv2
import torch

# Load the image using OpenCV
image = cv2.imread("/teamspace/studios/this_studio/SAM-Adapter-PyTorch/masks/1.png")

# Convert the image to a PyTorch tensor
tensor = torch.tensor(image)

# Check the shape of the tensor
print("Shape of the tensor:", tensor.shape)
