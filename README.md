# THRESHOLDING
## Aim
To segment the image using global thresholding, adaptive thresholding and Otsu's thresholding using python and OpenCV.

## Software Required
1. Anaconda - Python 3.7
2. OpenCV

## Algorithm

### Step1:
Load the required libraries like OpenCV, NumPy, and Matplotlib.
<br>
### Step2:
Read the input image from the file and convert it to grayscale using OpenCV.
<br>
### Step3:
Apply different thresholding techniques:

Global thresholding (binary, binary inverse, truncate, to zero, to zero inverse). Otsu’s thresholding. Adaptive thresholding (mean, Gaussian).
<br>

### Step4:
Store the results of each thresholding operation in a list for easy visualization.
<br>

### Step5:
Display the original grayscale image and the thresholded images side by side using Matplotlib to compare results.
<br>

## Program

```python
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

```
## Output

### Original Image
![image](https://github.com/user-attachments/assets/a0075d87-1697-4c7d-858e-113f42524c48)

### Global Thresholding
![image](https://github.com/user-attachments/assets/78f15983-87e3-4c67-97cd-5eec37de460e)

![image](https://github.com/user-attachments/assets/2a99992d-1775-4b15-a74c-d66b76f8bc2a)

![image](https://github.com/user-attachments/assets/12972326-f500-442d-b9de-6ad7ca4975ce)

![image](https://github.com/user-attachments/assets/466396f7-5cab-4672-97da-7e504cf296b4)

![image](https://github.com/user-attachments/assets/76e799dc-6cfd-466b-b6c7-a09fc0450f25)


### Adaptive Thresholding
![image](https://github.com/user-attachments/assets/0f8229e9-b6c9-49c4-8083-4ff5d0957dcd)

![image](https://github.com/user-attachments/assets/a0a315c1-07f7-4558-80fc-e2fc1a06ea8e)


### Optimum Global Thesholding using Otsu's Method
![image](https://github.com/user-attachments/assets/34b55264-8df5-4abf-80ba-c3088097fe08)

## Result
Thus the images are segmented using global thresholding, adaptive thresholding and optimum global thresholding using python and OpenCV.
