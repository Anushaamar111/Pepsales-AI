import motor.motor_asyncio
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

username = quote_plus(os.getenv("DB_USERNAME"))
password = quote_plus(os.getenv("DB_PASSWORD"))

MONGO_URI = f"mongodb+srv://{username}:{password}@cluster0.3v4eigz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client.notification_db  
notifications_collection = db.notifications
