'''
Attack based on hashcat mask attack

If more information of the password is known, the user can specify the character set (for example
 lowercase alphabet, uppercase alphabet, number, special character).

 To show that it is running, it will print set of variations every 100000000 tries as it is intended for more
 complex passwords with a length greater than 5 chars.

'''
########### OPTIONS 5: HASHCAT MASK ----------------- #############################
## ----------- CONSTANTS & IMPORTS --------------- ###
import itertools

from dictionary import dictionary_attack_choice #see dictionary.py line 39

hashcat_mask_codes = {
    "n": ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    "l": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    "u": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    "s": ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', " "],
    "a": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    "x": ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', " "],
    "y": ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    "z": ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ']
}

mask_attack_codes_explained = '''
    The codes for the mask are:
    n: (0-9)
    l: (a-z)
    u: (A-Z)
    s: (!@#$ etc.)
    a: (a-z), (A-Z)
    x: (0-9), (!@#$ etc)
    y: (0-9), (a-z)
    z: All Characters
    '''

## ----------- UI COMPONENTS --------------- ###
hashcat_mask_attack_intro = '''

/////////////////////////////////////////////////////////////////


You have selected Option 5: Hashcat Mask Attack.
Based on Hashcat's Mask Attack, this is a faster version of the brute force attack, and can
be used on longer or more complex passwords.

Please use the following codes to indicate the character set for each character of the password.

Eg. emilY135@ --> llllunnns

'''



## --------------- MAIN FUNCTION - MASK ATTACK ----------------- ###
def mask_attack(password):
    '''
     Based on Hashcat's Mask Attack, this is a faster version of the brute force attack, and can be used on longer,
     more complex passwords.
     If more information of the password is known, the user can specify the character set (for example
     lowercase alphabet, uppercase alphabet, number, special character).

     To show that it is running, it will print set of variations every 100000000 tries as it is intended for more
     complex passwords with a length greater than 5 chars.

     :return None if no match is found.
     :return attempt if match is found.
     '''

    # Introduce Hashcat's Mask Attack.
    print(hashcat_mask_attack_intro)

    ## counter for number of attempts
    counter = 0
    ## Print interval is every 100000000th attempt
    interval = 100000000

    ## Prints key value pairs for the mask code
    print(mask_attack_codes_explained)

    ## Prompts user to input their mask.
    mask = input("Please input your mask.\nFor reduced runtime, be as precise as possible. \n>>> ")
    print(f"The program will now guess passwords and show every {interval}th attempt...")

    # Generate list of lists from each char in mask with get()
    for char in mask:
        if char in hashcat_mask_codes:
            mask_variants = [hashcat_mask_codes.get(char, [char]) for char in mask]

            # Generate all cartesian products from the mask_variants list of hashcat_mask_codes[char] for char in mask:
            for product in itertools.product(*mask_variants):
                attempt = "".join(product)

                # Check if the mask attack password matches the provided password
                if attempt == password:
                    return attempt #PW found --> returns PW string
                else:
                    counter += 1
                    if counter % interval == 0:
                        print(f">>>{attempt}<<<")  ##prints every 100000000th attempt to show the function is working
        else:
            print("Invalid mask input, please try another attack.")

