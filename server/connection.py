from pymongo import MongoClient

# Connect to the MongoDB instance
client = MongoClient('mongodb+srv://arpanseal1234:Arpan%401234@clusterhar.blgpbui.mongodb.net/?retryWrites=true&w=majority')

# Select the database and collection to store the data
db = client['human_activity']
collection = db['activity_collection']