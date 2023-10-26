import cv2 
import numpy as np 
 
def binary_array(array, thresh, value=0):
  
  if value == 0:
    binary = np.ones_like(array) 
         
  else:
    binary = np.zeros_like(array)  
    value = 1
 
  binary[(array >= thresh[0]) & (array <= thresh[1])] = value 
  return binary
 
def blur_gaussian(channel, ksize=3):  
  return cv2.GaussianBlur(channel, (ksize, ksize), 0)
         
def mag_thresh(image, sobel_kernel=3, thresh=(0, 255)):   
  sobelx = np.absolute(sobel(image, orient='x', sobel_kernel=sobel_kernel))          
  sobely = np.absolute(sobel(image, orient='y', sobel_kernel=sobel_kernel))  
  mag = np.sqrt(sobelx ** 2 + sobely ** 2)   
  return binary_array(mag, thresh)
 
def sobel(image, orient='x', sobel_kernel=3):
    
    if orient == 'x':
        sobel_image = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
    elif orient == 'y':
        sobel_image = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
    else:
        raise ValueError("Invalid orientation. Use 'x' or 'y'.")

    return sobel_image
 
def threshold(channel, thresh=(128,255), thresh_type=cv2.THRESH_BINARY):
  return cv2.threshold(channel, thresh[0], thresh[1], thresh_type)