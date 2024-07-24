
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
import pytz

uri = "mongodb+srv://user:pass@clusterid.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server

# Send a ping to confirm a successful connection





def main(data):

    client = MongoClient(uri, server_api=ServerApi('1'))

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    database = client["x-flask"]
    collection = database["topthings"]

    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    for i in data:
        temp = {
            "Topic": i[0],
            "Name": i[1],
            "Posts": i[2].split(' ')[0]
        }
        datatoupload['Trends'].append(temp)

    collection.insert_one({"trend": datatoupload})



def retrieve():
    client = MongoClient(uri, server_api=ServerApi('1'))



    database = client["x-flask"]
    collection = database["topthings"]

    return collection.find()


    
