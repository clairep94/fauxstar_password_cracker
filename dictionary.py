### OPTIONS 2 & 3: DICTIONARY COMPILER & DICTIONARY ATTACK ----------------- ###

## ----------- UI COMPONENTS --------------- ###
compiler_intro = '''

/////////////////////////////////////////////////////////////////


You have selected Option 2: Add to Program's 'Common Passwords' Data File.

This program contains a 'Common Passwords' data file compiled from several resources.
See the presentation for more info on the sources list.
This option allows you to add new password lists to this data file, while ignoring repeat entries.

What is the name of the file you'd like to add?

Please ensure that the file is located in the "Dictionaries" folder.
Please write the full name of the file including .txt.

>>>'''



dictionary_attack_intro = '''

/////////////////////////////////////////////////////////////////


You have selected Option 3: Dictionary Attack.
This method is the fastest method, however longer password lists will increase the runtime.
See the presentation for the sources list.

Please note, option 2 would ideally be rockyou.txt, a password list
from a infamous data breach on RockYou, which stored its data in plaintext
instead of password hashes. This list contains 14,341,564 unique passwords 
from 32,603,388 accounts, but I could not find a safe and free download of this file.
'''

dictionary_attack_choice = '''
Which dictionary would you like to use?

1. most_common_passwords.txt (13.2k entries)
2. 330k_probable_passwords.txt (330k entries)
3. phished_info.txt (15k entries if iterated)
4. Other file in the Dictionaries folder

>>>'''


## --------------- FUNCTIONS - DICTIONARY COMPILER ----------------- ###
def compile():
    '''
    Adds a new password list from a .txt file to the program's most_common_passwords.txt.
    This compiled word list can be used for attack options 4, 6, and 7 (Dictionary Attack, L33tspeak Attack and Hybrid Attack).

    Already compiled:
    file_name = "500_worst_passwords.txt"
    file_name = "2020-200_most_used_passwords.txt"
    file_name = "Common_user_pass_combos.txt"
    file_name = "twitter-banned.txt"
    file_name = "probable-v2-top12000.txt"
    file_name = "cities_names.txt" --- added word = word.lower().replace(" ", "") to address
    two word names like "New York" --> "newyork"
    '''

    ### Print intro for dictionary compiler and prompts user for name of new password list to add
    new_dict = input(compiler_intro)

    ### Opens new file and reads as a list
    with open("Dictionaries/" + new_dict) as file:
        addition_dictionary = file.read()
    addition_dictionary = addition_dictionary.split("\n")

    ### Opens existing data file and reads as a list
    with open("Dictionaries/most_common_passwords.txt") as file:
        destination_dictionary = file.read()
    destination_dictionary = destination_dictionary.split("\n")

    ### For loop to add any words in the additional_dictionary list that are not in the destination_dictionary_list
    for word in addition_dictionary:
        if word not in destination_dictionary:
            destination_dictionary.append(word)

    ### Re-writes the appended list as the data file
    with open("Dictionaries/most_common_passwords.txt", mode="w") as file:
        for word in destination_dictionary:
            ## added if statement so that the last entry does not add a space unnecessarily.
            file.write("\n"+word)

    ## Print to indicate end of function
    print(f"{new_dict} has been added to most_common_passwords.txt")
    print("This updated password list can be used for attack options 4, 6, and 7 (Dictionary Attack, L33tspeak Attack and Hybrid Attack).")


def dict_attack(password):
    '''
    Takes in the user's password list choice, reads each password entry and checks it against the password.

    To show that it is running, it will print an attempt every x tries depending on the length of the password list.

    :return None if no match is found.
    :return attempt if match is found.
    '''

    ## Introduce dictionary attack & show dictionary options
    print(dictionary_attack_intro)
    dict_choice = input(dictionary_attack_choice)

    ## Dictionary Choice & Print Intervals -- larger dictionaries have larger print intervals.
    if dict_choice == "1":
        dict_choice = "most_common_passwords.txt"
        interval = 30
    elif dict_choice == "2":
        dict_choice = "330k_probable_passwords.txt"
        interval = 100
    elif dict_choice == "3":
        dict_choice = "phished_info.txt"
        interval = 30

    # If user input is 4 or not 1,2,3 --> User can type name of different data file within the Dictionaries folder
    else:
        try:
            dict_choice = input(
                "\nWhat is the full name and extension of the file?\nMake sure it is in the Dictionaries folder.")
            interval = int(input("What is the print interval? \nRecommendation is 100 for 330k entries.\n>>>"))
        except:
            print("\nInvalid file name.")
            print("Running most_common_passwords.txt by default.\n")
            dict_choice = "most_common_passwords.txt"
            interval = 30

    ## Prints user's password list choice & print interval
    print(f"\n\nYou have chosen the following password list:")
    print(dict_choice)
    print(f"The program will now guess passwords and show every {interval}th attempt...\n")

    ### MAIN FUNCTION LOOP -----------------###
    ## Runs through each word in selected Password List/Dictionary.
    counter = 0 ## counter for number of attempts
    with open("Dictionaries/" + dict_choice) as file:
        for word in file:
            word = word.strip()
            if word == password:
                return word
            else:
                counter += 1
                if counter % interval == 0:
                    print(f">>>{word}<<<")  ## prints every intervalth attempt to show the function is working
