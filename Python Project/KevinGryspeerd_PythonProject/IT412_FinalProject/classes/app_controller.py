import os
from classes.customer import Customer

class App_Controller():
    """A class that is created to handle several functions for the application."""

    def __init__(self):
        """Construct an instance for handling the app."""
        self.db_tables = ['crm_data', 'mailings']

    def editTableRecordCondition(self, passed_table, passed_column):
        """Provides the functionality for editing a table record."""
        # Database Table CRM Data
        person_change = Customer()
        if passed_table == "crm_data":
            if passed_column == 'f_name':
                person_change.getFirstName()
                tmp_change = f"{passed_column}='{person_change.firstName}'"
            elif passed_column == 'l_name':
                person_change.getLastName()
                tmp_change = f"{passed_column}='{person_change.lastName}'"
            elif passed_column == 'address':
                person_change.getAddressLine()
                tmp_change = f"{passed_column}='{person_change.addressLine}'"
            elif passed_column == 'city':
                person_change.getCity()
                tmp_change = f"{passed_column}='{person_change.city}'"
            elif passed_column == 'state':
                person_change.getStateAbbreviation()
                tmp_change = f"{passed_column}='{person_change.stateCode}'"
            elif passed_column == 'zip':
                person_change.getZipCode()
                tmp_change = f"{passed_column}={person_change.zipCode}"
            elif passed_column == 'company':
                person_change.getCompanyName()
                tmp_change = f"{passed_column}='{person_change.companyName}'"
            elif passed_column == 'primary_phone':
                person_change.getPhoneNumber1()
                tmp_change = f"{passed_column}='{person_change.phoneNumber1}'"
            elif passed_column == 'secondary_phone':
                person_change.getPhoneNumber2()
                tmp_change = f"{passed_column}='{person_change.phoneNumber2}'"
            elif passed_column == 'email_address':
                person_change.getEmailAddress()
                tmp_change = f"{passed_column}='{person_change.email}'"
        # Database Table Mailings
        if passed_table == f"mailings":
            if passed_column == 'name':
                person_change.getFirstName()
                person_change.getLastName()
                tmp_name = person_change.buildFullName(person_change.firstName, person_change.lastName)
                tmp_change = f"{passed_column}='{tmp_name}'"
            elif passed_column == 'company':
                person_change.getCompanyName()
                tmp_change = f"{passed_column}='{person_change.companyName}'"
            elif passed_column == 'address':
                person_change.getAddressLine()
                person_change.getCity()
                person_change.getStateAbbreviation()
                person_change.getZipCode()
                tmp_address = person_change.buildMailingAddress(person_change.addressLine, person_change.city, person_change.stateCode, person_change.zipCode)
                tmp_change = f"{passed_column}='{tmp_address}'"

        return tmp_change

    def dict_TableColumns(self, passed_table):
        """A dictionary for each of the columns within each of the tables."""
        if passed_table == "crm_data":
            columns = {'f_name': "First Name", 'l_name': "Last Name", 'address': "Address Line", 'city': "City", 'state': "State", 'zip': "Zip Code", 'company': "Company", 'primary_phone': "Main Number", 'secondary_phone': "Alternate Number", 'email_address': "Email Address"}
        elif passed_table == "mailings":
            columns = {'name': "Name", 'company': "Company Name", 'address': "Mailing Address"}
        return columns

    def getAppDirectory(self):
        """Gets the main working directory for the app."""
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    def getDatabaseTable(self):
        """A method to call when attempting to get one of two options for a database table."""
        while True:
            self.printDatabaseTables()
            tmp_table = input("Please select a database: ")
            value_ok = self.validateOption1Or2(tmp_table)
            if value_ok:
                if tmp_table == "1":
                    return f"crm_data"
                elif tmp_table == "2":
                    return f"mailings"
                else:
                    print("The value you entered was not valid.")

    def getTableRecordIdCondition(self, passed_table):
        """Requests the user to enter the id for the table record they would like to update. Creates a sql condition based on the returned id parameters."""
        while True:
            tmp_id = input("Enter the id of the record you would like to edit: ")
            value_ok = self.validateIsDigit(tmp_id)
            if value_ok:
                if passed_table == "crm_data":
                    id = f"crm_id={tmp_id}"
                elif passed_table == "mailings":
                    id = f"mail_id={tmp_id}"
                return id

    def getTableRecordColumn(self, passed_table):
        """Provides the ability to get a table record that needs to be edited"""
        table_columns = self.dict_TableColumns(passed_table)
        counter = 0
        columns = list(table_columns.keys())
        for value in table_columns:
            counter = counter + 1
            print(f"{counter}. {table_columns[value]}")
        while True:
            choice = input("Enter the number for the value you would like to change: ")
            value_ok = self.validateIsDigit(choice)
            if value_ok:
                choice = int(choice)
                if 0 < choice <= counter:
                    choice = choice - 1
                    tmp_column = columns[choice]
                    return tmp_column
                else:
                    print("You did not enter a valid column choice.")

    def getTableRecordEditOrDeleteOption(self):
        """Asks the user what they would like to do with a record."""
        while True:
            self.printEditingOptions()
            tmp_option = input("Enter the option for the record you would like to edit: ")
            value_ok = self.validateOption1Or2(tmp_option)
            if value_ok:
                return tmp_option

    def printEditingOptions(self):
        """Prints out the options for editing or deleting a database table record."""
        print("1. Edit the record.")
        print("2. Remove the record.")

    def printDatabaseTables(self):
        """A method for printing out the database tables for this application."""
        print("1. CRM Data")
        print("2. Mailings")

    def validateIsDigit(self, passed_value):
        """Provides validation for ensuring that a digit is passed to it."""
        if passed_value.isdigit():
            return True
        else:
            print("The value you entered is not a digit, please try again.")
            return False

    def validateOption1Or2(self, passed_value):
        """A method to validate the inputs and returning a database."""
        if passed_value.isdigit():
            if passed_value == "1" or passed_value == "2":
                return True
            else:
                print("The number that was entered did not match one of the options.")
        else:
            print("The value that was entered was not a digit.")
        return False