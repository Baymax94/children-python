'''
3.请完善程序，使用二分查找算法从字符串列表中查找banana所在位置。
'''
target = 'banana'   #查找目标是banana
fruits = ['pear', 'orange', 'grape', 'banana', 'apple']
left, right = 0, len(fruits) - 1
while left <= right:
    mid = (right - left) // 2 + left
    if target == fruits[mid]:
        print(mid)
        break
    elif target < fruits[mid]:
        left = mid + 1
    else:
        right = mid - 1
else:
    print('找不到')
