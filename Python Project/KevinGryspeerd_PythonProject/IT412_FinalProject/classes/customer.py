from classes.validator import *

class Customer(Validator):
    """A class that represents a customer."""

    def __init__(self):
        """Initalize an instance of a customer."""
        super().__init__()
        self.addressLine = ''
        self.city = ''
        self.companyName = ''
        self.email = ''
        self.firstName = ''
        self.lastName = ''
        self.phoneNumber1 = ''
        self.phoneNumber2 = ''
        self.stateCode = ''
        self.zipCode = int

    def buildFullName(self, fname, lname):
        """Combines the first name and the last name into a single string."""
        name_size = len(fname) + len(lname)
        if name_size > 49:
            if len(fname) > 25:
                fname = fname[:24]
                name_size = len(fname) + len(lname)
                if name_size > 49:
                    lname = lname[:25]
            else:
                lname = lname[:25]
        name = f"{fname} {lname}"
        return name

    def buildMailingAddress(self, passed_address, passed_city, passed_state, passed_zip):
        """Builds an address into a single address format."""
        count = len(passed_address) + len(passed_city) + len(passed_state) + len(passed_zip)
        if count > 44:
            count = len(passed_city) + len(passed_state) + len(passed_zip) + 5
            add_size = 50 - count
            passed_address = passed_address[:add_size]
        mailAddress = f"{passed_address}, {passed_city}, {passed_state} {passed_zip}"
        return mailAddress

    def getAddressLine(self):
        """Gets the address line for the customer."""
        while True:
            tmp_address = input("Enter the address for the customer: ")
            value_ok = self.validateAddressLine(tmp_address)
            if value_ok:
                break
        self.addressLine = tmp_address

    def getCity(self):
        """Gets the city for the customers address."""
        while True:
            tmp_city = input("Enter the city for the customers address: ")
            value_ok = self.validateCityName(tmp_city)
            if value_ok:
                break
        self.city = tmp_city

    def getCompanyName(self):
        """Gets the name of the company for the customer."""
        while True:
            tmp_company = input("Enter the name of the company for the customer: ")
            value_ok = self.validateCompanyName(tmp_company)
            if value_ok:
                break
        self.companyName = tmp_company

    def getEmailAddress(self):
        """Gets the email address for the customer."""
        while True:
            tmp_email = input("Enter the email address for the customer: ")
            value_ok = self.validateEmailAddress(tmp_email)
            if value_ok:
                break
        self.email = tmp_email

    def getFirstName(self):
        """Gets the first name of the customer."""
        while True:
            tmp_name = input("Enter the first name of the customer: ")
            value_ok = self.validatePersonsName(tmp_name)
            if value_ok:
                break
        self.firstName = tmp_name
    
    def getLastName(self):
        """Gets the last name of the customer."""
        while True:
            tmp_name = input("Enter the last name of the customer: ")
            value_ok = self.validatePersonsName(tmp_name)
            if value_ok:
                break
        self.lastName = tmp_name
    
    def getPhoneNumber1(self):
        """Gets the first phone number for the customer."""
        while True:
            tmp_number = input("Enter the phone number for the customer: ")
            value_ok = self.validatePhoneNumber(tmp_number)
            if value_ok:
                break
        self.phoneNumber1 = tmp_number

    def getPhoneNumber2(self):
        """Gets the second phone number for the customer."""
        while True:
            tmp_number = input("Enter the phone number for the customer: ")
            value_ok = self.validatePhoneNumber(tmp_number)
            if value_ok:
                break
        self.phoneNumber2 = tmp_number

    def getStateAbbreviation(self):
        """Gets the abbreviated state code for the customer."""
        while True:
            tmp_state = input("Enter the state abbreviation for the customer: ")
            value_ok = self.validateStateAbbreviation(tmp_state)
            if value_ok:
                break
        self.stateCode = tmp_state.upper()

    def getZipCode(self):
        """Gets the zip code for the customer."""
        while True:
            tmp_zip = input("Enter the zip code for the customer: ")
            value_ok = self.validateZipCode(tmp_zip)
            if value_ok:
                break
        self.zipCode = tmp_zip