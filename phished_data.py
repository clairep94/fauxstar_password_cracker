# ====================================== PERSON CLASS FOR SUBMIT BUTTON =================================================== #
'''
I wanted to store the following information for the target and their love, and found the best way was to store
the information in objects, as I wanted this information & the generated strings for each person.

your_name
claire --.lower()
CLAIRE —.upper()
Claire — .capitalize()

your_month
June
JUNE — .upper()
june — .lower()
06 — months_num[months.index(your_month_var.get())]

your_day
27

your_year
1994
94 — [-2:]

your_date — products
[m][d][y]
[m][y][d]
[d][m][y]
[d][y][m]
[y][m][d]
[y][d][m]
[d][y]
[y][d]
[m][y]
[y][m]
[m][d]
[d][m]

'''

import itertools

### ---------- PERSON CLASS ----------------- ##
# Person class to store the name and birthday in different cases and formats
class Person:
    '''
    Store a person's name and birthday and in different cases and formats
    Creates a list of possible cartesian products of 2 of the date_lists lists, and 3 of the date_lists lists
    '''
    def __init__(self, label, name, Month, mm, dd, yyyy):
        self.label = label
        self.name = name.lower()
        self.NAME = name.upper()
        self.Name = name.capitalize()
        self.Month = Month
        self.MONTH = Month.upper()
        self.month = Month.lower()
        self.mm = mm
        self.dd = dd ## write months_num[months.index(your_month_var.get())] when initialising
        self.yyyy = yyyy
        self.yy = yyyy[-2:]

        ## all name formats as a lists
        self.names_list = [self.name, self.NAME, self.Name]

        ## all date formats as a lists
        self.months_list = [self.Month, self.MONTH, self.month, self.mm]
        self.days_list = [self.dd]
        self.years_list = [self.yyyy, self.yy]

        ## list of all date lists
        self.dates_lists = [self.months_list, self.days_list, self.years_list]

        ## all cartesian products from dates
        self.date_products = self.product(self.dates_lists)

        ## all generated name, date, and date combinations for this person as a list of strings:
        self.all_entry = self.names_list + self.months_list + self.days_list + self.years_list + self.date_products

    def product(self, dates_lists):
        all_possible_orders = []

        # Combinations of 2 lists
        for two_lists_combination in itertools.combinations(dates_lists, 2):
            for combo in itertools.product(*two_lists_combination): #generates tuples of combinations
                for perm in itertools.permutations(combo): #joins each tupple into a string
                    joined_str = ''.join(perm) #joins each tuple into a string
                    all_possible_orders.append(joined_str) #appends each string to all possible_orders list

        # All 3 lists together
        for combo in itertools.product(*dates_lists):
            for perm in itertools.permutations(combo): #generates tuples of cartesian permutations
                joined_str = ''.join(perm) #joins each tupple into a string
                all_possible_orders.append(joined_str) #appends each string to all_possible_orders list

        return all_possible_orders

    def __str__(self):
        return f"{self.name}\n" \
               f"{self.NAME}\n" \
               f"{self.Name}\n" \
               f"{self.Month}\n" \
               f"{self.MONTH}\n" \
               f"{self.month}\n" \
               f"{self.mm}\n" \
               f"{self.dd}\n" \
               f"{self.yyyy}\n" \
               f"{self.yy}" \
               f"{self.date_products}"

    def print_info(self):
        return f"For {self.label}\n:" \
               f"Entered Name: {self.name}\n" \
               f"Alternate Name Cases: {self.names_list}\n" \
               f"Entered Birthday: {self.Month} {self.dd} {self.yyyy}\n" \
               f"Alternate Date Formats: {self.date_products}"



# ====================================== CREATING CONCATENATED COMBINATIONS FROM THE PHISHED INFO =================================================== #
def all_concatenations():
    '''
    Takes phished_data.txt as an input and generates all possible combinations of elements from the list
    taken 2 at a time using itertools.combinations
    Then joins each combination to create the concatenated string
    Then appends each concatenated string into the phished_data.txt data file.

    ['a', 'b', 'c', 'd'] --> ['ab', 'ac', 'ad', 'bc', 'bd', 'cd']
    '''
    with open("Dictionaries/phished_info.txt") as file:
        current_dictionary = file.read()
    current_dictionary = current_dictionary.split("\n")
    all_possible_combinations = list(itertools.combinations(current_dictionary, 2))
    all_concatenations_list = [''.join(combo) for combo in all_possible_combinations]

    with open("Dictionaries/phished_info.txt", "a") as file:
        for word in all_concatenations_list:
            file.write("\n"+word)

    print("\nAdding concatenations to phished_info.txt")