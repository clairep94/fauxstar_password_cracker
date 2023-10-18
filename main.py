'''
FAUX STAR HYBRID ATTACK PASSWORD CRACKER:

The goal of this project is to demonstrate an understanding of the different strategies that hackers use to gain access
to victims' passwords.

These include:
Phishing, Dictionary Attack, Brute Force Attack, Hashcat Mask Attack, L33tspeak Attack
and Hashcat Hybrid Attack

'''
# ============================================================================= #

# ----------------------- IMPORTS: UI COMPONENTS -------------------------------#
import ui

# ----------------------- IMPORTS: ATTACK MODULES -------------------------------#
import dictionary
import brute_force
import phished_data
import l33tspeak
import hashcat_mask
import hashcat_hybrid


# ============================================================================= #

# ------------------------ MAIN PROGRAM ----------------------------------------#

## Introduce the program & print logo
print(ui.intro_ascii)
print(ui.intro_blurb)

## User inputs the target password
target_password = input("What is the password to crack?\n>>>")
print("")

## guess_password is declared as a blank string so that guess_password != target password
guess_password = ""


## --------------- MAIN PROGRAM LOOP: ---------------##
## while loop that repeats prompting user input for attack methods and executing attack methods
## until guess_password == target_password.
while guess_password != target_password:
    attack_method = input(ui.attack_options_blurb)


##----------- 1. FAUX STAR PHISH -------------------##
    if attack_method == "1":

        # Shows phishing email 'sent' to target
        print(ui.phishing_email)

        # Opens Faux Star tkinter GUI which writes inputs into phished_info.txt
        with open("faux_star.py") as f:
            exec(f.read())

        # On target exiting the program:
        print("\nVictim has been phished. Their info has been added to phished_info.txt.\nSelect another attack to use them")
        print("Use Sherlock to check their username or email address against other social media registrations for more\naccounts to target.")

        # Asks user if they would like to generate concatenations using 2 entries from phished_info.txt at a time
        if input("\nWould you like to generate combinations of 2 entries at a time from phished_info.txt?\nFor example: [emily, 1994] --> 1994emily, emily1994\nType 'Y' or 'N' >>>>").upper() == "Y":
            phished_data.all_concatenations()
            print("\nphished_data.txt has been extended to >15k entries. \nSelect another attack to use them")
        ## Loops back to attack choices


##----------- 2. DICTIONARY COMPILER ----------------##
    elif attack_method == "2":
        dictionary.compile()


##----------- 3. DICTIONARY ATTACK ----------------##
    elif attack_method == "3":
        result = dictionary.dict_attack(password=target_password)

        ## Check result
        if result is not None:
            guess_password = result  ##exits loop
        else:
            print(ui.password_not_found_blurb)


##----------- 4. STANDARD BRUTE FORCE ----------------##
    elif attack_method == "4":
        result = brute_force.brute_force_standard(password=target_password)

        ## Check result
        if result is not None:
            guess_password = result  ##exits loop
        else:
            print(ui.password_not_found_blurb)


##----------- 5. HASHCAT MASK ----------------##
    elif attack_method == "5":
        result = hashcat_mask.mask_attack(password=target_password)

        ## Check result
        if result is not None:
            guess_password = result  ##exits loop
        else:
            print(ui.password_not_found_blurb)


##----------- 6. L33tspeak Attack ----------------## ****
    elif attack_method == "6":
        result = l33tspeak.l33t_speak_attack(password=target_password)

        ## Check result
        if result is not None:
            guess_password = result  ##exits loop
        else:
            print(ui.password_not_found_blurb)



# ##----------- 7. Hybrid Attack ----------------## ****
    elif attack_method == "7":
        result = hashcat_hybrid.hybrid_attack(password=target_password)

        ## Check result
        if result is not None:
            guess_password = result  ##exits loop
        else:
            print(ui.password_not_found_blurb)



##------------- X. ERROR MESSAGE FOR INVALID ATTACK CHOICE ----------------##
    else:
        print("Invalid input. Please choose a valid attack method.") ##loops back to attack choices


## --------------- IF PASSWORD IS FOUND: ---------------##
print(ui.password_found_blurb)
print(f">>>>{guess_password}<<<<")
print(f"\n\nThanks for using FAUX-STAR Password Cracker.")