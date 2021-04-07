# coding:utf-8
# https://www.itread01.com/content/1546447870.html
# https://blog.csdn.net/liqiancao/article/details/55670749

import numpy as np
from cv2 import cv2

# 下載圖片轉成灰階圖
image = cv2.imread("./cutout_result/test_crop_NG(1).jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("test.bmp", gray)

# 利用Sobel 檢測原理，偵測出邊緣
# 计算x，y方向上的梯度，之后在x方向上减去y方向上的梯度，通过这个减法，我们留下具有高水平梯度和低垂直梯度的图像区
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
cv2.imwrite("test_morphology.bmp", closed)


# 从图像上还有一些小的白色斑点，这会干扰之后的昆虫轮廓的检测，要把它们去掉。分别执行4次形态学腐蚀与膨胀。
# perform a series of erosions and dilations
closed = cv2.erode(closed, None, iterations=4)
closed = cv2.dilate(closed, None, iterations=4)
cv2.imwrite("test_iterations.bmp", closed)

(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
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
cropImg = image[y1 : y1 + hight, x1 : x1 + width]
print("for the 4 coordinate:")
print(x1, x2, y1, y2)
cv2.imwrite("cutout.jpg", cropImg)


# resize
x = 0
y = 0
# 裁切區域的長度與寬度
xs = 1100
ys = 540
resizeImg = cropImg[y : y + ys, x : x + xs]
cv2.imwrite("result.jpg", resizeImg)
