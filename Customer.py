# Swetha Moorthi
# ISQA 3900 - November 12, 2020
# Customer class

class Customer:
    def __init__(self, cust_ID, fName="", lName="", company="", street="", city="", state="", zipcode=0):
        self.cust_ID = cust_ID
        self.fName = fName
        self.lName = lName
        self.company = company
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        return self.cust_name() + "\n" + self.cust_fullAddress()

    def cust_name(self):
        return self.fName + " " + self.lName

    def cust_fullAddress(self):
        address = ""
        if self.company != "":
            address += self.company + "\n"
        address += self.street + "\n"
        address += self.city + ", " + self.state + " " + self.zipcode
        return address

    def cust_ID(self):
        return self.cust_ID

    def cust_company(self):
        return self.company()