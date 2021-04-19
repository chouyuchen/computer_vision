from cv2 import cv2
import numpy as np
from PIL import Image

image = cv2.imread("resize.m.png")
h = image.shape[0]
w = image.shape[1]
print("hight,width: {}, {}".format(h, w))

"""
# 先把圖片補成1400
to_image = Image.new("RGB", (w, 1400))
sub = 1400 - h
image_cut = image[0:sub, :, :]
cv2.imwrite("sub.m.png", image_cut)
to_image.paste(Image.open("1.m.png"), (0, 0))
to_image.paste(Image.open("sub.m.png"), (0, h))
to_image.save("resize.m.png")
"""


# cut
image_list = []
cut_size = 140
h_step = int(1400 / cut_size)  # 切割的每隔為step=1400/140

for i in range(cut_size):
    image_cut = image[h_step * int(i) : h_step * int(i + 1), :, :]
    print(h_step * int(i), h_step * int(i + 1))
    image_list.append(image_cut)
    cv2.imwrite("./pic_gen/cut_size{}.m.png".format(i), image_cut)
    print("save cut_size{}".format(i))

# print(len(image_list))

# compose
# 循環貼上，把照片按順序黏貼到對應位置上
# start_index=i
for i in range(cut_size):
    # 創一新圖片
    to_image = Image.new("RGB", (w, 1400))
    count = 0
    # paste image:
    for j in range(i, cut_size):
        # print(count)
        image_from = Image.open("./pic_gen/cut_size{}.m.png".format(count))
        to_image.paste(image_from, (0, h_step * int(j)))
        count += 1
    # print("from start:")
    for j in range(i):
        # print(count)
        image_from = Image.open("./pic_gen/cut_size{}.m.png".format(count))
        to_image.paste(image_from, (0, h_step * int(j)))
        count += 1

    to_image.save("./finish/img{}.m.png".format(i + 1))
    print("save img{}".format(i + 1))
