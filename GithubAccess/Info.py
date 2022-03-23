from github import Github

class Info:
        
    # Static method to make a clean dictionary of a github user
    # argument: NamedUser (pygithub api)
    # return type: dict[]
    @staticmethod
    def make_clean_dictionary(user):        
        dct = {
            "username": user.login,
            "num_of_repos": user.public_repos,
            "following": user.following,
            "followers": user.followers,
            "repositories": []
        }

        for repo in user.get_repos():
            print("\nGetting info on:\n" + repo.full_name)

            temp_dict = {"name": repo.full_name, 
                         "language": repo.language,
                         "commits": repo.get_commits().totalCount,
                         "forks": repo.forks_count,
                         "pulls": repo.get_pulls().totalCount,
                         "watchers": repo.watchers_count,
                         "stargazers": repo.stargazers_count,
                         "subscribers": repo.subscribers_count
                         }

            dct["repositories"].append(temp_dict)

        for key, value in dict(dct).items():
            if(value is None):
                del(dct[key])

        return dct

    # Static method to get username from user and return a user object
    # for the username provided
    # argument: Github instance
    # return type: NamedUser
    @staticmethod
    def get_username(github):
        valid_token = False
        # Keep asking user for until we receive a valid username
        while valid_token is False :
            username = input("Enter a username -> ")
            # check if username is valid by attempting a get request
            # if exception is raised then username is invalid
            try:
                user = github.get_user(username)
                valid_token = True
            except Exception:
                print("Invalid username entered!")

        return user

    # Static method to get token from user and return a Github instance
    # for the token provided
    # argument: None
    # return type: Github instance
    @staticmethod
    def get_token():
        valid_token = False
        # Keep asking user for token until we receive a valid token
        while valid_token is False :
            token = input("Enter a personal access token -> ")
            github = Github(token)
            # check if token is valid by attempting a get request
            # if exception is raised then token is invalid
            try:
                github.get_user("eli-scorpio")
                valid_token = True
            except Exception:
                print("Invalid token entered!")

        return github
    
    