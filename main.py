import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt


def flip_image(image_array, mode='horizontal'):
    height, width, channels = image_array.shape
    flipped_image = np.zeros_like(image_array)

    if mode == 'horizontal':
        for y in range(height):
            for x in range(width):
                flipped_image[y, x] = image_array[y, width - x - 1]
    elif mode == 'vertical':
        for y in range(height):
            flipped_image[y] = image_array[height - y - 1]
    else:
        raise ValueError("Invalid mode. Use 'horizontal' or 'vertical'.")

    return flipped_image


def rotate_image(image_array, angle):
    height, width, channels = image_array.shape
    rotated_image = np.empty_like(image_array)

    if angle == 90:
        rotated_image = np.empty((width, height, channels), dtype=image_array.dtype)
        for y in range(height):
            for x in range(width):
                rotated_image[x, height - y - 1] = image_array[y, x]
    elif angle == 180:
        for y in range(height):
            for x in range(width):
                rotated_image[height - y - 1, width - x - 1] = image_array[y, x]
    elif angle == 270:
        rotated_image = np.empty((width, height, channels), dtype=image_array.dtype)
        for y in range(height):
            for x in range(width):
                rotated_image[width - x - 1, y] = image_array[y, x]
    else:
        raise ValueError("Invalid angle. Use 90, 180, or 270 degrees.")

    return rotated_image


# Example usage:
image_array = imread("./01.jpg")

# Display the original image
plt.imshow(image_array)
plt.title("Original Image")
plt.show()

# Flip horizontally
flipped_horizontal = flip_image(image_array, mode='horizontal')
plt.imshow(flipped_horizontal)
plt.title("Flipped Horizontally")
plt.show()

# Flip vertically
flipped_vertical = flip_image(image_array, mode='vertical')
plt.imshow(flipped_vertical)
plt.title("Flipped Vertically")
plt.show()

# Rotate the image by 90 degrees
rotated_image_90 = rotate_image(image_array, angle=90)
plt.imshow(rotated_image_90)
plt.title("Rotated Image (90 degrees)")
plt.show()

# Rotate the image by 180 degrees
rotated_image_180 = rotate_image(image_array, angle=180)
plt.imshow(rotated_image_180)
plt.title("Rotated Image (180 degrees)")
plt.show()

# Rotate the image by 270 degrees
rotated_image_270 = rotate_image(image_array, angle=270)
plt.imshow(rotated_image_270)
plt.title("Rotated Image (270 degrees)")
plt.show()
