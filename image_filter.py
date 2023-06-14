import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Create the Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open the file explorer dialog
file_path = filedialog.askopenfilename()

# Check if a file was selected
if file_path:
    # Load the image using cv2
    color_orig = cv2.imread(file_path)
else:
    print("No file selected.")

# make a grayscale copy
gray_orig = cv2.cvtColor(color_orig, cv2.COLOR_BGR2GRAY)

# dummy function that does nothing
def dummy(value):
    pass

# define convolution kernels
identity_kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
gaussian_kernel1 = cv2.getGaussianKernel(3, 0)
gaussian_kernel2 = cv2.getGaussianKernel(5, 0)
box_kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.float32) / 9.0

kernels = [identity_kernel, sharpen_kernel, gaussian_kernel1, gaussian_kernel2, box_kernel]

# create the UI - window and sliders
cv2.namedWindow('app')
cv2.createTrackbar('contrast', 'app', 1, 100, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, len(kernels)-1, dummy)
cv2.createTrackbar('grayscale', 'app', 0, 1, dummy)

# main UI loop
count = 1
while True:
    grayscale = cv2.getTrackbarPos('grayscale', 'app')
    contrast = cv2.getTrackbarPos('contrast', 'app')
    brightness = cv2.getTrackbarPos('brightness', 'app')
    kernel_idx = cv2.getTrackbarPos('filter', 'app')
    
    # Apply the selected filter to the color and grayscale images
    color_modified = cv2.filter2D(color_orig, -1, kernels[kernel_idx])
    gray_modified = cv2.filter2D(gray_orig, -1, kernels[kernel_idx]) 
    
    # Adjust contrast and brightness of the modified images
    color_modified = cv2.addWeighted(color_modified, contrast, np.zeros_like(color_orig), 0, (brightness-50))
    gray_modified = cv2.addWeighted(gray_modified, contrast, np.zeros_like(gray_orig), 0, (brightness-50))
    
    # Wait for a key press
    key = cv2.waitKey(100)
    if key == ord('q'):  # Quit if 'q' is pressed
        break
    elif key == ord('s'):  # Save the modified image if 's' is pressed
        if grayscale == 0:
            cv2.imwrite('output_{}.png'.format(count), color_modified)
        else:
            cv2.imwrite('output_{}.png'.format(count), gray_modified)
        count += 1
    
    # Show the modified image
    if grayscale == 0:
        cv2.imshow('app', color_modified)
    else:
        cv2.imshow('app', gray_modified)

# Cleanup
cv2.destroyAllWindows()