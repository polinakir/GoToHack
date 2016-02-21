# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:35:05 2016

@author: Dima
"""

import pandas as pd
data = [{'age': 15, 'c': 'Yes', 'm': 3}, {'age': 15, 'c': 'Yes', 'm': ''}, {'age': 18, 'c': 'Yes', 'm': 3}, {'age': 16, 'c': None, 'm': 3}]
age_count_compile = {age: 0 for age in range(14, 19)}
age_count = {age: 0 for age in range(14, 19)}
key_user = data[0].keys()
for user in data:
    complite = False
    for key in key_user:
        if (user[key] != None) or (user[key] != ""):
            complite = True
        else:
            complite = False
            break
    if complite:
        age_count_compile[int(user["age"])] += 1
    age_count[int(user["age"])] += 1
df1 = pd.Series(age_count_compile).to_frame()
df2 = pd.Series(age_count).to_frame()
print(df1)
#df = df2.merge(df1, 'left')
#print(user.count(), data.count())