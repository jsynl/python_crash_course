# 图片背景透明处理
import PIL.Image as Image

def transparent_back(img):
    img = img.convert('RGBA')  # 图片转换为四通道。第四个通道就是我们要修改的透明度。返回新的对象
    L, H = img.size  # 图片尺寸
    print('图片尺寸: ', (L, H))
    color_0 = img.getpixel((0,0))  # 返回图片某个坐标点颜色
    print('color_0: ', color_0)
    for h in range(H):
        for l in range(L):
            dot = (l, h)
            color_1 = img.getpixel(dot)  # 获取坐标 dot 点颜色
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)  # 取 color_1 前三个通道值，将第四个变为 0
                # print('color_1: ', color_1)
                img.putpixel(dot, color_1)  # 修改坐标处颜色，没有返回值，直接修改 img
    return img


if __name__ == '__main__':
    
    img=Image.open(r'C:\Users\jsynl\MyProjects\python_crash_course_alien\images\ship.bmp')
    img=transparent_back(img)
    img.save(r'C:\Users\jsynl\Desktop\ship_r.bmp')