# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 18:46:26 2021

@author: lenovo
"""


import cv2
from matplotlib import pyplot as plt
import numpy

im = cv2.imread("foot.png")
# B = im[:,:,2]
# plt.imshow(B)
# Y = 255-B
# plt.imshow(Y)

gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) 
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
# thresh = cv2.adaptiveThreshold(Y,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#             cv2.THRESH_BINARY_INV,35,5)

aa, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

x=[]
for i in range(0, len(contours)):
    if cv2.contourArea(contours[i]) > 172690:
        x.append(contours[i])
cv2.drawContours(im, x, -1, (255,0,0), 2) 

plt.imshow(im)