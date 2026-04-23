#Pseudocode
#import classes
#import helper

#login function
#parameters: user dictionary
    #while true
        #show a welcome message and explain the login
        #ask if they want create a new user or login or exit
        #escape = false
        #if they choose to create a new user
            #ask for a username
            #create a user with the user class
            #call the string method and show them their account info
            #get the formated info and save it to the dictionary
            #return good
        #else if they choose login
            #while true:
                #show a message that if they forgot their username they can input forgot
                #ask for username
                #if username is "forgot"
                    #escape = true
                    #break
                #call search 
                #if it returns true
                    #ask for their password
                    #if the passsword matches the one in the dictionary
                        #break
                #else:
                    #show sorry that username doesn't exist please input a valid username
            #return good
        #else if they choose to exit
            #return quit
        #if escape is true:
            #continue
        


