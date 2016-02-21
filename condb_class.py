class ConDB:
    def __init__(self, server='goto.reproducible.work', dbname='vk'):
        from pymongo import MongoClient
        self.c = MongoClient(server)
        self.db = self.c[dbname]
        
    def getAgesDF(self, lim=100, cond={}):
        from datetime import datetime
        from pandas import DataFrame
        users = self.db.users
        ages_dict = {}
        for user in users.find(cond, {"bdate":1, "_id":1}).limit(lim):
            form_bdate = user["bdate"]
            b_date = datetime.strptime(form_bdate, '%d.%m.%Y')
            user_id = user["_id"]
            user_age = int((datetime.today() - b_date).days/365)
            ages_dict[user_id] = user_age
        ages_df = DataFrame.from_dict(ages_dict, orient='index', dtype=None)
        return ages_df

    defaultCond = {'_id': 1, 'bdate': 1, 'interests': 1, 'about': 1, 'music': 1, 'tv': 1, 'books': 1, 'games': 1, 'movies': 1}
    
    def getUsersDF(self, lim=100, cond=defaultCond):
        from datetime import datetime
        from pandas import DataFrame
        users = self.db.users
        users_list = []
        for user in users.find({}, cond).limit(lim):
            try:
                user_interests = user['interests']
            except KeyError:
                user_interests = None

            try:
                user_about = user['about']
            except KeyError:
                user_about = None

            try:
                user_music = user['music']
            except KeyError:
                user_music = None

            try:
                user_tv = user['tv']
            except KeyError:
                user_tv = None

            try:
                user_books = user['books']
            except KeyError:
                user_books = None

            try:
                user_games = user['games']
            except KeyError:
                user_games = None

            try:
                user_movies = user['movies']
            except KeyError:
                user_movies = None
            try:
                user_age = int((datetime.today() - (datetime.strptime(user['bdate'], '%d.%m.%Y'))).days/365)
            except KeyError:
                user_age = None
            user_dict = {'_id': user['_id'], 'interests': user_interests, 'about': user_about, 'music': user_music, 'tv': user_tv, 'books': user_books, 'games': user_games, 'movies': user_movies, 'age': user_age}
            users_list.append(user_dict)
        return users_list