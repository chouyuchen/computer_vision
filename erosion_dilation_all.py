import cv2
import numpy as np

#讀取圖片"
for i in range(1,60,2):
    path = "./金屬件/rename/img_{}.bmp".format(i)
    print(path)
    image = cv2.imread(path)
    kernel = np.ones((4, 4), np.uint8)
    erosion = cv2.erode(image, kernel, iterations = 3)
    dilation =cv2.dilate(image, kernel, iterations = 3)
    #result1=erosion(image,kernel)
    #print("{}success\n".format(1))
    result1="./金屬件/Image_gen/Dilate_{}.bmp".format(i)
    result2="./金屬件/Image_gen/Erode_{}.bmp".format(i)
    cv2.imwrite(result1,dilation)
    cv2.imwrite(result2,erosion)

for i in range(2,60,2):
    path = "./金屬件/rename/img_{}.png".format(i)
    print(path)
    image = cv2.imread(path)
    #image = cv2.resize(image, (256, 256), interpolation=cv2.INTER_AREA)
    kernel = np.zeros((4, 4), np.uint8)
    erosion = cv2.erode(image, kernel, iterations = 3)
    dilation =cv2.dilate(image, kernel, iterations = 3)
    #result1=erosion(image,kernel)
    #print("{}success\n".format(1))
    result1="./金屬件/Image_gen/Dilate_{}({}).png".format(i-1,i-1)
    result2="./金屬件/Image_gen/Erode_{}({}).png".format(i-1,i-1)
    cv2.imwrite(result1,dilation)
    cv2.imwrite(result2,erosion) 