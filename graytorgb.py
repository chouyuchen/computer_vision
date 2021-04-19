from cv2 import cv2
import numpy as np

for i in range(140):
    image = cv2.imread("./finish/img{}.bmp".format(i + 1))
    color = cv2.cvtColor(image, cv2.GRAY2BGR)
    cv2.imwrite("./finish/img{}.png".format(i), color)
    print("save img{}".format(i))