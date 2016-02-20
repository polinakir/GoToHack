# -*- coding: cp1251 -*-
from pymongo import MongoClient
import json
from datetime import datetime

# -- Получение возраста --

c = MongoClient('goto.reproducible.work')
print(c.database_names())

vk = c.vk
print(vk.collection_names())

users = vk.users

q = users.find({},{"bdate":1})

i=0
while i < 15:
	obj = q.next()
	form_bdate = obj["bdate"]
	b_date = datetime.strptime(form_bdate, '%d.%m.%Y')
	print "Age : %d" % ((datetime.today() - b_date).days/365)
	i += 1

# -- Получение возраста --

#uQuery = users.find({ }, { bdate: 1, id: 1 })

#print(json.dumps(uQuery, sort_keys=True, indent=4))

walls = vk.walls
query = walls.find_one()

#print(json.dumps(query, sort_keys=True, indent=4))