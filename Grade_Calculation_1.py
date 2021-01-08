#!/usr/bin/env python3

# Swetha Moorthi
# ISQA3900850.1208 - 25 September 2020
# A Python Program which take scores as input and displays grades.

def main():

    # function call to display the title of the program
    display_title()

    try:
        # function call to get scores as an input and returns scores list
        test_scores = get_scores()

        # function call to add scores and returns total score
        total_score = add_scores(test_scores)

        # find length of test scores list
        score_count = len(test_scores)

        # calculate average score
        average_score = round((total_score / score_count), 2)

        # function call to determine letter grade based on percentage grade
        letter_grade = get_letter_grade(average_score)

        # displays the scores list, total, average score and Letter grade.
        print()
        print("Scores:\t\t", test_scores)
        print("Total:\t\t\t", total_score)
        print("Average score:\t", average_score)
        print("Letter grade:\t", letter_grade)

    except ZeroDivisionError as e:
        print("\nDivide by zero Error. You have not entered any valid test score.")

    print("\nThank you for your time. Bye!")


# function to get the scores from the user and saves them to the list
def get_scores():

    # initialize variables
    counter = 0
    test_scores = []

    while True:
        try:
            test_score = input("Enter test score (or '-1' to quit): ")
            if test_score != "-1":
                test_score = int(test_score)
            else:
                break
            if 0 <= test_score <= 100:
                test_scores.append(test_score)
            else:
                print("You must enter integer values >= 0 and <= 100 or -1 to quit. Try again.")
        except ValueError:
            print("You must enter integer values >= 0 and <= 100 or -1 to quit. Try again.")

    return test_scores


# function to add the scores in the test scores list
def add_scores(test_scores):
    total = 0
    for score in test_scores:
        total += score
    return total


# function to display a welcome message
def display_title():
    print("Welcome to the Grade Calculator.")
    print()


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


# if started as the main module, call the main() function
if __name__ == '__main__':
    main()