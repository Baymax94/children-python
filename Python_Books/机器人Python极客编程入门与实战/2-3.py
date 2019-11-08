# -*- coding:utf-8 -*-
import numpy as np
import scipy as sp
import pandas as pd
import pip
# pip V10.0.0以上版本需要导入下面的包
from pip._internal.utils.misc import get_installed_distributions

x10 = pip._internal.get_installed_distributions()
df = pd.DataFrame()
df['name'] = x10
print(df.head())
df.to_csv('F:/GitHub/children-python/Python_Books/机器人Python极客编程入门与实战/m10.csv',index=False)