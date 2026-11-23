
# Import required libraries
from PIL import Image             # Used to open and work with images
import numpy as np                # Used to convert images into NumPy arrays
import matplotlib.pyplot as plt   # Used to display images

# Load the original image
# Update the image file path according to the location where you have saved the project on your computer.
img = Image.open(r"<Update the image file path according to the location where you have saved the project on your computer.>")
## Image.open() reads the image from the specified location.

# Convert the image into a NumPy array
img_arr = np.asarray(img)

# print(img_arr)                   # Displays pixel values
# print(img_arr.shape)             # Displays image dimensions (height, width, channels)


'''------------------ Remove Red Channel ----------------------'''

img_arr_red = img_arr.copy()
# Creates a copy of the original image array to protect the original.

img_arr_red[:, :, 0] = 0
# 0 represents the Red channel in RGB.
# Sets all Red channel values to 0, i.e., absence of Red colour.


'''------------------ Remove Green Channel ----------------------'''

img_arr_green = img_arr.copy()
# Creates another copy of the original image array.

img_arr_green[:, :, 1] = 0
# 1 represents the Green channel in RGB.
# Sets all Green channel values to 0, i.e., absence of Green colour.


'''------------------ Remove Blue Channel ----------------------'''

img_arr_blue = img_arr.copy()
# Creates another copy of the original image array.

img_arr_blue[:, :, 2] = 0
# 2 represents the Blue channel in RGB.
# Sets all Blue channel values to 0, i.e., absence of Blue colour.


'''------------------ Display Original and Modified Images ----------------------'''

# Create a layout with 4 rows and 2 columns
fig, axes = plt.subplots(4, 2, figsize=(5, 10))
# 4 rows = Original + 3 colour channel comparisons
# 2 columns = Original image and modified image

# Main heading for the complete comparison
fig.suptitle("RGB Image Channel Manipulation", fontsize=10)

#imshow() places each image in its respective row and column

# Row 1: Original image
axes[0, 0].imshow(img) #imshow() = Show image
axes[0, 0].set_title("Original Image")
axes[0, 0].axis("off") #Without this line, Matplotlib displays numbers along the X-axis and Y-axis around the image.
                       #With this line, only the image is visible, making the output cleaner.

axes[0, 1].imshow(img)
axes[0, 1].set_title("Original Image(As Rendered by Matplotlib)") #Matplotlib is displaying the loaded image, not that we have changed its RGB channels
axes[0, 1].axis("off")


# Row 2: Red channel removal
axes[1, 0].imshow(img)
axes[1, 0].set_title("Original Image")
axes[1, 0].axis("off")

axes[1, 1].imshow(img_arr_red)
axes[1, 1].set_title("Red Channel Removed")
axes[1, 1].axis("off")


# Row 3: Green channel removal
axes[2, 0].imshow(img)
axes[2, 0].set_title("Original Image")
axes[2, 0].axis("off")

axes[2, 1].imshow(img_arr_green)
axes[2, 1].set_title("Green Channel Removed")
axes[2, 1].axis("off")


# Row 4: Blue channel removal
axes[3, 0].imshow(img)
axes[3, 0].set_title("Original Image")
axes[3, 0].axis("off")

axes[3, 1].imshow(img_arr_blue)
axes[3, 1].set_title("Blue Channel Removed")
axes[3, 1].axis("off")


# Adjust spacing between images and headings
plt.tight_layout()

# Display all images(4 rows and 2 columns together) in one window
plt.show() 
