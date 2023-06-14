# Image Filter and Enhancement Application

This is a Python application that allows you to load an image, apply various filters, adjust contrast and brightness, and save the modified image.

## Functionality

- The application uses the `cv2` module from OpenCV to perform image processing operations.
- Upon running the application, a file explorer dialog opens, allowing you to select an image file.
- After selecting a file, the application displays the original image and provides a graphical user interface (GUI) to control various image processing parameters.
- The GUI includes the following sliders:
  - **Contrast**: Adjusts the contrast of the image.
  - **Brightness**: Adjusts the brightness of the image.
  - **Filter**: Allows you to choose from a set of predefined convolution kernels to apply different image filters.
  - **Grayscale**: Toggles between color and grayscale display modes.
- As you adjust the sliders, the application dynamically updates the modified image.
- Pressing the 's' key saves the modified image as a PNG file in the current directory. The file name is incremented automatically.
- Pressing the 'q' key quits the application.

## Prerequisites

To run this application, you need to have the following dependencies installed:

- Python 3.x
- OpenCV (cv2)
- NumPy
- tkinter (usually included with Python)

You can install the required packages using `pip`:

```shell
pip install opencv-python numpy tkinter

## Usage

1. Clone the repository or download the source code files.
2. Install the dependencies mentioned in the Prerequisites section.
3. Run the Python script `image_filter.py`.
4. In the file explorer dialog, select an image file and click **Open**.
5. Use the sliders in the GUI to adjust the image processing parameters and observe the modified image in real-time.
6. Press the 's' key to save the modified image.
7. Press the 'q' key to exit the application.

## Contributing

Contributions to the project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.