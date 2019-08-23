# 二分法
element=[2,5,8,15,17,19]
val=5
low=0
high=len(element)-1
trace=False
while low<=high:
    mid=(low+high)//2
    if element[mid]==val:
        trace=True
        break
    elif element[mid]>val:
        high=mid-1
    else:
        low=mid+1

if trace:
    print("Find, the index of {0} is {1}".format(val,mid))
else:
    print("No element {0}".format(val))