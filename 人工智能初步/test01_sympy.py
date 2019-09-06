#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sympy
# 虚数单位i
print(sympy.I)
print(sympy.I**2)
print(sympy.sqrt(-1))
# 自然对数的底E
print(sympy.E)
print(sympy.log(sympy.E))
# 无穷大oo
print(1 / sympy.oo)
print(1 + sympy.oo)
# 圆周率pi
print(sympy.pi)
print(sympy.sin(sympy.pi / 2))
# 初等运算
# 求对数
print(sympy.log(sympy.E**3))
print(sympy.log(1000, 10))
# 求平方根
print(sympy.sqrt(4))
# 求n次方根
print(sympy.root(8, 3))
# 求k次方
print(2**3)
print(16**(1 / 2))
# 求阶乘
print(sympy.factorial(4))
# 求三角函数
print(sympy.cos(sympy.pi / 2))

# 表达式与表达式求值
# 首先定义x为一个符号，表示一个变量
x = sympy.Symbol('x')
fx = 2 * x + 1
# 可以看到fx是一个sympy.core.add.Add类型的对象，也就是一个表达式
print(type(fx))
# 用evalf函数，传入变量的值，对表达式进行求值
print(fx.evalf(subs={x: 2}))

# 多元表达式
x, y = sympy.symbols('x y')
f = 2 * x + y
print(f.evalf(subs={x: 2, y: 2}))
print(f.evalf(subs={x: 1}))

# 解方程
x = sympy.Symbol('x')
print(sympy.solve(x - 1, x))
print(sympy.solve(x**2 - 1, x))
print(sympy.solve(x**2 + 1, x))
f = x**2 + 1
print(sympy.solve(f, x))

# 解方程组
# 如：x+y=1;x-y=3
x, y = sympy.symbols('x y')
print(sympy.solve([x + y - 1, x - y - 3], [x, y]))

# 计算求和式 sympy.summation
# 如：n=1~100；2n求和
n = sympy.Symbol('n')
print(sympy.summation(2 * n, (n, 1, 100)))

# 解带有求和式的方程
# 如：x=1~5;x求和，求解“和”+10x=15
x = sympy.Symbol('x')
i = sympy.Symbol('i', integer=True)
f = sympy.summation(x, (i, 1, 5)) + 10 * x - 15
print(sympy.solve(f, x))

# 求极限 sympy.limit
x = sympy.Symbol('x')
f1 = sympy.sin(x) / x
print(sympy.limit(f1, x, 0))

f2 = (1 + x)**(1 / x)
print(sympy.limit(f2, x, 0))

f3 = (1 + 1 / x)**x
print(sympy.limit(f3, x, sympy.oo))

# 求导 sympy.diff
x = sympy.Symbol('x')
f = x**2 + 2 * x + 1
print(sympy.diff(f, x))

f2 = sympy.sin(x)
print(sympy.diff(f2, x))

f3 = x**2 + 2 * x + y**3
print(sympy.diff(f3, x))
print(sympy.diff(f3, y))

# 求定积分 sympy.integrate
x = sympy.Symbol('x')
f = 2 * x
# 传入函数表达式和积分变量、积分下限、上限
print(sympy.integrate(f, (x, 0, 1)))

# 多重积分
t, x = sympy.symbols('t x')
f = 2 * t
g = sympy.integrate(f, (t, 0, x))
print(sympy.integrate(g, (x, 0, 3)))

# 求不定积分 sympy.integrate
x = sympy.Symbol('x')
f = sympy.E**x + 2 * x
print(sympy.integrate(f, x))

# 1.2 人工智能可以为我们做什么
# 1.2.1 符号运算
