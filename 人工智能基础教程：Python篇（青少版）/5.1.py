# file=open('E:\GitHub\children-python\人工智能基础教程：Python篇（青少版）\testfile.txt')
file = open('E:/GitHub/children-python/人工智能基础教程：Python篇（青少版）/testfile.txt')
while True:
    line = file.readline()
    if len(line) == 0:
        break
    print(line, end="")
file.close()
# open函数
# 从文件中读取数据
