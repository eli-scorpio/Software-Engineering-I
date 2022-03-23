# AUTHOR: Eligijus Skersonas

from github import Github # Import pygithub library
from Info import Info # Import Info class
import pymongo  # Import pymongo library

# Print Banner
print(" .d8888b.  d8b 888    888               888                  d8888                                            \n" +
                "d88P  Y88b Y8P 888    888               888                 d88888                                            \n" +
                "888    888     888    888               888                d88P888                                            \n" +
                "888        888 888888 88888b.  888  888 88888b.           d88P 888  .d8888b .d8888b .d88b.  .d8888b  .d8888b  \n" +
                "888  88888 888 888    888 \"88b 888  888 888 \"88b         d88P  888 d88P\"   d88P\"   d8P  Y8b 88K      88K      \n" +
                "888    888 888 888    888  888 888  888 888  888        d88P   888 888     888     88888888 \"Y8888b. \"Y8888b. \n" +
                "Y88b  d88P 888 Y88b.  888  888 Y88b 888 888 d88P       d8888888888 Y88b.   Y88b.   Y8b.          X88      X88 \n" +
                " \"Y8888P88 888  \"Y888 888  888  \"Y88888 88888P\"       d88P     888  \"Y8888P \"Y8888P \"Y8888   88888P'  88888P' \n" +
                "                                                                                                              ")

# Create a github instance using user token
github = Info.get_token()

# Ask user for username to create a user object for the given username
user = Info.get_username(github)

# Store user information into a dictionary and clean dictionary (remove null fields)
dct = Info.make_clean_dictionary(user)

# Establish connection with mongodb
client = pymongo.MongoClient("mongodb://localhost:27017")

# Create database
print("\nCreating Database...")
database = client.classDB
database.githubuser.insert_many([dct])
print("Database Created!")

