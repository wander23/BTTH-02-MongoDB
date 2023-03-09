from pymongo import MongoClient

import datetime

client = MongoClient('localhost', 27017)

# create a database
db = client['BTTH#02']

# create a collection
collection = db['restaurants']  # db.createCollection("restaurants")

# create multi document
documents = [
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Bronx",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 82
            },
            {
                "date": datetime.datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "A",
                "score": 17
            }
        ],
        "name": "Villa",
        "restaurant_id": "41704620"
    },
    {
        "address": {
            "street": "3 Avenue",
            "zipcode": "10076",
            "building": "1481",
            "coord": [-73.9557414, 40.7720266]
        },
        "borough": "Sundae",
        "cuisine": "Vietnamese",
        "grades": [
            {
                "date": datetime.datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 94
            },
            {
                "date": datetime.datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 5
            }
        ],
        "name": "Villa2",
        "restaurant_id": "41704621"
    },
    {
        "address": {
            "street": "4 Avenue",
            "zipcode": "10077",
            "building": "1482",
            "coord": [-73.9557415, 40.7720266]
        },
        "borough": "Bronx",
        "cuisine": "American",
        "grades": [
            {
                "date": datetime.datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 100
            },
            {
                "date": datetime.datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "C",
                "score": 1
            }
        ],
        "name": "Villa3",
        "restaurant_id": "41704622"
    }
]

# insert multi document
collection.insert_many(documents)  # db.restaurants.insertMany(document)
