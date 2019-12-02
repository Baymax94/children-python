'''
2.请完善程序，实现对字符串列表按降序排序。
'''
fruits = ['banana', 'grape', 'apple', 'orange', 'pear']
j = 0
while j < len(fruits) - 1:
    p = j
    i = j + 1
    while i < len(fruits):
        if fruits[i] > fruits[p]:
            p = i
        i = i + 1
    if p != j:
        fruits[j], fruits[p] = fruits[p], fruits[j]
    print(j+1, fruits)
    j = j + 1
