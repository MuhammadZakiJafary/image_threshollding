import cv2
import numpy as np
image=cv2.imread("C:\\Users\\Hanzalah\\Downloads\\mz.png",cv2.IMREAD_GRAYSCALE)
image=cv2.resize(image,(300,400))

edgess = cv2.threshold(image, 125, 255, cv2.THRESH_BINARY)
#BINARY → light object on dark background
thresh_inv = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
#BINARY_INV → dark object on light background
thresh_trunc = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
#TRUNC → everything above threshold becomes T
thresh_tozero = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
#TOZERO → keeps bright parts, removes dark
thresh_tozero_inv = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
#TOZERO_INV → keeps dark parts, removes bright
cv2.imshow("Original Image", image)
#We use the edges[1] beacause the treshold generate 2 values 
#[0] is the threshold value and [1] is the thresholded image
cv2.imshow("Threshold Image", edgess[1])
cv2.imshow("Inverted Threshold Image", thresh_inv[1])
cv2.imshow("Truncated Threshold Image", thresh_trunc[1])
cv2.imshow("To Zero Threshold Image", thresh_tozero[1])
cv2.imshow("To Zero Inverted Threshold Image", thresh_tozero_inv[1])
cv2.waitKey(0)
cv2.destroyAllWindows()
