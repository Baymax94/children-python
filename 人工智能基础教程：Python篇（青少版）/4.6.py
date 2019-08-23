# 冒泡排序
element=[17,5,19,8,15]

for i in range(len(element)):
    for j in range(i+1):
        if element[i]<element[j]:
            element[i],element[j]=element[j],element[i]

print(element)