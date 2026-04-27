#Pseudocode
from helper import*


#User class
class User():
    #initiate(username, password)
    def __init__(self, username):
        self.username = username
    #formate to add
    def formate_dict(self):
        #take username, hashed password, starting amount of money, and an empty invintory and create a dictionary
        #return it
        #avatar base is a sprite that we will input
        avatar_base = None
        user = {"password": self.password(),
                "money": 100,
                "avatar base": avatar_base,
                "inventory": {}                
}
    #password
    def password(self):
        #ask for the password
        pw = input("Please create a password and input it here: ")
        #take the password, hash it
        hash_value = hash_pass(pw)
        return hash_value
    
    



    
    