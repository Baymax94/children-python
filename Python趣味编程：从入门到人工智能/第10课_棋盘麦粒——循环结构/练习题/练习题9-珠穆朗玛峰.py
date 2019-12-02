'''
程序：珠穆朗玛峰
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
h = 8848 * 100 * 10
n = 0.5
t = 0
while True:
    n = n * 2
    t += 1
    if n >= h:
        break
print(t)
