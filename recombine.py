import random

import numpy as np
from cv2 import cv2
from PIL import Image

image = cv2.imread("./001.bmp")
img = cv2.imread("./001.m.png")
h = image.shape[0]
w = image.shape[1]
print("hight,width: {}, {}".format(h, w))

# crop
x = 1270
radius = 630
y = 900
topic1 = image[y : y + radius, x : x + radius]
topic2 = img[y : y + radius, x : x + radius]
cv2.imwrite("crop.bmp", topic1)
cv2.imwrite("crop.m.png", topic2)

# rotate
cols, rows = topic2.shape[:2]
for i in range(2, 120):
    angle = 3.0 * i
    print("image angle: ", angle)
    # 第一个参数旋转中心，第二个参数旋转角度，第三个参数：缩放比例
    M1 = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    # print(M)
    # 第三个参数：变换后的图像大小
    res1 = cv2.warpAffine(topic1, M1, (rows, cols))
    res2 = cv2.warpAffine(topic2, M1, (rows, cols))
    result1 = "./pic01/cut_{}.bmp".format(3 * i)
    result2 = "./pic01/cut_{}.m.png".format(3 * i)
    cv2.imwrite(result1, res1)
    cv2.imwrite(result2, res2)
    print("{} ,{} success".format(result1, result2))

    for j in range(3):
        # paste
        start = 0
        stop = 1400
        x = random.randrange(start, stop, 1)
        y = random.randrange(start, stop, 1)
        print(x, y)

        to_image1 = Image.open("background.bmp")
        to_image2 = Image.new("RGB", (w, h))
        image_from1 = Image.open("./pic01/cut_{}.bmp".format(3 * i))
        image_from2 = Image.open("./pic01/cut_{}.m.png".format(3 * i))
        to_image2.paste(image_from2, (x, y))
        to_image1.paste(image_from1, (x, y))
        to_image1.save("./pic01_gen/Rotate{}_{}.bmp".format(3 * i, j))
        to_image2.save("./pic01_gen/Rotate{}_{}.m.png".format(3 * i, j))

        # converted image into 8 bits(only for png)
        new = Image.open("./pic01_gen/Rotate{}_{}.m.png".format(3 * i, j))
        src = Image.open("./001.m.png")
        converted = new.quantize(palette=src)
        converted.save("./pic01_gen/Rotate{}_{}.m.png".format(3 * i, j))
        print("succeed convert img{} {}.m.png".format(3 * i, j))
