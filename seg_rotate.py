import numpy as np
import cv2

image = cv2.imread("1 (1).bmp")
img = cv2.imread("1 (1).m.png")
# image.shape[0]=height, img.shape[1]=width, img.shape[2]=channel
cols, rows = image.shape[:2]


for i in range(0, 25):
    angle = 15.0 * i
    print("image angle: ", angle)
    # 第一个参数旋转中心，第二个参数旋转角度，第三个参数：缩放比例
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    # print(M)
    # 第三个参数：变换后的图像大小
    res = cv2.warpAffine(image, M, (rows, cols))
    result = "./金屬件/Img_rotate/rotate{}.bmp".format(15 * i)
    cv2.imwrite(result, res)
    print("{} success\n".format(result))

for i in range(0, 25):
    angle = 15.0 * i
    print("image angle: ", angle)
    # 第一个参数旋转中心，第二个参数旋转角度，第三个参数：缩放比例
    M1 = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    # print(M)
    # 第三个参数：变换后的图像大小
    res = cv2.warpAffine(img, M1, (rows, cols))
    result1 = "./金屬件/Img_rotate/rotate{}({}).m.png".format(15 * i, 15 * i)
    cv2.imwrite(result1, res)
    print("{} success\n".format(result1))