class ConDB:
    def __init__(self, server='goto.reproducible.work', dbname='vk'):
        from pymongo import MongoClient
        # В доработке
        self.c = MongoClient(server)
        self.db = self.c[dbname]
        
    def getUsersDF(self, lim=100):
        from datetime import datetime
        users = self.db.users
        for user in users.find({}, {"bdate":1, "_id":1}).limit(100):
            form_bdate = user["bdate"]
            b_date = datetime.strptime(form_bdate, '%d.%m.%Y')
            # user["_id"] - айди пользователя
            # int((datetime.today() - b_date).days/365) - возраст пользователя