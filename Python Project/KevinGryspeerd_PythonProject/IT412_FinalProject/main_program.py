from functions.app_functions import *

while True:

    printAppOptions()

    user_choice = int(getUserChoice())

    if user_choice == 1:
        # Option 1: Import a new data file.
        userChoice_importNewDataFile()
    elif user_choice == 2:
        # Option 2: Show data currently in a database.
        userChoice_showDatabaseTable()
    elif user_choice == 3:
        # Option 3: Add a record to the databases
        userChoice_addNewDatabaseRecord()
    elif user_choice == 4:
        # Option 4: Edit a record.
        userChoice_editDatabaseRecord()
    elif user_choice == 5:
        # Option 5: Quit the program
        break
    else:
        print("You did not enter a value between 1 and 5. Please try again.")