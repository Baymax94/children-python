# 定义了一个元组，只有一个元素，要加上','
t1=(0,)
t2=(0,'tuple',17.1)
t3=0,'tuple',17.1
t4=('abc',('list','dictionary'))
t5=tuple('spam')

print(t2)
print(t3)
print(t4[1][1])
print(len(t3))
print(t1+t2)
print(t1*3)
print('tuple' in t2)
print(t1.count(0))
print(t3.index(17.1))
print(list(t2))

for x in t3:
    print(t3)
    