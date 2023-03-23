from classes.app_controller import *
from classes.file_handler import *
from classes.customer import *
from data.database_handler import Database_Handler

# Initialize classes
app_controls = App_Controller()
app_database = Database_Handler()

def getUserChoice():
    """Gets the option for what the user will process.
    Returns:
        A validated integer"""
    userchoice_ok = False
    while not userchoice_ok:
        tmp_choice = input("Please enter what option you would like to do: ")
        userchoice_ok = validateInteger(tmp_choice)
    return tmp_choice

def printAppOptions():
    """Prints out the user's options for the app."""
    print("\n1. Import a new data file")
    print("2. Show data currently in a database")
    print("3. Add a record to the databases")
    print("4. Edit a record")
    print("5. Quit the program")

def userChoice_addNewDatabaseRecord():
    """A function that handles the addition of a database record to both databases. This is option 3 of the application."""
    if validateDatabaseConnection():
        new_record = Customer()
        new_record.getFirstName()
        new_record.getLastName()
        new_record.getAddressLine()
        new_record.getCity()
        new_record.getStateAbbreviation()
        new_record.getZipCode()
        new_record.getCompanyName()
        new_record.getPhoneNumber1()
        choice = input("Enter 'y' if you would like to include a secondary number: ")
        if choice.lower() == 'y':
            new_record.getPhoneNumber2()
        choice = input("Enter 'y' if you would like to include an email address: ")
        if choice.lower() == 'y':
            new_record.getEmailAddress()
        full_name = new_record.buildFullName(new_record.firstName, new_record.lastName)
        full_address = new_record.buildMailingAddress(new_record.addressLine, new_record.city, new_record.stateCode, new_record.zipCode)
        app_database.COMMAND_insertRecordIntoCrmDataTable(new_record.firstName, new_record.lastName, new_record.addressLine, new_record.city, new_record.stateCode, new_record.zipCode, new_record.companyName, new_record.phoneNumber1, new_record.phoneNumber2, new_record.email)
        app_database.COMMAND_insertRecordToMailingTable(full_name, full_address, new_record.companyName)
    else:
        print("Error connecting to the database")

def userChoice_editDatabaseRecord():
    """Provides functionality to edit a database record. This is used in option 4 of the application."""
    if validateDatabaseConnection():
        modified_table = app_controls.getDatabaseTable()
        if modified_table == "crm_data":
            app_database.COMMAND_showAllCrmDataTable()
        elif modified_table == "mailings":
            app_database.COMMAND_showAllMailingsTable()

        modified_condition = app_controls.getTableRecordIdCondition(modified_table)
        modified_method = app_controls.getTableRecordEditOrDeleteOption()

        if modified_method == "1":
            # Edit the record
            modified_column = app_controls.getTableRecordColumn(modified_table)
            modified_value = app_controls.editTableRecordCondition(modified_table, modified_column)
            app_database.COMMAND_updateTableRecord(modified_table, modified_condition, modified_value)
        elif modified_method == "2":
            # Confirm change and delete the database record.
            confirmed_change = input("This will remove the record from the database.\nEnter 'y' to confirm that you want to delete it: ")
            if confirmed_change.lower() == 'y':
                app_database.COMMAND_deleteDatabaseTableRecord(modified_table, modified_condition)
    else:
        print("Error connecting to the database.")

def userChoice_importNewDataFile():
    """Handles the operations of the first option for the application."""
    app_files = app_controls.getAppDirectory()
    app_files = app_files + "\\text_files"
    new_data = File_Handler(app_files)
    test_connection = validateDatabaseConnection()
    if not test_connection:
        are_sure = input("Error connecting to the database, press 'y' to generate the files without access to the database: ")
        if are_sure.lower() != 'y':
            return
    
    choice = input("Enter the path to your data file, or press 'd' to use test data: ")
    if choice != "d":
        new_data.validateFileExists(choice)
        if new_data:
            new_data.importNewTextFile(choice)
            if test_connection:
                app_database.importNewDatabase(new_data.file_data)
        else:
            print("The file you entered does not exist.")
    else:
        test_data = app_files + "\\customer_export.txt"
        new_data.importNewTextFile(test_data)
        if test_connection:
            app_database.importNewDatabase(new_data.file_data)

def userChoice_showDatabaseTable():
    """A function that returns a selected database table's data."""
    if validateDatabaseConnection():
        db_table = app_controls.getDatabaseTable()
        if db_table == "crm_data":
            app_database.COMMAND_showAllCrmDataTable()
        elif db_table == "mailings":
            app_database.COMMAND_showAllMailingsTable()
    else:
        print("Error connecting to the database.")

def validateDatabaseConnection():
    """Validate the connectivity to a database"""
    try:
        app_database.executeSelectQuery("SELECT 1")
        return True
    except:
        return False

def validateInteger(passed_value):
    """Validates an input value for the program.
    Arguments:
        A value that will be checked to see if it is of a digit.
    Returns:
        True or False Boolean"""
    if passed_value.isdigit():
        return True
    else:
        print("The value you entered is not a integer.")
        return False
