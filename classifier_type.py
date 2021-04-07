from cv2 import cv2
import numpy as np

"""
# cutoff the unnecessary part
def resizeImg(cropImg):
    # resize
    x = 0
    y = 0
    # 裁切區域的長度與寬度
    xs = 1100
    ys = 540
    resizeImg = cropImg[y : y + ys, x : x + xs]
    return resizeImg
"""


def check(x):
    if x < 0:
        x = 0
    else:
        pass
    return x


# main function
for i in range(236, 536):
    print(i)
    image = cv2.imread("../PIC/2021train/train/OK/3333  ({}).jpg".format(i + 1))
    col, row = image.shape[:2]
    gray = cv2.imread(
        "../PIC/2021train/train/OK/3333  ({}).jpg".format(i + 1), cv2.IMREAD_GRAYSCALE
    )
    cols, rows = gray.shape[:2]

    gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    blurred = cv2.blur(gradient, (9, 9))
    (_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    closed = cv2.erode(closed, None, iterations=4)
    closed = cv2.dilate(closed, None, iterations=4)

    (cnts, _) = cv2.findContours(
        closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))
    # cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
    # cv2.imwrite("test_bounding.jpg", image)

    Xs = [i[0] for i in box]
    Ys = [i[1] for i in box]
    x1s = min(Xs)
    x2s = max(Xs)
    y1s = min(Ys)
    y2s = max(Ys)
    x1 = check(x1s)
    x2 = check(x2s)
    y1 = check(y1s)
    y2 = check(y2s)
    hight = y2 - y1
    width = x2 - x1
    cropImg = image[y1 : y1 + hight, x1 : x1 + width]
    print("for the 4 coordinate:")
    print(x1, x2, y1, y2)
    name = "../PIC/2021train/train/cutoff_OK/train_OK_({}).jpg".format(i + 1)
    cv2.imwrite(name, cropImg)
    print("{} success\n".format(name))
