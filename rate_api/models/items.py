import pymongo
mongo_pass = 'wgrAmKyE8e9NpUN2'
client = pymongo.MongoClient("mongodb+srv://ivovivanov:{}@ivomongo.55lz8zm.mongodb.net/?retryWrites=true&w=majority".format(mongo_pass))
db = client.rate_api
items_collection = db.items

#changed = items_collection.find_one_and_update({'item_id': 8}, {'$set': {'item_id': 123}})

def get_items():
    cursor = items_collection.find()
    item_list = list()
    for record in cursor:
        item_list.append({'id': record.get('item_id'), 'name': record.get('item_name')})
    return item_list

if __name__ == '__main__':
    print(get_items())