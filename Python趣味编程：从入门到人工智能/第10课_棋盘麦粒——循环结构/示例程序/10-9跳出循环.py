'''
程序：在双重循环中，用break只能跳出一层循环
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
i = 1
while i <= 3:
    j = 1
    while j <= i:
        print('*', end='')
        break
        j = j + 1
    print()
    i = i + 1
