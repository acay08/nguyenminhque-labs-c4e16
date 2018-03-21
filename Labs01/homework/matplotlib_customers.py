from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

number_of_events = db.customers.find({"ref" : "events"}).count()
number_of_ads = db.customers.find({"ref" : "ads"}).count()
number_of_wom = db.customers.find({"ref" : "wom"}).count()

print("total Events's customers: ",number_of_events)
print("total advertisements's customers: ", number_of_ads)
print("total wom's customers: ", number_of_wom)

total = number_of_ads + number_of_wom + number_of_events
print('Total customers by Refs: ',total)

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot

labels = ['Event', 'Advertisements', 'Word of mouth']
values = [number_of_events/total*100, number_of_ads/total*100, number_of_wom/total*100]
colors = ['red', 'green', 'gold']
explode = [0, 0, 0]

#2. plot
pyplot.pie(values, labels=labels, colors = colors, explode=explode, shadow = True, autopct='%1.0f%%')

pyplot.axis('equal')
#3. Show
pyplot.show()
