# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:35:05 2016

@author: Dima

"""

import pandas as pd
from ConDb.condb import ConDB 
import matplotlib.pyplot as plt
from nltk.stem.snowball import RussianStemmer, SnowballStemmer
from nltk.tokenize import RegexpTokenizer
import re
import collections as col
from Pars import Pars
englich_stemmer = SnowballStemmer("english")
russian_stemmer = RussianStemmer()


def stemmer_m(user):
    def process(key):
        token = tokenizer.tokenize(user[key])
        stem_tok = []                
        for t in token: 
            stem_tok.append(englich_stemmer.stem(t))
            stem_tok.append(russian_stemmer.stem(t))
        return 1

    percent = 0
    for key in key_user:
        if (user[key] == None) or (user[key] == ""):
            pass
        else:
            try:
                int(user[key])
                percent += 1
            except TypeError:
                process(key)
                Pars(user[key])
                percent += 1
            except ValueError:
                process(key)
                Pars(user[key])
                percent += 1
    return int((percent/len(key_user))*100)
    
#data = [{'age': 15, 'c': 'Yes', 'm': 3}, {'age': 15, 'c': 'Yes', 'm': ''}, {'age': 18, 'c': 'Yes', 'm': 3}, {'age': 16, 'c': None, 'm': 3}]
pattern = re.compile("[^ ,\.\!\?\:]+")
tokenizer = RegexpTokenizer(pattern)
DB = ConDB()

data = DB.getUsers(1000)

age_count_complete = {age: [] for age in range(14, 19)}
age_count = {age: [] for age in range(14, 19)}

key_user = data[0].keys()

for user in data:
    complete = stemmer_m(user)
    age_count_complete[int(user["age"])].append(complete)
    #age_count[int(user["age"])].append(
df = pd.DataFrame()
df1 = pd.Series(age_count_complete)
#df2 = pd.Series(age_count).to_frame()
df.insert(0, "Full completed",df1)

#df.insert(1, "Total",df2)

#c = []
#for i in range(14, 19):
#    c.append((df["Full completed"][i] * 1.0 /df["Total"][i])*100)
#df.insert(2, "Percent", c)
c = col.Counter()
for word in df["Full completed"][14]:
     c[word] += 1
df_new = pd.DataFrame(list(c.items()), columns=["val","count"])
plt.xlabel("Percent")
plt.ylabel("Count")
df_new = df_new.sort_values('val')
print(df_new)

plt.plot(df_new['val'], df_new['count'], color='blue')
#plt.plot(df.index, df["Total"], color='blue')
#plt.plot(df.index, df["Full completed"], color='red')
#plt.plot(df.index, df["Percent"], color='red')

#plt.legend(loc="upper left")

#print(user.count(), data.count())