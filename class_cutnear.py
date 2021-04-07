from cv2 import cv2
import numpy as np


for i in range(224):
    # print(i)
    image = cv2.imread("./20210223train/train/NG_1/train_NG1_{}.jpg".format(i + 1))
    cols, rows = image.shape[:2]

    # print("cols,rows:{},{}", cols, rows)
    # 裁切區域的 x 與 y 座標（左上角）
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

    # subtract the y-gradient from the x-gradient
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    # 梯度图像中不大于90的任何像素都设置为0（黑色）。 否则，像素设置为255（白色）
    # blur and threshold the image
    blurred = cv2.blur(gradient, (9, 9))
    (_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)

    # 身体区域有很多黑色的空余，我们要用白色填充这些空余，使得后面的程序更容易识别昆虫区域
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # 从图像上还有一些小的白色斑点，这会干扰之后的昆虫轮廓的检测，要把它们去掉。分别执行4次形态学腐蚀与膨胀。
    # perform a series of erosions and dilations
    closed = cv2.erode(closed, None, iterations=4)
    closed = cv2.dilate(closed, None, iterations=4)

    (cnts, _) = cv2.findContours(
        closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

    # compute the rotated bounding box of the largest contour
    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))
    # cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
    # cv2.imwrite("test_bounding.jpg", image)

    Xs = [i[0] for i in box]
    Ys = [i[1] for i in box]
    x1 = min(Xs)
    x2 = max(Xs)
    y1 = min(Ys)
    y2 = max(Ys)
    hight = y2 - y1
    width = x2 - x1

    # 裁切區域的長度與寬度
    xs = 2000
    ys = 500

    if hight > 1000 or width > 1850:
        print("skip")
        continue
    elif x1 < 0:
        print("x1<0")
        x = 0
        crop_img = image[y1 : y1 + ys, x - 150 : x + xs - 150]
        result = "./20210223train/train/NG/crop_NG1_{}.jpg".format(i + 1)
        cv2.imwrite(result, crop_img)

    else:
        crop_img = image[y1 : y1 + ys, x1 : x1 + xs]
        result = "./20210223train/train/NG/crop_NG1_{}.jpg".format(i + 1)
        cv2.imwrite(result, crop_img)

    print("{} success\n".format(i + 1))