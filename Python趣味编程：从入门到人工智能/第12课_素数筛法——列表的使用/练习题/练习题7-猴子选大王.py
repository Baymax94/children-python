'''
程序：猴子选大王
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
提示：又叫约瑟夫环、约瑟夫斯问题等。
'''
queue = [n for n in range(1, 42)]
i = 1
while len(queue) > 1:
    n = queue.pop(0)
    if i % 3 > 0:
        queue.append(n)
    i += 1
print(queue)
