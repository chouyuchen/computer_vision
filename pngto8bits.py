from PIL import Image

for i in range(140):
    new = Image.open("./pic1/img{}.m.png".format(i + 1))
    src = Image.open("./pic_origin/1.m.png")
    converted = new.quantize(palette=src)
    converted.save("./pic1/img{}.m.png".format(i + 1))
    print("succeed {} image".format(i + 1))
