# !/usr/bin/env python3
# -*- coding: utf-8 -*-
def isprime(n):
    """
    本函数判读n是否是质数
    如果n是质数，那么返回True
    否则返回False
    """
    for x in range(2,1+n//2):
        if n//x == n/x:
            return False
    return True

def iscomposite(n):
    """
    本函数判读n是否是合数
    如果n是合数，那么返回True
    否则返回False
    """
    for x in range(2,1+n//2):
        if n//x == n/x:
            return True
    return False

print("\n以下是100以为的质数：")
for x in range(2,100):
    if isprime(x):
        print(x,end=' ')

print("\n以下是100以为的合数：")
for x in range(2,100):
    if iscomposite(x):
        print(x,end=' ')

# python简单算法定义函数判断的质数和合数
