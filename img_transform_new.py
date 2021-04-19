from cv2 import cv2
import numpy as np
from PIL import Image

# k 代表原圖為哪一張
for k in range(1, 2):
    print(k)

    # image = cv2.imread("./pic_origin/crop/0{}.bmp".format(k + 1))
    image = cv2.imread("./pic_origin/crop/{}.m.png".format(k + 1))
    h = image.shape[0]
    w = image.shape[1]
    print("hight,width: {}, {}".format(h, w))

    # cut（切割出想要的格式）
    # image_list = []
    cut_size = 125  # cut_size只總共切成幾張
    h_step = int(1250 / cut_size)  # 切割的每隔為step=1250/125=10

    for i in range(cut_size):
        image_cut = image[h_step * int(i) : h_step * int(i + 1), :, :]
        # print(h_step * int(i), h_step * int(i + 1))
        # image_list.append(image_cut)
        cv2.imwrite("./pic_gen/cut_size{}.png".format(i), image_cut)
        # cv2.imwrite("./pic_gen/cut_size{}.bmp".format(i), image_cut)
        print("save cut_size{}".format(i))

    # compose
    # 循環貼上，把照片按順序黏貼到對應位置上
    # start_index=i
    # pic_size=800/10=80
    pic_size = 80
    for i in range(cut_size):  # i 控制為哪一張切割圖片開始
        # 創一新圖片
        # to_image = Image.new("RGB", (w, 1400))
        to_image = Image.new("RGB", (w, 800))  # for png
        # to_image = Image.new("L", (w, 800))  # for bmp

        # 控制該跑(1)或者是(2)
        if i + 80 <= cut_size:
            # print("run 1")
            count = 0  # 開始貼的位置
            # paste image:
            # the first start (from the index)
            for j in range(i, i + pic_size):
                # print(count)
                image_from = Image.open("./pic_gen/cut_size{}.png".format(j))
                # image_from = Image.open("./pic_gen/cut_size{}.bmp".format(j))
                to_image.paste(image_from, (0, h_step * int(count)))  # 從0開始貼
                count += 1

        # print("from start:")
        else:
            count = 0
            # print("run 2")
            for j in range(i, cut_size):
                # print(count)
                image_from = Image.open("./pic_gen/cut_size{}.png".format(j))
                # image_from = Image.open("./pic_gen/cut_size{}.bmp".format(j))
                # print("from cut_size{}.bmp".format(j))
                to_image.paste(image_from, (0, h_step * int(count)))
                # print("paste on position {}".format(h_step * count))
                count += 1
            control_size = pic_size - count
            # print(control_size)
            for j in range(control_size):
                # print("note")
                image_from = Image.open("./pic_gen/cut_size{}.png".format(j))
                # image_from = Image.open("./pic_gen/cut_size{}.bmp".format(j))
                # print("from cut_size{}.bmp".format(j))
                to_image.paste(image_from, (0, h_step * int(count)))
                # print("paste on position {}".format(h_step * count))
                count += 1

        to_image.save("./pic_crop/pic{}/img{} {}.m.png".format(k + 1, k + 1, i + 1))
        # to_image.save("./pic_crop/pic{}/img{} {}.bmp".format(k + 1, k + 1, i + 1))
        print("save img{} {}".format(k + 1, i + 1))

        """
        # crop image to right size
        delta_x = 1020
        x = 530
        img = cv2.imread("./pic{}/img{} {}.m.png".format(k + 1, k + 1, i + 1))
        image_crop = img[:, x : x + delta_x]
        cv2.imwrite("./pic{}/img{} {}.m.png".format(k + 1, k + 1, i + 1), image_crop)
        print("save img{} {}".format(k + 1, i + 1))
        """

        # converted image into 8 bits(only for png)
        new = Image.open("./pic_crop/pic{}/img{} {}.m.png".format(k + 1, k + 1, i + 1))
        src = Image.open("./pic_origin/{}.m.png".format(k + 1))
        converted = new.quantize(palette=src)
        converted.save("./pic_crop/pic{}/img{} {}.m.png".format(k + 1, k + 1, i + 1))
        print("succeed convert img{} {}.m.png".format(k + 1, i + 1))
