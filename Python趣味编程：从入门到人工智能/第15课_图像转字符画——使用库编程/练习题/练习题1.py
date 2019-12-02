from PIL import Image, ImageFilter
img = Image.open('hellokitty.jpg')
#img = img.filter(ImageFilter.GaussianBlur)#高斯模糊
#img = img.filter(ImageFilter.BLUR)#普通模糊
#img = img.filter(ImageFilter.EDGE_ENHANCE)#边缘增强
#img = img.filter(ImageFilter.FIND_EDGES)#找到边缘#
img = img.filter(ImageFilter.EMBOSS)#浮雕*
#img = img.filter(ImageFilter.CONTOUR)#轮廓*
#img = img.filter(ImageFilter.SHARPEN)#锐化
#img = img.filter(ImageFilter.SMOOTH)#平滑
#img = img.filter(ImageFilter.DETAIL)#细节
img.show()
