# resize the picture with only knowing directory instead of the filenames
import os

import numpy as np
from cv2 import cv2


array_of_img = []  # this if for store all of the image data
# this function is for read image,the input is directory name
def read_directory(directory_name):
    # this loop is for read each image in this foder,directory_name is the foder name with images.
    for filename in os.listdir(r"./" + directory_name):
        print(filename)  # just for test
        # img is used to store the image data
        img = cv2.imread(directory_name + "/" + filename)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        array_of_img.append(img)


def crop(image):
    cols, rows = image.shape[:2]
    print(cols, rows)
    x = 0
    y = 500
    xs = 2048
    ys = 1200
    crop_img = image[y : y + ys, x : x + xs]
    result = "./resize_TEST/test({}).jpg".format(len(array_of_img))
    cv2.imwrite(result, crop_img)
    print("{} success\n".format(result))


# 傳入檔名
read_directory("resize")
for s in array_of_img:
    crop(s)


"""
#路徑中盡量不要有中文名字會造成判讀困難跟錯誤
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
