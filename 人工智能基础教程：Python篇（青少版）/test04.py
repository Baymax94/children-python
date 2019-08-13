# 分数
from fractions import Fraction
f = Fraction(1,2)
print("print Fraction(1,2): {0}".format(f))
f = Fraction(2.5)
print("print Fraction(2.5): {0}".format(f))
f = Fraction("2.5")
print("print Fraction('2.5'): {0}".format(f))
f = Fraction(122,368)
print("print Fraction(122,368): {0}".format(f))

# 复数
# j 定义复数的虚部
a = 2 + 3j
b = complex(4,9)
print(type(a))
print(type(b))
print(a+b)
print(a-b)
print(a*b)
print(a/b)