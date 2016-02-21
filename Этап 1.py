# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:35:05 2016

@author: Dima
"""
import pymongo
#import json

client = pymongo.MongoClient('goto.reproducible.work')
db = client['vk']
data = db["users"]
user = data.find({'interests': {'$exists': True},
	'about': {'$exists': True},
	'music': {'$exists': True},
      'tv': {'$exists': True},#проверить
	'books': {'$exists': True},
	'games': {'$exists': True},
	'movies': {'$exists': True},
#	"personal": {
#        "alcohol": {'$exists': True},
#        "political": {'$exists': True},
#        "smoking": {'$exists': True}
#	}
 })
#print(json.dumps(user, indent=4, ensure_ascii=False)[:] + '...')
print(user.count())