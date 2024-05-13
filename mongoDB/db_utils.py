from .mongo_connection import get_mongo_client

client = get_mongo_client()
db = client['urop-database']  # Replace 'your_database_name' with the actual name of your database.

def check_user(username, userAuthority):
    """Check if a user exists in the database."""
    users_collection = db['user-info'] if userAuthority == "student" else db['admin-info']
    return users_collection.find_one({"username": username})

def add_user(username, password, userAuthority):
    """Add a new user to the database."""
    users_collection = db['user-info'] if userAuthority == "student" else db['admin-info']
    result = users_collection.insert_one({"username": username, "password": password})
    return result.inserted_id
