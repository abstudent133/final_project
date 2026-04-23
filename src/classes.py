#Pseudocode
#import random

#User class
class User():
    #initiate(username, password)
    def __init__(self, username):
        self.username = username
    #formate to add
    def formate_dict(self):
        #take username, hashed password, starting amount of money, and an empty invintory and create a dictionary
        #return it
        avatar_base = None
        user = {"username": self.username,
                "password": self.password(),
                "money": 100,
                "avatar base": avatar_base,
                "inventory": {}                
}
    #password
    def password(self):
        #ask for the password
        #take the password, hash it
        pass

    



    
    