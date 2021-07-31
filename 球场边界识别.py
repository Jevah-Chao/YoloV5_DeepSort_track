# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 18:36:30 2021

@author: lenovo
"""
import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils


im_path = "foot.png"
imgsrc = cv2.imread(im_path)
img = imgsrc

# Resize to improve detection accuracy

t = int(img.shape[1] * 1.6)
img = imutils.resize(imgsrc, width=t)


# Apply gaussian blur
kernel_size = 3
img = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

# Convert to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Initialize morph-kernel, apply CLOSE before Canny to improve edges detection
kernel0 = np.ones((9,27), np.uint8)
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel0)

# Detect edges
low_threshold = 5
high_threshold = 50
edges = cv2.Canny(img, low_threshold, high_threshold)

# Initialize morph-kerne, apply CLOSE after Canny to merge edges
kernel2 = np.ones((8,24), np.uint8)
edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel2)

# Hough Lines params
rho = 1  # distance resolution in pixels of the Hough grid
theta = np.pi / 180  # angular resolution in radians of the Hough grid
# minimum number of votes (intersections in Hough grid cell)
threshold = 0
min_line_length = 20  # minimumer of  numbpixels making up a line
max_line_gap = 5  # maximum gap in pixels between connectable line segments

# Run Hough on edge detected image
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

output = np.copy(imgsrc) * 0  # creating a blank to draw lines on
for line in lines:
    for x1, y1, x2, y2 in line:
        long = abs(x1 - x2) + abs(y1 -y2)
        # print (long)
        if long > 500:
            print (line)
            cv2.line(output, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 1)
        elif long > 50:
            cv2.line(output, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 255), 1)
plt.imshow(output)