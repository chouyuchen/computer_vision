from cv2 import cv2
from PIL import Image

image = cv2.imread("./01.bmp")
h = image.shape[0]
w = image.shape[1]
print("hight,width: {}, {}".format(h, w))
"""
batch = image[0:1000, 0:900]
batch = cv2.resize(batch, (w, h), interpolation=cv2.INTER_AREA)
cv2.imwrite("background.bmp", batch)
"""