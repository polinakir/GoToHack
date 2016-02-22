# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:35:05 2016

@author: Dima

"""

### Импортируем все модули ###
import pandas as pd
from ConDb.condb import ConDB 

#from nltk.stem.snowball import RussianStemmer, SnowballStemmer
from nltk.tokenize import RegexpTokenizer
import re
import collections as col
from Pars import Pars

### Все, что нужно такинайзеру и стэмеру ###
pattern = re.compile("[^ ,\!\?:;-]+")
tokenizer = RegexpTokenizer(pattern)


### функции для уменьшения объема кода ###
def stemmer_m(user):
    def process(key):
        token = tokenizer.tokenize(user[key])
        return Pars(token)

    percent = 0
    for key in key_user:
        if key == '_id' or key == 'age':
            continue
        if (user[key] == None) or (user[key] == ""):
            continue
        process(key)
        percent += process(key)
    return int((percent / (len(key_user) - 2)) * 100)


### Получаем людей из базы ###
DB = ConDB()
data = DB.getUsers(1000)

age_count_complete = {age: [] for age in range(14, 19)}
age_count = {age: [] for age in range(14, 19)}

key_user = data[0].keys()

### обрабатываем профили ###
for user in data:
    complete = stemmer_m(user)
    age_count_complete[int(user["age"])].append(complete)
