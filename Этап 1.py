# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:35:05 2016

@author: Dima
"""
import pymongo
client = pymongo.MongoClient('goto.reproducible.work')
db = client['vk']
data = db["users"]
user = data.find({'interests': {'$exists': True}})
#import json
#print(json.dumps(user, indent=4, ensure_ascii=False)[:] + '...')
print(user.count())