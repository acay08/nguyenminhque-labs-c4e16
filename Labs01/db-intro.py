from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds117749.mlab.com:17749/c4e16-acay"
#1. connect to database
client = MongoClient(mongo_uri)

#2. Get database
db = client.get_default_database()

#3. create collection
games = db['games']
blogs = db['blogs']
dicts = db['dicts']
inventory = db['inventory']
#4. create a new document
new_game = {
    "name" : "Dao Vang",
    "description" : "gold dig"
}

blog = {
    "name" : "acay",
    "nickname" : "acay08"
}

dict = {
    "lv" : "vai lua",
    "tg" : "thoi gian",
    "ht" : "hoc tap",
    "cdmm" : "canh dong menh mong"
}

invent = {
    "gold" : 500,
    "pouch" : ["flint", "twine", "gemstone"],
    "backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"]
}

#5. insert document into collection
# games.insert_one(new_game)
# blogs.insert_one(blog)
# dicts.insert_one(dict)
# inventory.insert_one(invent)

#6. read
all_game = games.find()

for game in all_game:
    print(game['name'])
