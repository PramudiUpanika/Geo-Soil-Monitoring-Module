import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Try loading from current dir, then parent
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/geo_soil_db")

client = AsyncIOMotorClient(MONGO_URI)
db = client.get_database("test")
