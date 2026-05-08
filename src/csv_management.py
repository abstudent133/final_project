# Mh 1st csv management pseudocode
import pandas as pd
import ast

# save csv, takes in user dictionary:
def save_df(dictionary, file_path):
    # gets all keys and values
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    row_data = []
    # loops over them and adds them all to a list
    for i in range(len(keys)):
        row_data.append([keys[i], values[i]])
        print(row_data)
    # converts the list to a dataframe
    df = pd.DataFrame(row_data, columns = ["names", "info"])
    # adds dataframe to the csv
    df.to_csv(file_path)


# load csv:
def load_df(file_path):
    # create dataframe
    df = pd.read_csv(file_path)
    char_dict = {}
    # loops over rows in the csv and add them to a dictionary, saving by username
    for index, row in df.iterrows():
        char_dict[row["names"]] = ast.literal_eval(row["info"])
    # return the dictionary
    return char_dict

# DICTIONARY STRUCTURE:
    # users = {
    # username = {
        # password = password
        # money = money
        # avatar_base = avatar_base
        # inventory = {item : equipped, item_2 : unequipped}
    #}
#}

test = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5
}