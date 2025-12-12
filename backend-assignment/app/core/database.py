from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class Database:
    client: AsyncIOMotorClient = None

db = Database()

async def connect_to_mongo():
    db.client = AsyncIOMotorClient(settings.MONGO_URL)
    print("✅ Connected to MongoDB")

async def close_mongo_connection():
    if db.client:
        db.client.close()
        print("🛑 Closed MongoDB connection")

def get_master_db():
    """Returns the database responsible for global metadata."""
    return db.client[settings.MASTER_DB_NAME]

def get_tenant_db_collection(collection_name: str):
    """
    Returns a specific collection within the master DB or a separate DB 
    depending on strategy.
    For this assignment (Strategy A: Collection-per-org):
    """
    return db.client[settings.MASTER_DB_NAME][collection_name]