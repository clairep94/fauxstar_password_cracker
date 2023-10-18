### OPTIONS 6: L33TSPEAK ------------------------ ###
import dictionary

## ----------- UI COMPONENTS --------------- ###
l33tspeak_attack_intro = '''

/////////////////////////////////////////////////////////////////


You have selected Option 6: Hashcat L33tspeak Attack.
Based on Hashcat's L33tspeak Attack, this attack cycles through chosen password list and generates
L33tspeak alternative spellings of each word. This attack can also be used on individual words.

Eg.  emily --> 3mily, 3MILY, 3m!ly, 3M!Ly, etc.

'''
word_or_dict_prompt = '''
Would you like to use a dictionary or a specific word?
Type D for dictionary or W for word
>>>>'''

## ----------- CONSTANTS & IMPORTS --------------- ###
import itertools
import dictionary


# Dictionary of alternative characters & alternative cases for each letter in the lowercase alphabet.
leet_subs = {
        "a": ["4","@", "a", "A"],
        "b": ["B", "b"],
        "c": ["C", "c"],
        "d": ["D", "d"],
        "e": ["3", "E", "e"],
        "f": ["F", "f"],
        "g": ["9", "G", "g"],
        "h": ["H", "h"],
        "i": ["1", "!", "I", "i"],
        "j": ["J", "j"],
        "k": ["K", "k"],
        "l": ["1", "L", "l"],
        "m": ["M", "m"],
        "n": ["N", "n"],
        "o": ["0", "O", "o"],
        "p": ["P", "p"],
        "q": ["Q", "q"],
        "r": ["R", "r"],
        "s": ["5", "$", "s", "S"],
        "t": ["7", "T", "t"],
        "u": ["U", "u"],
        "v": ["V", "v"],
        "w": ["W", "w"],
        "x": ["X", "x"],
        "y": ["Y", "y"],
        "z": ["Z", "z"]
    }


def l33t_speak_attack(password):
    '''
    Contains a dictionary of key value pairs for each lower case letter, and a list of alternative cases and
    L33tspeak alternative characters. (eg. a --> 4, @, a, A)

    Takes in the user's password list choice, loops through each word in a selected dictionary file,
    and uses get() to create a list of each character's list of alternative characters. If the character
    is not a lowercase letter, get() returns the original character.

    Then uses itertools.product() to generate all cartesian products from the list of lists of alternative characters
    for each character in the word, and checks each product against the target password.

    For example:

    emily --> 3mily, 3MILY, 3m!ly, 3M!Ly, etc.

    To show that it is running, it will print set of variations every x tries depending on the length of the dictionary.

    :return None if no match is found.
    :return attempt if match is found.

    '''

    # Introduce Hashcat's L33tspeak Attack.
    print(l33tspeak_attack_intro)

    # Ask if L33tspeak attack should be on specific word or a dictionary
    word_or_dict = input(word_or_dict_prompt).upper()

    #### SPECIFIC WORD ###########################################################
    if word_or_dict == "W":

        # Ask for the word
        word = input("Please input the word:\n>>>")

        interval = 5 ## print interval
        counter = 0  ## counter for number of attempts
        print(f"The program will now guess passwords and show every {interval}th attempt...")


        ### MAIN FUNCTION LOOP ----------------- ###
        # For each char in word, if char is a key in leet_subs:
        # leet_subs[char] list is added to leet_variants list
        # If char is not a key in leet_subs:
        # get() returns the original char as default.
        # eg. ana1 --> [["4","@", "a", "A"], ["N", "n"], ["4","@", "a", "A"], ["1"]]
        leet_variants = [leet_subs.get(char, [char]) for char in word]

        # Generate all cartesian products from the leet_variants list of leet_sub[char] for char in word:
        for product in itertools.product(*leet_variants):
            attempt = ''.join(product)

            # Check if the leetspeak password matches the provided password
            if attempt == password:
                return attempt  # PW found --> returns PW string
            else:
                counter += 1
                if counter % interval == 0:
                    print(f">>>{attempt}<<<")  ##prints every intervalth attempt to show the function is working


    #### DICTIONARY ###########################################################
    elif word_or_dict == "D":
        # Asks user for password list choice
        dict_choice = input(dictionary.dictionary_attack_choice)

        ## Changes dict_choice to selected data file, and changes the print interval based on the
        # amount of entries. Longer entries have larger print intervals.
        if dict_choice == "1":
            dict_choice = "most_common_passwords.txt"
            interval = 500
        elif dict_choice == "2":
            dict_choice = "330k_probable_passwords.txt"
            interval = 50000
        elif dict_choice == "3":
            dict_choice = "phished_info.txt"
            interval = 500
        # If user input is 4 or not 1,2,3 --> User can type name of different data file within the Dictionaries folder
        else:
            try:
                dict_choice = input(
                    "\nWhat is the full name and extension of the file?\nMake sure it is in the Dictionaries folder.")
                interval = int(input("What is the print interval? \nRecommendation is 50000 for 330k entries.\n>>>"))
            except:
                print("\nInvalid file name.")
                print("Running most_common_passwords.txt by default.\n")
                dict_choice = "most_common_passwords.txt"
                interval = 500


        ### MAIN FUNCTION LOOP ----------------- ###
        counter = 0 ## counter for number of attempts
        print(f"The program will now guess passwords and show every {interval}th attempt...")


        ## Reads each word in the dictionary
        with open("Dictionaries/"+dict_choice) as file:
            for word in file:
                word = word.strip()

                ### MAIN FUNCTION LOOP ----------------- ###
                # For each char in word, if char is a key in leet_subs:
                # leet_subs[char] list is added to leet_variants list
                # If char is not a key in leet_subs:
                # get() returns the original char as default.
                # eg. ana1 --> [["4","@", "a", "A"], ["N", "n"], ["4","@", "a", "A"], ["1"]]
                leet_variants = [leet_subs.get(char, [char]) for char in word]

                # Generate all cartesian products from the leet_variants list of leet_sub[char] for char in word:
                for product in itertools.product(*leet_variants):
                    attempt = ''.join(product)

                    # Check if the leetspeak password matches the provided password
                    if attempt == password:
                        return attempt #PW found --> returns PW string
                    else:
                        counter += 1
                        if counter % interval == 0:
                            print(f">>>{attempt}<<<") ##prints every intervalth attempt to show the function is working

    ##### INVALID CHOICE ERROR ########################################
    else:
        print("Invalid input. Please choose a valid attack method.") ##loops back to attack choices

