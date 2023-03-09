from pymongo import MongoClient

import datetime

client = MongoClient('localhost', 27017)

# create a database
db = client['BTTH#02']

# create a collection
collection = db['movies']  # db.createCollection("movies")

# create multi document
movies = [
    {
        "_id": 1,
        "title": "Tom and Jerry",
        "director_id": 34,
        "director_name": "Tim Story",
        "director_birth_date": datetime.datetime.strptime("1970-10-01", "%Y-%m-%d"),
        "release_year": 2019,
        "rating": 3.5,
        "votes": 320,
        "actors": [
            {
                "_id": 1,
                "first_name": "Khoa",
                "last_name": "Ngô",
                "birth_date": datetime.datetime.strptime("2000-10-01", "%Y-%m-%d"),
                "as": "Tom"
            },
            {
                "_id": 2,
                "first_name": "Tuấn",
                "last_name": "Phùng",
                "birth_date": datetime.datetime.strptime("1990-10-01", "%Y-%m-%d"),
                "as": "Jerry"
            }
        ],
        "studio_id": 1,
        "studio_name": "Vietsub",
        "studio_year_founded": datetime.datetime.strptime("1923-10-01", "%Y-%m-%d"),
        "studio_country": "Việt Nam",
        "studio_state": "HCM",
        "studio_city": "Hồ Chí Minh",
        "studio_street": "227 Nguyễn Văn Cừ"
    },
    {
        "_id": 2,
        "title": "Tom and Jerry",
        "director_id": 12,
        "director_name": "Andy Tennant",
        "director_birth_date": datetime.datetime.strptime("1970-10-01", "%Y-%m-%d"),
        "release_year": 2020,
        "rating": 4.5,
        "votes": 120,
        "actors": [
            {
                "_id": 1,
                "first_name": "Khoa",
                "last_name": "Ngô",
                "birth_date": datetime.datetime.strptime("2000-10-01", "%Y-%m-%d"),
                "as": "Tom"
            },
            {
                "_id": 4,
                "first_name": "Huy",
                "last_name": "Dương",
                "birth_date": datetime.datetime.strptime("1990-10-01", "%Y-%m-%d"),
                "as": "Jerry"
            }
        ],
        "studio_id": 4,
        "studio_name": "Engsub",
        "studio_year_founded": datetime.datetime.strptime("1940-10-01", "%Y-%m-%d"),
        "studio_country": "Mỹ",
        "studio_state": "CA",
        "studio_city": "Los Angeles",
        "studio_street": "123 Hollywood"
    },
    {
        "_id": 3,
        "title": "Tây Du Ký",
        "director_id": 40,
        "director_name": "Trần Văn Kiệt",
        "director_birth_date": datetime.datetime.strptime("1970-10-01", "%Y-%m-%d"),
        "release_year": 1996,
        "rating": 5,
        "votes": 1000,
        "actors": [
            {
                "_id": 4,
                "first_name": "Huy",
                "last_name": "Dương",
                "birth_date": datetime.datetime.strptime("1990-10-01", "%Y-%m-%d"),
                "as": "Jerry"
            },
            {
                "_id": 2,
                "first_name": "Tuấn",
                "last_name": "Phùng",
                "birth_date": datetime.datetime.strptime("1990-10-01", "%Y-%m-%d"),
                "as": "Jerry"
            }
        ],
        "studio_id": 1,
        "studio_name": "TayDuKy",
        "studio_year_founded": datetime.datetime.strptime("1923-10-01", "%Y-%m-%d"),
        "studio_country": "Việt Nam",
        "studio_state": "HN",
        "studio_city": "Hà Nội",
        "studio_street": "47 Đường 3/2"
    }
]

# insert multi document
collection.insert_many(movies)
