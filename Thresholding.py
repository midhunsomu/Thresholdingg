
#NAME : MIDHUN S
#REF NO : 212223240087


import numpy as np
import cv2
import matplotlib.pyplot as plt
image = cv2.imread("flower.jpeg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh_dipt1 = cv2.threshold(image_gray, 86, 255, cv2.THRESH_BINARY)
ret, thresh_dipt2 = cv2.threshold(image_gray, 86, 255, cv2.THRESH_BINARY_INV)
ret, thresh_dipt3 = cv2.threshold(image_gray, 86, 255, cv2.THRESH_TOZERO)
ret, thresh_dipt4 = cv2.threshold(image_gray, 86, 255, cv2.THRESH_TOZERO_INV)
ret, thresh_dipt5 = cv2.threshold(image_gray, 100, 255, cv2.THRESH_TRUNC)

ret, thresh_dipt6 = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

thresh_dipt7 = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thresh_dipt8 = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles = [
    "Gray Image", 
    "Threshold Image (Binary)", 
    "Threshold Image (Binary Inverse)", 
    "Threshold Image (To Zero)", 
    "Threshold Image (To Zero-Inverse)", 
    "Threshold Image (Truncate)", 
    "Otsu's Threshold", 
    "Adaptive Threshold (Mean)", 
    "Adaptive Threshold (Gaussian)"
]

images = [
    image_gray, thresh_dipt1, thresh_dipt2, thresh_dipt3, 
    thresh_dipt4, thresh_dipt5, thresh_dipt6, thresh_dipt7, thresh_dipt8
]

for i in range(9):
    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image)
    plt.axis("off")
    plt.subplot(1, 2, 2)
    plt.title(titles[i])
    plt.imshow(cv2.cvtColor(images[i],cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()
