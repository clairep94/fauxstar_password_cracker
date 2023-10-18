'''
Attack based on hashcat hybrid attack

User can combine a dictionary and concatenate dictionary words with a mask

eg. password + nnnl --> password009a, password909g, password902j etc.
'''

########### OPTIONS 7: HASHCAT HYBRID ----------------- #############################
## ----------- CONSTANTS & IMPORTS --------------- ###
import itertools
import hashcat_mask
import dictionary
import l33tspeak

## ----------- UI COMPONENTS --------------- ###
hashcat_hybrid_attack_intro = '''

/////////////////////////////////////////////////////////////////


You have selected Option 7: Hashcat Hybrid Attack.
Based on Hashcat's Hybrid Attack, this attack generates possible concatenations
from a mask and adds it to either the front or end of a word. The attack can be applied
to either a single word or a dictionary.

Eg.  emily + nnnlss --> emily001a@! 
'''

## --------------- MAIN FUNCTION - HYBRID ATTACK ----------------- ###

def hybrid_attack(password):
    '''
    Based on Hashcat's Hybrid Attack, it combines a dictionary attack with a mask attack.
    It asks the user to input a mask and whether to add it to the in front or behind a word.
    Then it generates a list of possible combinations from that mask.

    It then either concatenates the mask combinations to a single word or to each word in a dictionary.

    To show that it is running, it will print set of variations every x tries depending on the length of the dictionary.

    :return None if no match is found.
    :return attempt if match is found.
    '''

    ## Introduce Hybrid Attack
    print(hashcat_hybrid_attack_intro)

###### MASK PORTION ####################################################################

    ## Prints key value pairs for the mask code
    print(hashcat_mask.mask_attack_codes_explained)

    ## Prompts user to input their mask.
    mask = input("Please input your mask.\nFor example for emily199@, type 'nnns'. \n>>> ")

    # Generate list of lists from each char in mask with get()
    concatenations = []
    for char in mask:
        if char in hashcat_mask.hashcat_mask_codes:
            mask_variants = [hashcat_mask.hashcat_mask_codes.get(char, [char]) for char in mask]

            # Generate all cartesian products from the mask_variants list of hashcat_mask_codes[char] for char in mask:
            for product in itertools.product(*mask_variants):
                concat = "".join(product)
                concatenations.append(concat)

    print("\nFinished generating concatenations from the mask.")


###### ORDER FOR CONCATENATION ####################################################################

    ## Asks user if word or mask should be first:
    first_element = input("\nDo you want to have the word or mask go first?\nType 'W' or 'M'. \nFor example for emily199@, type 'W'.\n>>>> ").upper()
    if first_element == "W":
        print("Word will go first.")
    elif first_element == "M":
        print("Mask will go first.")
    else:
        print("Invalid input. Word will go first as default.")
        word_or_mask = "W"


####### DICTIONARY PORTION ###############################################################

    # Ask if Hybrid attack should be on specific word or a dictionary
    word_or_dict = input(l33tspeak.word_or_dict_prompt).upper()


    #### SPECIFIC WORD ###########################################################
    if word_or_dict == "W":

        # Ask for the word
        word = input("Please input the word:\n>>>")

        interval = 5 ## print interval
        counter = 0  ## counter for number of attempts
        print(f"The program will now guess passwords and show every {interval}th attempt...")

        ### MAIN FUNCTION LOOP ----------------- ###
        for conc in concatenations:
            #Concatenate word and mask in order depending on first_element
            if first_element == "W":
                attempt = word + conc
            elif first_element == "M":
                attempt = conc + word

            # Check if the hybrid attack password matches the provided password
            if attempt == password:
                return attempt  # PW found --> returns PW string
            else:
                counter += 1
                if counter % interval == 0:
                    print(f">>>{attempt}<<<")


    #### DICTIONARY ###########################################################
    elif word_or_dict == "D":
        # Asks user for password list choice
        dict_choice = input(dictionary.dictionary_attack_choice)

        ## Changes dict_choice to selected data file, and changes the print interval based on the
        # amount of entries. Longer entries have larger print intervals.
        if dict_choice == "1":
            dict_choice = "most_common_passwords.txt"
            interval = 50
        elif dict_choice == "2":
            dict_choice = "330k_probable_passwords.txt"
            interval = 500
        elif dict_choice == "3":
            dict_choice = "phished_info.txt"
            interval = 50
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
                interval = 50

        ### MAIN FUNCTION LOOP ----------------- ###
        counter = 0 ## counter for number of attempts
        print(f"The program will now guess passwords and show every {interval}th attempt...")

        ## Reads each word in the dictionary
        with open("Dictionaries/"+dict_choice) as file:
            for word in file:
                word = word.strip()

                for conc in concatenations:
                    # Concatenate word and mask in order depending on first_element
                    if first_element == "W":
                        attempt = word + conc
                    elif first_element == "M":
                        attempt = conc + word

                    # Check if the hybrid attack password matches the provided password
                    if attempt == password:
                        return attempt  # PW found --> returns PW string
                    else:
                        counter += 1
                        if counter % interval == 0:
                            print(f">>>{attempt}<<<")



    ##### INVALID CHOICE ERROR ########################################
    else:
        print("Invalid input. Please choose a valid attack method.")  ##loops back to attack choices