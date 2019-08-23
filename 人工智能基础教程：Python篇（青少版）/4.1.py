# 分类加法计数原理
# 声明list是一个列表，使用“[]”表示一个空的列表并赋值给list
list=[]

for i in range(3):
    list.append("Airplane_{0}".format(i+1))

for i in range(4):
    list.append("Train_{0}".format(i+1))

print("The number of the way from Beijing to Shanghai is:{0}".format(len(list)))

for i in list:
    print(i)