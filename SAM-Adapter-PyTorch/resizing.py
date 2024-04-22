import cv2
import os
import argparse

# Function to resize an image
def resize_image(input_path, output_path, target_width, target_height):
    # Load the image
    image = cv2.imread(input_path)
    
    # Resize the image to the desired shape
    resized_image = cv2.resize(image, (target_width, target_height))
    
    # Save the resized image
    cv2.imwrite(output_path, resized_image)

# Parse the command-line arguments
parser = argparse.ArgumentParser(description='Resize images')
parser.add_argument('--input_dir', type=str, help='Directory containing input images')
parser.add_argument('--output_dir', type=str, help='Directory to save resized images')
parser.add_argument('--target_width', type=int, default=640, help='Target width for resizing')
parser.add_argument('--target_height', type=int, default=480, help='Target height for resizing')
args = parser.parse_args()

# Check if input directory is provided
if not args.input_dir:
    print("Input directory is required.")
    exit(1)

# Check if output directory is provided
if not args.output_dir:
    print("Output directory is required.")
    exit(1)

# Create the output directory if it doesn't exist
os.makedirs(args.output_dir, exist_ok=True)

# Loop through each image file in the input directory
for filename in os.listdir(args.input_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Get the full path of the input image
        input_path = os.path.join(args.input_dir, filename)
        
        # Construct the output path for the resized image
        output_path = os.path.join(args.output_dir, filename)
        
        # Resize the image and save it
        resize_image(input_path, output_path, args.target_width, args.target_height)
        print(f"Resized image '{filename}' saved to '{output_path}'")
