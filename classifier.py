# resize the picture
# the picture names are in sequence ;otherwise using class_image
import numpy as np
from cv2 import cv2

"""
image = cv2.imread("../PIC/2021train/test/NG/0000 (1).jpg")
cols, rows = image.shape[:2]
x = 0
y = 500
xs = 2048
ys = 1200
crop_img = image[y : y + ys, x : x + xs]
result = "../PIC/2021train/test/NG_resize/test_crop_NG(1).jpg"
cv2.imwrite(result, crop_img)
print("{} success\n".format(result))
"""


for i in range(537):
    # print(i)
    image = cv2.imread("../PIC/2021train/train/OK/3333 ({}).jpg".format(i + 1))
    cols, rows = image.shape[:2]
    # print("cols,rows:{},{}", cols, rows)
    # 裁切區域的 x 與 y 座標（左上角）
    x = 0
    y = 500
    # 裁切區域的長度與寬度
    xs = 2048
    ys = 1200
    crop_img = image[y : y + ys, x : x + xs]
    result = "../PIC/2021train/train/OK_resize/train_crop_OK({}).jpg".format(i + 1)
    cv2.imwrite(result, crop_img)
    print("{} success\n".format(result))
