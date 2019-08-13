# 简单的计算器
# 整数运算
x = int(input("please input the first operand:"))
y = int(input("please input the second operand:"))
character = input("please input the instraction character:")
if character == "+":
    result = x+y
elif character == "-":
    result = x-y
elif character == "*":
    result = x*y
elif character == "/":
    result = x/y
else:
    print("wrong")
    exit()
print("the result is: ",result)
print("测试 the result is:{0}".format(result))