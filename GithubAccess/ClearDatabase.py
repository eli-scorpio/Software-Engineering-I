# AUTHOR: Eligijus Skersonas
import pymongo

# Establish connection with mongodb
client = pymongo.MongoClient("mongodb://localhost:27017")
# Create database
database = client.classDB
# Clear database
print("\nClearing database...")
database.githubuser.delete_many({})
print("Database cleared!\n")