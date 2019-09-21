poem = '''Beautiful is better than ugly.
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
...
'''

file = open(
    "E:/GitHub/children-python/人工智能基础教程：Python篇（青少版）/testWriteFile.txt", "w")
file.write(poem)
file.close()
# 写数据到文件
