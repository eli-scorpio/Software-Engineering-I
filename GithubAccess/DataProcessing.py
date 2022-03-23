# AUTHOR: Eligijus Skersonas
import pymongo

# Establish connection with mongodb
client = pymongo.MongoClient("mongodb://localhost:27017")

# Create database
database = client.classDB
# Create collection
githubuser = database.githubuser.find()

# create user.csv files
print("\nWriting data to user.csv.....")
with open('user.csv', 'w') as f:
    f.write("User,Repos,Following,Followers\n")
    dict = database.githubuser.find({'username' : {'$exists' : True}})

    for user in dict:
        f.write(str(user['username']) + ',' + str(user['num_of_repos']) + ',' + str(user['following']) +
        ',' + str(user['followers']) +'\n')

# create data.csv file
print("Writing data to data.csv.....")
with open('data.csv', 'w') as f:
    f.write("Repo,Language,Commits,Forks,Pulls,Watchers,Stargazers,Subscribers\n")
    dct = database.githubuser.find({'username' : {'$exists' : True}})

    for user in dct:
        for repo in user['repositories']:
            f.write(str(repo['name']) + ',' 
            + str(repo['language']) + ',' 
            + str(repo['commits']) + ',' 
            + str(repo['forks']) + ','
            + str(repo['pulls']) + ','
            + str(repo['watchers']) + ','
            + str(repo['stargazers']) + ','
            + str(repo['subscribers']) +'\n')