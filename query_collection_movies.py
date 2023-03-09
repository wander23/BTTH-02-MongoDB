from pymongo import MongoClient

import datetime

client = MongoClient('localhost', 27017)

# create a database
db = client['BTTH#02']

# create a collection
collection = db['movies']

if __name__ == "main":
    while True:
        print('''
            1. Cho biết các movies có title là “Tom and Jerry”
            2. Cho biết các movies có rating lớn hơn 3.0 và nhỏ hơn 5.0
            3. Cho biết các movies có diễn viên họ “Ngô”
            4. Cho biết các movies được sản xuất ở “Mỹ” và có hơn 10 người vote
            5. Cho biết các movies có diễn viên sinh năm 2000 hoặc có năm phát hành trước 2020
        ''')
        choice = input('nhập yêu cầu: ')
        if choice == '1':
            # 1. Cho biết các movies có title là “Tom and Jerry”
            # db.movies.find({'title': 'Tom and Jerry'})
            for i in collection.find({'title': 'Tom and Jerry'}):
                print(i)
        elif choice == '2':
            # 2. Cho biết các movies có rating lớn hơn 3.0 và nhỏ hơn 5.0
            # db.movies.find({'rating': {'$gt': 3.0, '$lt': 5.0}})
            for i in collection.find({'rating': {'$gt': 3.0, '$lt': 5.0}}):
                print(i)
        elif choice == '3':
            # 3. Cho biết các movies có diễn viên họ “Ngô”
            # db.movies.find({'actors.last_name': 'Ngô'})
            for i in collection.find({'actors.last_name': 'Ngô'}):
                print(i)
        elif choice == '4':
            # 4. Cho biết các movies được sản xuất ở “Mỹ” và có hơn 10 người vote
            # db.movies.find({'studio_country': 'Mỹ', 'votes': {'$gt': 10}})
            for i in collection.find({'studio_country': 'Mỹ', 'votes': {'$gt': 10}}):
                print(i)
        elif choice == '5':
            # 5. Cho biết các movies có diễn viên sinh năm 2000 hoặc có năm phát hành trước 2020
            # {$or: [
            #       { release_year: { $lt: 2020 }},
            #       { 'actors.birth_date':
            #           { $gte: ISODate('2000-01-01'),
            #             $lte: ISODate('2000-12-31')} }]}}
            for i in collection.find(
                    {'$or': [{'release_year': {'$lt': 2020}},
                             {'actors.birth_date': {
                                 '$gte': datetime.datetime(2000, 1, 1),
                                 '$lte': datetime.datetime(2000, 12, 31)}}]}):
                print(i)
        elif choice == '0':
            break
