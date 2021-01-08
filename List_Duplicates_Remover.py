#!/usr/bin/env python3

# Swetha Moorthi
# ISQA3900850.1208 - 25 September 2020
# A Python Program to sort and remove duplicates from a list.

def main():

    # function call to display the title of the program
    display_title()

    # names list with duplicates
    names = ['maria', 'maria', 'will', 'sam', 'maria', 'kahn', 'sam', 'barry', 'george', 'hank', 'belinda', 'maria',
             'karthik']

    # simple sort on names list
    names.sort()

    # function call to eliminate duplicates in the names list
    unique_names = remove_duplicates(names)

    # prints names list
    print("Initial list of Names:")
    print(names)

    # prints unique names list
    print("\nList of Unique Names:")
    print(unique_names)

    print("\nThank you for your time. Bye!")


# function to display a welcome message
def display_title():
    print("Welcome to the List Duplicate Remover.\n")


# function to get total points as an input
def remove_duplicates(names):
    # list for unique names
    unique_names = []

    # loop through each name in the names list
    for name in names:
        # check whether the name is in unique names list
        if name not in unique_names:
            unique_names.append(name)

    return unique_names


# if started as the main module, call the main() function
if __name__ == '__main__':
    main()