from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

post = {
    "title" : "Vô đề st",
    "author" : "Acay Nguyen - c4e16",
    "content" : "Bắt đầu học giữa tháng ba. Thời gian học lượng đúng là hay ghê. Lúc mới học thấy ok. Học xong mới biết đánh đề dễ hơn..."
}

db.posts.insert_one(post)
