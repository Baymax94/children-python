'''
程序：素数筛法
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
#输入筛选的上界
n = int(input('请输入一个自然数:'))

#生成数表
a = list(range(2, n + 1))

#筛选素数
i = 0
while i < len(a):
    j = i + 1
    while j < len(a):
        if a[j] % a[i] == 0:
            a.pop(j)
        else:
            j = j + 1 
    i = i + 1

#输出素数
print('在自然数2~%d之间找到%d个素数。列表如下：' % (n, len(a)))
print(a)
