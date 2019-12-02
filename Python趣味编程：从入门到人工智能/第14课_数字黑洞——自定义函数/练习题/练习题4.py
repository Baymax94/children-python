'''
4.请完善程序，使用递归方式计算1~100的各数之和。
'''
def add(n):
    if n > 1:
        return add(n-1) + n
    else:
        return 1
        
s = add(100)
print(s)
