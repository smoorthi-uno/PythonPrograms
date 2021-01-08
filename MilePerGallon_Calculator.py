#!/usr/bin/env python3

# Swetha Moorthi
# ISQA3900850.1208 - 18 October 2020
# A Python Program to Calculate Miles Per Gallon - Program stores each trips data to a list,
# saves the list to a csv file and reads trips from csv file before entering new trip data.

import csv


def main():
    # function call to display the title of the program
    display_title()

    while True:
        # two-dimensional list to store each trip data: miles driven, gas used, mpg value
        trips = []

        # user is prompted to enter choice to read trips from a file
        readcsv_choice = input("Would you like to read trips from a file? y/n: ")

        # if user selects to read trips from a previously saved file
        if readcsv_choice == 'y':

            # user is prompted for the filename
            csv_filename = input("Enter the csv filename containing the trip data: ")

            # function to read the trips into the list
            trips = read_trips(csv_filename)

            list_type = type(trips)
            if list_type != list:
                trips = []

            if len(trips) != 0:
                # function displays the trips from the file
                list_trips(trips)
                break
            else:
                break

        # if user selects not to read trips from a previously saved file - 'Do Nothing'
        elif readcsv_choice == 'n':
            print()
            break

        # if user enter invalid choice
        else:
            print("Please enter valid choice. Try again.")

    # user is prompted to enter choice to enter trip data
    tripinput_choice = input("Would you like to enter trip data? y/n: ")

    while True:

        if tripinput_choice == 'y':

            # list to store each trip data each time the user enters
            trip = []

            # get input from the user
            miles_driven = get_input("Enter miles driven: \t\t")
            gallons_used = get_input("Enter gallons of gas used: \t")

            if miles_driven > 0 and gallons_used > 0:
                mpg = miles_driven / gallons_used
                mpg = round(mpg, 2)
            else:
                print("Please enter values greater than 0.")
                continue

            # append trip data to one-dimensional trip list
            trip.append(miles_driven)
            trip.append(gallons_used)
            trip.append(mpg)

            # append trip list to trips list
            trips.append(trip)

            # print the elements of trip list
            list_trips(trips)

            tripinput_choice = input("Would you like to continue? y/n: ")

            if tripinput_choice == 'y':
                continue

            elif tripinput_choice == 'n':

                # save trips list data to a trips.csv file
                write_trips(trips)
                break

            else:
                tripinput_choice = input("Please enter valid choice? y/n: ")
                continue

        elif tripinput_choice == 'n':

            # save trips list data to a trips.csv file
            write_trips(trips)
            break

        else:
            tripinput_choice = input("Please enter valid choice? y/n: ")
            continue

    print("\nThank you for your time. Bye!")


# function to print the elements in the trips list
def list_trips(trips):
    if len(trips) == 0:
        print("Trips: Empty")
    else:
        print("Trips: ")
        i = 0
        for trip in trips:
            trip = trips[i]
            print("{:25} {:30} {:25}".format(str(i + 1) + ". Miles: " + str(trip[0]), "Gallons of gas: " + str(trip[1]),
                                             "Mpg: " + str(trip[2])))
            i += 1
    print()


# get input from the user
def get_input(prompt):
    while True:
        try:
            input_value = float(input(prompt))
            return input_value
        except ValueError:
            print("Enter numeric values only. Please try again.")


# function to save trips data i the list to a csv file
def write_trips(trips):
    filename = "trips.csv"
    try:
        with open(filename, "w", newline="") as outfile:
            writer = csv.writer(outfile)
            writer.writerows(trips)
            print("\nTrips saved to file: " + filename)
    except FileNotFoundError as e:
        print("FileNotFoundError: ", e)
    except OSError as e:
        print("OSError: ", e)
    except Exception as e:
        print(type(e), e)


# function to read trips data from a csv file
def read_trips(filename):
    trips = []
    try:
        with open(filename, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                trips.append(row)
        return trips
    except FileNotFoundError as e:
        print("Trips not read from file - file not found: " + filename)
    except OSError as e:
        print("OSError: ", e)
    except Exception as e:
        print(type(e), e)


# function to calculate mpg - not used in the program
def calc_mpg(miles_driven, gallons_used):
    try:
        mpg = miles_driven / gallons_used
        mpg = round(mpg, 2)
        return mpg
    except ZeroDivisionError:
        print("\nDivide by zero Error. Please enter values greater than 0.")


# function to display a welcome message
def display_title():
    print("Welcome to the Miles Per Gallon program.\n")


# if started as the main module, call the main() function
if __name__ == '__main__':
    main()