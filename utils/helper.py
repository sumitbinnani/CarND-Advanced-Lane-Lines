import cv2
import matplotlib.pyplot as plt


def show_image_cv2(img):
    """Returns cv2 image
    in matplotlib format
    """
    return plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
