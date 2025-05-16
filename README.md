# License Plate Detection using OpenCV

This project detects and extracts vehicle license plates from images using OpenCV in Python. The script uses edge detection and contour approximation to find rectangular regions that are likely license plates.

## Features

- Reads an input image file
- Converts it to grayscale
- Detects edges using Canny edge detector
- Finds contours and filters for rectangular shapes with typical license plate aspect ratio
- Highlights the detected license plate in the image
- Displays the original image, contours, and the detected plate region
