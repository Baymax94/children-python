'''
程序：用break跳出循环
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i = i + 1
