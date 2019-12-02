'''
程序：图像转字符画
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
#导入Pillow库中的Image类
from PIL import Image

#主程序
def main():
    #打开图片、调整图片尺寸、转换为灰度图像
    img_name = 'hellokitty.jpg'
    width, height = 80, 48
    img = Image.open(img_name).resize((width, height)).convert('L')
    
    #将图片每个像素的灰度值转换为一个字符
    text = ''
    for y in range(height):
        for x in range(width):
            text += getchar(img.getpixel((x, y)))
        text += '\n'
        
    #将字符画保存到一个文本文件中
    fo = open('hellokitty.txt', 'w')
    fo.write(text)
    fo.close()

#将灰度值转换为字符
#ascii_chars = list('MNHQ$OC?7>!:-;. ')
def getchar(gray):
    #unit = 256 / len(ascii_chars)
    #return ascii_chars[int(gray // unit)]
    return '@' if gray < 128 else ' '


#程序入口
if __name__ == '__main__':
    main()
