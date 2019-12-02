'''
程序：输出九九乘法表
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(j, 'x', i, '=', i * j, end='  ')
        j += 1
    print()
    i += 1
