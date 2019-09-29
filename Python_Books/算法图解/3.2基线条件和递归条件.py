# 基线条件和递归条件
def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i-1)


print(countdown(10))
