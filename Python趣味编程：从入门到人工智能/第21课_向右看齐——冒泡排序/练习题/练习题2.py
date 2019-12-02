'''
2.请完善程序，实现对字符串列表按降序排序。
'''
fruits = ['banana', 'grape', 'apple', 'orange', 'pear']
j = 1
while j <= len(fruits) - 1:
    i = len(fruits) - 1
    while i >= j:
        if fruits[i] > fruits[i-1]:
            fruits[i], fruits[i-1] = fruits[i-1], fruits[i]
        i = i - 1
    print(j, fruits)
    j = j + 1
