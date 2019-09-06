#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sympy
import matplotlib.pyplot as plt
import numpy as np

# 分解因式 sympy.factor
a, b = sympy.symbols('a b')
f = a**3 - b**3
print(sympy.factor(f))

# 多项式展开 sympy.expand
f1 = (a - b) * (a**2 + a * b - b**2)
print(sympy.expand(f1))

# 多项式通分 sympy.together
x = sympy.Symbol('x')
f2 = (1 + x)**2 / ((1 - x) * (2 - x)) + (1 - x**2) / ((1 - x) * (2 - x))
print(sympy.together(f2))

# 多项式化简 sympy.simplify
f3 = (5 * (a**2) - 3 * b) - 3 * (a**2 - 2 * b)
print(sympy.simplify(f3))

# 阶乘
print(sympy.factorial(100))

# 求方程的根
f4 = x**4 - 8 * (x**3) + 24 * (x**2) - 32 * x + 15
print(sympy.solve(f4, x))

# 绘函数曲线图
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(x), np.sin(x)
plt.title("sin(x) and cos(x)")
plt.plot(x, C)
plt.plot(x, S)
plt.show()

x1 = np.arange(-4, 4, 0.1)
y1 = 2*(x1**2) + 3*x1 + 5
plt.title("一元二次函数")
plt.plot(x1, y1)
plt.show()

# 1.2 人工智能可以为我们做什么
# 1.2.1 符号运算
