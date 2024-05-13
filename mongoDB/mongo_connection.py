from pymongo import MongoClient
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

password = config['DEFAULT']['MongoDBPassword']

uri_template = "mongodb+srv://elvachen2000:{password}@userdata.nwparbt.mongodb.net/?retryWrites=true&w=majority&appName=userdata"
uri = uri_template.format(password=password)

client = MongoClient(uri)

def run():
    try:
        # Ping the server to test MongoDB connection; this effectively checks connection
        print("Pinging MongoDB...")
        db = client.admin  # You can replace 'admin' with the name of your database
        print(db.command('ping'))  # This line checks the connection
        print("You successfully connected to MongoDB!")
    finally:
        # Close the connection
        client.close()

if __name__ == "__main__":
    run()
