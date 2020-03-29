#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from functools import reduce
import _datetime
import time
import numpy as nm
import pandas as pd


my_data = [100, 200, 300, 400]
index1 = ['China', 'USA', 'Japan', 'Korea']
a = pd.Series(my_data, index1)
b = a.filter(a.keys() == 'USA')

c = pd.Series(my_data)


dat1 = pd.date_range('20190101', periods=6)
d = pd.DataFrame(nm.random.rand(6, 4), dat1, index1)
dd = d.sort_values(by='China')
print(dd)
t = d.iloc[0]
print(t)
dd.iloc[1,1] =1
dd.iloc[3,1] = 1

dd = dd.append(t, ignore_index=False)
print(dd)
print(dd[dd.China > 0.5])
print(dd[dd > 0.5])
dd[dd>0.8] = 0
print(dd)
print(dd[dd['China'].isin([0, 0.6])])
