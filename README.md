Image Thresholding in OpenCV 🖼️
I am currently learning OpenCV from the Tech With Sagar YouTube channel, and this project demonstrates image thresholding, a fundamental technique in computer vision.

What is Thresholding?
Thresholding is a method to separate the foreground from the background in an image based on pixel intensity. It’s widely used in image preprocessing, object detection, and segmentation.

Threshold Types Used in This Project:
cv2.THRESH_BINARY → Pixels > T → max value, else 0
cv2.THRESH_BINARY_INV → Inverted binary
cv2.THRESH_TRUNC → Pixels > T → T, else unchanged
cv2.THRESH_TOZERO → Pixels > T → unchanged, else 0
cv2.THRESH_TOZERO_INV → Pixels > T → 0, else unchanged

🔹 Quick visual idea
BINARY → light object on dark background
BINARY_INV → dark object on light background
TRUNC → everything above threshold becomes T
TOZERO → keeps bright parts, removes dark
TOZERO_INV → keeps dark parts, removes bright

Purpose:
The project shows how different threshold types affect image appearance and help understand how foreground-background separation works.

How to Run:
Clone the repository.
Place an image in the project folder.
Run the Python script (python threshold_demo.py).
Observe the original and thresholded images.

Learning Highlights:
How to use different threshold types in OpenCV
How thresholding helps in preprocessing for computer vision tasks

Understanding the difference between binary, inverted, trunc, and zero-based thresholds
