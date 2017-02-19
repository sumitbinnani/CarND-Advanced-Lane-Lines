import cv2
import numpy as np


def s_threshold(img, min=170, max=255):
    """Returns S channel thresholded
    by min and max values
    """
    # Convert to HLS color space and separate the S channel
    hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    s_channel = hls[:, :, 2]
    s_binary = np.zeros_like(s_channel)
    s_binary[(s_channel >= min) & (s_channel <= max)] = 1
    return s_binary


def sobelx_threshold(gray, min=20, max=255):
    """Returns sobel derviative in x-direction thresholded
    by min and max values
    """
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)  # Take the derivative in x
    abs_sobelx = np.absolute(sobelx)  # Absolute x derivative to accentuate lines away from horizontal
    scaled_sobel = np.uint8(255 * abs_sobelx / np.max(abs_sobelx))
    sxbinary = np.zeros_like(scaled_sobel)
    sxbinary[(scaled_sobel >= min) & (scaled_sobel <= max)] = 1
    return sxbinary


def hsv_mask(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_white = np.array([0,0,225], dtype=np.uint8)
    upper_white = np.array([180,255,255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_white, upper_white)
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

