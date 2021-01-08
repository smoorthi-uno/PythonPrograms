# Swetha Moorthi
# ISQA 3900 - November 12, 2020
# A Python program to read customer data from a .csv file, stores each customer’s data in a Customer object
# to a Python list and allows the user to lookup a customer by specifying the customer’s ID.

import csv
import sys
from Customer import Customer


# function to read customers data from csv file
def read_customers():
    filename = 'customers.csv'
    # list to store the all customer objects from the csv file
    customers = []
    try:
        with open(filename, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if reader.line_num != 1:
                    # convert row to Customer Object
                    cust_id = row[0]
                    first_name = row[1]
                    last_name = row[2]
                    company_name = row[3]
                    address = row[4]
                    city = row[5]
                    state = row[6]
                    zipcode = row[7]
                    customer = Customer(cust_ID=cust_id, fName=first_name, lName=last_name, company=company_name,
                                        street=address, city=city, state=state, zipcode=zipcode)
                    customers.append(customer)
        return customers
    except FileNotFoundError as e:
        print("Customers not read from file - file not found: " + filename)
        sys.exit()
    except OSError as e:
        print("OSError: ", e)
        sys.exit()
    except Exception as e:
        print(type(e), e)
        sys.exit()


# function to display all the customers from the Customers list
def display_customers(customers):
    print("ALL CUSTOMERS")
    print("-" * 30)
    for customer in customers:
        print(customer.cust_ID + " : " + customer.cust_name())
    print()


# function to find the customer in the Customers list
def find_customer(cust_id, customers):
    found = False
    for customer in customers:
        if customer.cust_ID == cust_id:
            found = True
            print(customer)
    if not found:
        print("Customer " + cust_id + " does not exist")
    print()


def main():
    # displays the title of the program
    print("CUSTOMER VIEWER\n")

    # read customers from csv file and store them to a list
    customers = read_customers()

    # display customers from the list
    display_customers(customers)

    choice = 'y'

    while True:
        if choice == 'y':
            # user is prompted to enter customer id
            cust_id = input("Enter Customer ID: ")
            print()

            # find the customer in the customer list based on the user entered customer id
            find_customer(cust_id, customers)

            # user is prompted to enter choice whether or not to continue
            choice = input("Would you like to continue? y/n: ")
            print()
        elif choice == 'n':
            print("Bye!")
            break
        else:
            # user is prompted to enter a valid choice
            choice = input("Please enter a valid choice. Would you like to continue? y/n: ")
            print()


# if started as the main module, call the main() function
if __name__ == "__main__":
    main()