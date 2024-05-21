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

def add_quiz(question, option1, option2, option3, answer):
    """Add a new quiz question to the database."""
    quiz_collection = db['quiz-data']
    quiz_data = {
        "question": question,
        "option1": option1,
        "option2": option2,
        "option3": option3,
        "answer": answer
    }
    result = quiz_collection.insert_one(quiz_data)
    return result.inserted_id

def add_lesson(lessonName, lessonContent):
    """Add a new lesson to the database"""
    lesson_collection = db['lesson-data']
    lesson_data = {
        "topic": lessonName,
        "content": lessonContent
    }
    result = lesson_collection.insert_one(lesson_data)
    return result.inserted_id