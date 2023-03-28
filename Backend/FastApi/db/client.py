# pip install pymongo
from pymongo import MongoClient
from dotenv import load_dotenv 
from os import environ
load_dotenv()
#Base de datos Local
#db_client = MongoClient().local
#Base de datos remota
db_client = MongoClient(environ.get("URL_MONGO")).test


