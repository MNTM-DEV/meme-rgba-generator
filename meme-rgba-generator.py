import sys
from PIL import Image


def get_generated_scale(size1, size2):
    h = max(size1[1], size2[1])
    w = int(size1[0]/size1[1]*h)
    return (w, h)


def reposition_img(img, scale, bg):
    ret = Image.new("RGB", scale, bg)
    rate_src = img.size[0]/img.size[1]
    rate_dst = scale[0]/scale[1]
    if(rate_src > rate_dst):
        gen_h = int(scale[0]/rate_src)
        ret.paste(img.resize((scale[0], gen_h)), (0, int((scale[1]-gen_h)/2)))
    else:
        gen_w = int(scale[1]*rate_src)
        ret.paste(img.resize((gen_w, scale[1])), (int((scale[0]-gen_w)/2), 0))
    return ret


def generate_png_matrix(img1, img2, scale):
    resize_img1 = reposition_img(img1, scale, "#FFFFFF")
    resize_img2 = reposition_img(img2, scale, "#000000")
    return (resize_img1, resize_img2)


def generate_img(imgs):
    img1 = imgs[0]
    img2 = imgs[1]
    img3 = Image.new("RGBA", img1.size)
    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            r1 = img1.getpixel((i, j))[0]
            r2 = img2.getpixel((i, j))[0]

            r1 = int(128+r1/2)
            r2 = int(r2/2)

            a = 255-r1+r2
            r = 0
            if(a != 0):
                r = int(255*r2/float(a))
            p3 = (r, r, r, a)
            img3.putpixel((i, j), p3)
    return img3


def process(path1, path2, path3):
    img1 = Image.open(path1).convert('L')
    img2 = Image.open(path2).convert('L')
    scale = get_generated_scale(img1.size, img2.size)
    imgs = generate_png_matrix(img1, img2, scale)
    img3 = generate_img(imgs)
    img3.save(path3)


def main():
    print("ATTENTION:查看命令行方式的使用帮助请使用 " + sys.argv[0] + " help")
    path1 = input('白色背景显示的图片的路径：')
    path2 = input('黑色背景显示的图片的路径：')
    path3 = input('透明图存放路径:')
    process(path1, path2, path3)


def cmd_help():
    print("制作隐藏的GHS图片/表情包的工具。")
    print(sys.argv[0] + " path1 path2 path3")
    print("path1\t白色背景显示的图片的路径")
    print("path2\t黑色背景显示的图片的路径")
    print("path3\t透明图存放路径")


if __name__ == "__main__":
    arg_count = len(sys.argv)
    if(arg_count == 1):
        main()
    elif(arg_count == 4):
        process(sys.argv[1], sys.argv[2], sys.argv[3])
    elif(arg_count == 2 and sys.argv[1] == 'help'):
        cmd_help()
    else:
        print("命令参数不合法！")
        cmd_help()
