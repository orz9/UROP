from .mongo_connection import get_mongo_client

client = get_mongo_client()
db = client['urop_user_info']  # Replace 'your_database_name' with the actual name of your database.

def check_user(username):
    """Check if a user exists in the database."""
    users_collection = db.users
    user = users_collection.find_one({"username": username})
    return user

def add_user(username, password):
    """Add a new user to the database."""
    users_collection = db.users
    result = users_collection.insert_one({"username": username, "password": password})
    return result.inserted_id
