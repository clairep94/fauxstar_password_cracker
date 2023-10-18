### OPTIONS 4: STANDARD BRUTE FORCE ----------------- ###

## ----------- UI COMPONENTS --------------- ###
brute_force_attack_intro = '''

/////////////////////////////////////////////////////////////////


You have selected Option 4: Brute Force Attack.
Please note that this method is the slowest if the password length is longer or unknown
or if the character set is bigger.

'''

brute_force_attack_char_set_choice = '''
Which character set would you like to choose?

1. Letters only (upper and lower)
2. Numbers only
3. Special Characters only
4. Letters & Numbers
5. Letters & Special Characters
6. All Characters

>>>'''


## ----------- CONSTANTS & IMPORTS --------------- ###
import string
import itertools

charset_codes = {
    1: string.ascii_letters,
    2: string.digits,
    3: (string.punctuation + " "),
    4: (string.ascii_letters + string.digits),
    5: (string.ascii_letters + string.punctuation + " "),
    6: (string.ascii_letters + string.punctuation + " " + string.digits)
}

print_intervals = {
    1: 100,
    2: 30,
    3: 30,
    4: 1000,
    5: 1000,
    6: 10000
}


## --------------- FUNCTIONS - STANDARD BRUTE FORCE ----------------- ###
def brute_force_standard(password):
    '''
    Takes in the user's character set choice, asks them to attempt the brute
    force method with either known password length or a max password length.
    Then uses itertools to generate cartesian products from the character set with
    either the known password length, or from length = 1 to the max password length.

    product('ABCD', repeat=2) ==> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD

    To show that it is running, it will print an attempt every 100 tries.
    This is best used for passwords with a length smaller than 5 chars.

    :return None if no match is found
    :return attempt if match is found.
    '''

    # Introduce Brute Force Attack and ask for character set
    print(brute_force_attack_intro)
    choice = int(input(brute_force_attack_char_set_choice))

    # Sets charset to choice and assigns a print interval according to the size of the charset
    charset = charset_codes[choice]
    interval = print_intervals[choice]

    # Print character set chosen
    print(f"\n\nYou have chosen the following character set:")
    print(charset)
    # Print print interval
    print(f"The program will now guess passwords and show every {interval}th attempt...\n")


    ## ------ MAIN FUNCTION LOOP ----------###
    counter = 0  ## counter for number of attempts

    ## If password length is known:
    if input("Is the password length known? (Y or N)\n>>>").upper() == "Y":

        length = int(input("What is the password length?\n>>>"))
        print(f"The program will now guess passwords and show every {interval}th attempt...")

        ## Generates cartesian products with length of length and joins each as a string to match against target pw
        for product in itertools.product(charset, repeat=length):
            attempt = "".join(product)
            if attempt == password:
                return attempt  # PW found --> returns PW string
            else:
                counter += 1
                if counter % interval == 0:
                    print(f">>>{attempt}<<<")  ##prints every intervalth incorrect attempt to show the function is working

    ## If password length is not known
    else:
        max_length = int(input("What is the max password length?\n>>>"))
        print(f"The program will now guess passwords and show every {interval}th attempt...")

        ## For each length from 1 to max length, generates cartesian products with that length and joins each as a string
        ## to match against the target pw
        for len in range(1, max_length + 1):
            for product in itertools.product(charset, repeat=len):
                attempt = "".join(product)
                if attempt == password:
                    return attempt  # PW found --> returns PW string
                else:
                    counter += 1
                    if counter % interval == 0:
                        print(f">>>{attempt}<<<")  ##prints every intervalth attempt to show the function is working



