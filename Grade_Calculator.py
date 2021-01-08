#!/usr/bin/env python3

# Swetha Moorthi
# ISQA 3900 - 8 September 2020
# A Python Program to calculates Letter grade assuming a scale of 1000 points

# function to display a welcome message
def display_title():
    print("Welcome to the Grade Calculator.")
    print()


# function to get total points as an input
def get_total_points():
    while True:
        user_input = input("Enter the total score earned in numbers (0 - 1000): \t")

        # checks if the user input is a digit
        if user_input.isdigit():
            total_score = int(user_input)
            if 0 <= total_score <= 1000:
                break
            else:
                print("You must enter integer values >= 0 and <= 1000. Try again.\n")
        else:
            print("You must enter integer values >= 0 and <= 1000. Try again.\n")

    return total_score


# function determines letter grade based on the average earned
def get_letter_grade(average_earned):
    if 92 <= average_earned <= 100:
        letter_grade = "A"
    elif 88 <= average_earned <= 91.99:
        letter_grade = "B+"
    elif 82 <= average_earned <= 87.99:
        letter_grade = "B"
    elif 78 <= average_earned <= 81.99:
        letter_grade = "C+"
    elif 70 <= average_earned <= 77.99:
        letter_grade = "C"
    elif 60 <= average_earned <= 69.99:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade


def main():
    # function call to display the title of the program
    display_title()

    choice = "y"
    while choice.lower() == "y":

        # function call to get the total points as an input for a student
        total_points = get_total_points()

        # calculate percentage grade based on total points
        percentage_grade = total_points / 1000 * 100

        # function call to determine letter grade based on percentage grade
        letter_grade = get_letter_grade(percentage_grade)

        # display the letter grade for the student
        print("You earned an average of " + str(
            round(percentage_grade, 2)) + "%. Letter grade earned: " + letter_grade + "\n")

        # ask if the user wants to continue
        while True:
            choice = input("Would you like to enter another score? (y/n): ")
            print()
            if choice.lower() == "y" or choice.lower() == "n":
                break
            else:
                print("Please enter a valid choice. ")

    print("Thank you for your time. Bye!")


# if started as the main module, call the main() function
if __name__ == '__main__':
    main()