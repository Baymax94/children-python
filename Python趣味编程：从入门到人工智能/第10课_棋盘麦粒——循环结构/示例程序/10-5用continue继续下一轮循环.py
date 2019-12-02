'''
程序：用continue继续下一轮循环
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
i = 0
while i < 10:
    i = i + 1
    if i % 2 == 0:
        continue
    print(i)
