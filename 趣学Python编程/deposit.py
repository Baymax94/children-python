print("欢迎来到财富测试")
deposit = int(input("请输入您的零花钱："))
if deposit >= 100 and deposit <= 500:
    print("还可以")
elif deposit > 500 and deposit <= 1000:
    print("相当可以")
elif deposit > 1000 and deposit <= 5000:
    print("哇！你真的很有钱")
else:
    print("送你一个微笑")