
from pymongo import MongoClient
client = MongoClientclient = MongoClient("replace your mongodb details")
db = client["sentiment_db"]
collection = db["results"]
def save_to_db(text, sentiment):
    entry = {"text": text, "sentiment": sentiment["label"], "score": sentiment["score"]}
    collection.insert_one(entry)

# from pymongo import MongoClient

# # Replace with your actual password (encode special characters if needed)
# client = MongoClientclient = MongoClient("replace mongodb details")
# db = client["sentiment_db"]
# collection = db["results"]

# def save_to_db(text, sentiment):
#     entry = {"text": text, "sentiment": sentiment["label"], "score": sentiment["score"]}
#     collection.insert_one(entry)

# # Test script to run when executed directly
# if __name__ == "__main__":
#     print("Starting database test...")
#     try:
#         # Test connection
#         databases = client.list_database_names()
#         print("Connection successful. Available databases:", databases)
        
#         # Test saving data
#         sample_text = "This is a test"
#         sample_sentiment = {"label": "POSITIVE", "score": 0.95}
#         save_to_db(sample_text, sample_sentiment)
#         print("Sample data saved successfully.")
        
#         # Test retrieving data
#         data = list(collection.find())
#         print("Data in collection:", data)
#     except Exception as e:
#         print(f"Error occurred: {e}")
#     finally:
#         print("Test completed.")