from cv2 import cv2

"""
for k in range(6):
    print(k)
    image = cv2.imread("./pic_origin/{}.bmp".format(k + 1))
    # h = image.shape[0]
    # w = image.shape[1]
    # print("hight,width: {}, {}".format(h, w))
    w = 1020
    x = 530
    y = 0
    h = 1250
    image = image[y : y + h, x : x + w]
    # image = image[:, x : x + w]
    h_ = image.shape[0]
    w_ = image.shape[1]
    print("hight,width: {}, {}".format(h_, w_))
    cv2.imwrite("./pic_origin/crop/0{}.bmp".format(k + 1), image)
"""


for k in range(6):
    image = cv2.imread("./pic_origin/{}.m.png".format(k + 1))
    w = 1020
    x = 530
    y = 0
    h = 1250
    image = image[y : y + h, x : x + w]
    # image = image[:, x : x + w]
    cv2.imwrite("./pic_origin/crop/{}.m.png".format(k + 1), image)
    h_ = image.shape[0]
    w_ = image.shape[1]
    print("hight,width: {}, {}".format(h_, w_))
    print("succeed crop img{}".format(k + 1))
