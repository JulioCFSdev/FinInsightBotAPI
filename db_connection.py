import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

url = os.environ['MONGO_URL']
client = pymongo.MongoClient(url)

db = client['FinInsightBotAPI']
