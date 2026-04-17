#Pseudocode
#import random
import random

#User class
    #initiate(username)
    #formate
        #take username, hashed password, starting amount of money, and an empty invintory and create a dictionary to save to the csv
    #password
        #ask if they want to make their own password or have one generated
        #if manual
            #ask for the password
        #else if they choose generate
            #run the password generator
        #take the password, hash it
    #password generator
    def main():

        #loop menu until user exits
        while True:

            #print menu options
            print("\nMAIN MENU")
            print("1. Generate Passwords")
            print("2. Exit")

            #choice = user menu selection
            choice = input("Choose an option: ").strip()

            #if choice is generate passwords
            if choice == "1":

                #ask for password length
                length = int(input("How long does the password need to be: "))

                #ask for character requirements
                lower = input("Lowercase letters (Y/N): ").upper() == "Y"
                upper = input("Uppercase letters (Y/N): ").upper() == "Y"
                numbers = input("Numbers (Y/N): ").upper() == "Y"
                special = input("Special characters (Y/N): ").upper() == "Y"

                #build character list based on choices
                characters = build_character_list(lower, upper, numbers, special)

                #if no character types selected
                if len(characters) == 0:
                    print("You must select at least one character type.")
                    continue

                #print password header
                print("\nPossible Passwords:\n")

                #generate 4 passwords
                for i in range(4):
                    print(generate_password(length, characters))

            #if choice is exit
            elif choice == "2":
                break

            #if invalid option
            else:
                print("Invalid option.")

        #end message
        print("Thank you for using the password generator.")


    #character function
    #intake what types of characters are allowed
    def build_character_list(self):

        #characters list starts empty
        characters = []

        #if lowercase allowed add lowercase ascii
        if self.lower:
            for i in range(97, 123):
                characters.append(chr(i))

        #if uppercase allowed add uppercase ascii
        if self.upper:
            for i in range(65, 91):
                characters.append(chr(i))

        #if numbers allowed add number ascii
        if self.numbers:
            for i in range(48, 58):
                characters.append(chr(i))

        #if special allowed add special ascii
        if self.special:
            for i in range(33, 48):
                characters.append(chr(i))

        #return characters list
        return characters
    #random function
    #intake the range and if it a character(char) or just a random number(numb)
    def random_value(start, end, value_type):

        #num is a random integer between the numbers of range
        num = random.randint(start, end)

        #if type is "char"
        if value_type == "char":
            #character is chr(num)
            return chr(num)

        #else
        else:
            #character = num
            return str(num)
    