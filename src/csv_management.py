# Mh 1st csv management pseudocode

# save csv, takes in user dictionary:
    # gets all keys and values
    # loops over them and adds them all to a list
    # converts the list to a dataframe
    # adds dataframe to the csv


# load csv:
    # create dataframe
    # loops over rows in the csv and add them to a dictionary, saving by username
    # return the dictionary

# DICTIONARY STRUCTURE:
    # users = {
    # username = {
        # password = password
        # money = money
        # avatar_base = avatar_base
        # inventory = {item : equipped, item_2 : unequipped}
    #}
#}