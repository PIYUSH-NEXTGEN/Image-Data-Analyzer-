# Image-Data-Analyzer-
This project performs a low-level statistical analysis of digital images using Python, NumPy, and PIL, without relying on high-level image processing libraries for understanding image data numerically by examining pixel distributions, color channel behavior, brightness, and histogram-based intensity segmentation.

The project supports both RGB and grayscale images and compares multiple images to determine relative brightness.

# Key Concepts Used -

Digital image representation as NumPy arrays

RGB color channels

Grayscale vs RGB handling

Statistical measures (mean, standard deviation, min, max)

Histogram-based intensity analysis

Brightness comparison using pixel averages

# Tech Stack -

Python

NumPy – numerical computation on pixel data.

Pillow (PIL) – image loading and color conversion .

# Functional Description
1️.Image Loading and Preprocessing
Images are loaded using PIL. If an image is originally grayscale (mode == 'L'), it is detected and reported. All images are then converted to RGB format to ensure uniform processing.
Each image is converted into a NumPy array of shape:
(height, width, 3)

2. Image-Level Statistical Analysis

For each image, the following statistics are computed:
Shape of the image array
Data type of pixel values
Mean pixel intensity
Standard deviation
Minimum and maximum pixel values
These metrics provide a global numerical description of the image.

3️. Channel-Wise Color Statistics

Each RGB channel is separated and analyzed independently.
For Red, Green, and Blue channels, the following are calculated:

Mean intensity
Standard deviation
Minimum intensity
Maximum intensity

4️. Brightness Estimation and Comparison

Image brightness is computed by:
Averaging RGB values per pixel
Taking the mean over the entire image
This produces a single scalar brightness value per image, allowing direct comparison.
The brighter image is determined using a simple conditional check.

5️. Histogram-Based Intensity Analysis

A histogram with 256 bins (0–255) is computed to represent pixel intensity distribution.
Pixel intensities are categorized into three regions:
Dark region (low intensity values)
Mid region
Bright region (high intensity values)
