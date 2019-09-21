import matplotlib.pyplot as plt
import matplotlib.image as mpimg

pic = mpimg.imread(
    'E:/GitHub/children-python/人工智能基础教程：Python篇（青少版）/baymax.png')

plt.imshow(pic)
plt.axis('off')
plt.show()

# 读取图片
