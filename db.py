
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
import pytz

uri = "mongodb+srv://root:root@cluster0.erzx9gg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

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


    data =  [['Trending in India', '#NEET_परीक्षा_परिणाम', '194K posts'], ['Politics · Trending', '#PrimeMinister', '25.6K posts'], ['Trending in India', '#MissYou', '1,283 posts']] 
    datatoupload = {
    "Date-Time": str(current_time.day) + "-" + str(current_time.month) + "-" + str(current_time.year) + " " + str(current_time.hour) + ":" + str(current_time.minute),
    "Trends": []
    }
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


    