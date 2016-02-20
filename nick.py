# -*- coding: cp1251 -*-
from pymongo import MongoClient
import json

c = MongoClient('goto.reproducible.work')
print(c.database_names())

vk = c.vk
print(vk.collection_names())

users = vk.users
query = users.find_one()
print(query)