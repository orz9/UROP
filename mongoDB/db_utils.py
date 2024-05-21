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

def add_quiz(topic, question, option1, option2, option3, answer):
    """Add a new quiz question to the database."""
    quiz_collection = db['quiz-data']
    quiz_data = {
        "topic": topic,
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

def check_lesson(lessonName):
    """Check if a lesson with the given name already exists in the database"""
    existing_lesson = db['lesson-data'].find_one({'topic': lessonName})
    return existing_lesson is not None

def get_lessons():
    lessons = db['lesson-data'].find({}, {'_id': 0, 'topic': 1})
    return list(lessons)

def get_lesson_content(topic):
    """Fetch the content of a lesson based on the topic."""
    lesson = db['lesson-data'].find_one({'topic': topic}, {'_id': 0, 'content': 1})
    if lesson:
        return lesson.get('content', 'No content available.')
    return 'No lesson found for the selected topic.'

def get_quiz_questions(topic):
    return list(db['quiz-data'].find({'topic': topic}, {'_id': 0}))

def update_student_performance(username, lesson, score, total):
    student_performance = db['student-performance']
    score_entry = f"{score}/{total}"

    # Create a new document if it does not exist
    update_result = student_performance.update_one(
        {'student_name': username},
        {
            '$push': {f'lessons.{lesson}': score_entry}
        },
        upsert=True  # This option creates a new document if no document matches the query
    )

    # Check if the operation was successful or if a new document was created
    if update_result.upserted_id is not None:
        print("Created a new student performance record.")
    elif update_result.modified_count == 0:
        # If the document exists but the lesson does not, initialize it
        update_result = student_performance.update_one(
            {'student_name': username, f'lessons.{lesson}': {'$exists': False}},
            {'$set': {f'lessons.{lesson}': [score_entry]}}
        )
        if update_result.modified_count == 0:
            print("Failed to initialize a new lesson for an existing student.")
        else:
            print("Initialized a new lesson for an existing student.")
    else:
        print("Updated an existing lesson record for the student.")

def delete_lesson(topic):
    db['lesson-data'].delete_one({'topic': topic})
    db['quiz-data'].delete_many({'topic': topic})