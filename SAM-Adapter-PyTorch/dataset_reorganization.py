import os
import shutil

# Function to rename files sequentially and save them in a new directory
def rename_and_save(directory, new_directory):
    files = os.listdir(directory)
    files.sort()  # Sort files to ensure they are in the same order
    os.makedirs(new_directory, exist_ok=True)  # Create new directory if it doesn't exist
    for i, filename in enumerate(files, start=1):
        new_filename = str(i) + os.path.splitext(filename)[1]  # Keep file extension
        shutil.copy(os.path.join(directory, filename), os.path.join(new_directory, new_filename))

# Directory paths for images and masks
images_dir = '/teamspace/studios/this_studio/SAM-Adapter-PyTorch/ISTD_Dataset/test/test_A'
masks_dir = '/teamspace/studios/this_studio/SAM-Adapter-PyTorch/ISTD_Dataset/test/test_B'
unshadowed_dir = '/teamspace/studios/this_studio/SAM-Adapter-PyTorch/ISTD_Dataset/test/test_C'
output_dir = '/teamspace/studios/this_studio/SAM-Adapter-PyTorch/ISTD_reorganised/'  # New directory to save renamed files

# Rename and save images
rename_and_save(images_dir, os.path.join(output_dir, 'test_A'))

# Rename and save masks
rename_and_save(masks_dir, os.path.join(output_dir, 'test_B'))
rename_and_save(unshadowed_dir, os.path.join(output_dir, 'test_C'))