import os
import random
import matplotlib.pyplot as plt

# Function to plot images side by side with filename
def plot_images(image1_path, image2_path, filename):
    # Load the images
    image1 = plt.imread(image1_path)
    image2 = plt.imread(image2_path)
    
    # Create a figure and axes
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    # Plot the first image
    axes[0].imshow(image1)
    axes[0].set_title('Shadowed image')
    axes[0].axis('off')
    
    # Plot the second image
    axes[1].imshow(image2)
    axes[1].set_title('Deshadowed Output')
    axes[1].axis('off')
    
    # Display the filename
    fig.suptitle(filename, fontsize=12)
    
    # Show the plot
    plt.show()

# Directory paths containing the images
folder1_path = '/teamspace/studios/this_studio/SAM-Adapter-PyTorch/ISTD_remastered/test_A'
folder2_path = '/teamspace/studios/this_studio/ShadowFormer/results'

# List the files in both folders
folder1_files = os.listdir(folder1_path)
folder2_files = os.listdir(folder2_path)

# Randomly select 10 different filenames
random_files = random.sample(folder1_files, 10)

# Plot the randomly selected images
for filename in random_files:
    image1_path = os.path.join(folder1_path, filename)
    image2_path = os.path.join(folder2_path, filename)
    plot_images(image1_path, image2_path, filename)
