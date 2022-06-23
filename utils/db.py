import motor.motor_asyncio
import pymongo.errors


class Database:

    client = None
    db = None

    @staticmethod
    async def initialize(db_url, db_name):
        Database.client = motor.motor_asyncio.AsyncIOMotorClient(db_url)
        Database.db = Database.client[db_name]
        try:
            await Database.db.command("ping")
        except pymongo.errors.ServerSelectionTimeoutError:
            print("Can't connect to MongoDB. Exiting.", flush=True)
            return False
        else:
            print("Connected successfully to MongoDB.", flush=True)
            return True
