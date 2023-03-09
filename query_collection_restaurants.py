from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['BTTH#02']

collection = db['restaurants']

if __name__ == '__main__':
    while True:
        print('''
        1. Cho biết tất cả documents trong collection restaurants
        2. Cho biết restaurant_id, name, borough và cuisine của tất cả document trong restaurants
        3. Cho biết restaurant_id, name, borough và zip code của tất cả document trong restaurants.
        4. Cho biết restaurant có borough = Bronx
        5. Cho biết restaurants có score trong khoản 80 đến 100
        6. cho biết restaurant có vĩ độ nhỏ hơn -60.754168 và có score lớn hơn 70
        7. Cho biết restaurants có điểm A
        ''')
        choice = input('nhập yêu cầu: ')
        if choice == '1':
            # db.restaurants.find()
            for i in collection.find():
                print(i)
        elif choice == '2':
            # db.restaurants.find({}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1})
            for i in collection.find({}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1}):
                print(i)
        elif choice == '3':
            # db.restaurants.find({}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'address.zipcode': 1})
            for i in collection.find({}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'address.zipcode': 1}):
                print(i)
        elif choice == '4':
            # db.restaurants.find({'borough': 'Bronx'})
            for i in collection.find({'borough': 'Bronx'}):
                print(i)
        elif choice == '5':
            # db.restaurants.find({'grades.score': {'$gte': 80, '$lte': 100}})
            for i in collection.find({'grades.score': {'$gte': 80, '$lte': 100}}):
                print(i)
        elif choice == '6':
            # db.restaurants.find({'address.coord': {'$lt': -60.754168}, 'grades.score': {'$gt': 70}})
            for i in collection.find({'address.coord': {'$lt': -60.754168}, 'grades.score': {'$gt': 70}}):
                print(i)
        elif choice == '7':
            # db.restaurants.find({'grades.grade': 'A'})
            for i in collection.find({'grades.grade': 'A'}):
                print(i)
        elif choice == '0':
            break
        else:
            print('Invalid choice')