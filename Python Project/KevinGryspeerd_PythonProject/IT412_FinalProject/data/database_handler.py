from classes.customer import *
from data.database_access import DB_Connect

class Database_Handler(DB_Connect):
    """A class for handling the database interactions"""

    def __init__(self, db_username="root",db_password='', database='python_projects'):
        """Initalize an instance of the database handler class"""
        super().__init__(db_username, db_password, database)

    def COMMAND_deleteDatabaseTableRecord(self, passed_table, passed_condition):
        """A SQL Command that removes a record from a database.
        Arguments:
            passed_table: the table name, passed_condition: The SQL condition for removing the record."""
        self.executeQuery(f"DELETE FROM {passed_table} WHERE {passed_condition}")

    def COMMAND_insertRecordIntoCrmDataTable(self, passed_fname, passed_lname, passed_address, passed_city, passed_state, passed_zip, passed_company, passed_primary_phone, passed_secondary_phone, passed_email):
        """Inserts a new record into the 'crm_data' table."""
        sql_query = f"INSERT INTO `crm_data` (`crm_id`, `f_name`, `l_name`, `address`, `city`, `state`, `zip`, `company`, `primary_phone`, `secondary_phone`, `email_address`) VALUES (NULL, '{passed_fname}', '{passed_lname}', '{passed_address}', '{passed_city}', '{passed_state}', {int(passed_zip)}, '{passed_company}', '{passed_primary_phone}', '{passed_secondary_phone}', '{passed_email}')"
        sql_query.replace("''", "NULL")
        self.executeQuery(sql_query)

    def COMMAND_insertRecordToMailingTable(self, passed_name, passed_company, passed_address):
        """Inserts a new record into the 'mailings' table"""
        self.executeQuery(f"INSERT INTO `mailings` (`mail_id`, `name`, `company`, `address`) VALUES (NULL, '{passed_name}', '{passed_company}', '{passed_address}')")

    def COMMAND_showAllCrmDataTable(self):
        """Returns a list of database records from the crm data."""
        db_result = self.executeSelectQuery("SELECT * FROM crm_data")
        for record in db_result:
            print(f"ID: {record['crm_id']} | Name: {record['f_name']} {record['l_name']} | Company: {record['company']} | Address: {record['address']}, {record['city']}, {record['state']} {record['zip']} | Phone: {record['primary_phone']} | Alt Number: {record['secondary_phone']} | Email: {record['email_address']}")

    def COMMAND_showAllMailingsTable(self):
        """Returns a list of database records from the mailing list."""
        db_result = self.executeSelectQuery("SELECT * FROM mailings")
        for record in db_result:
            print(f"ID: {record['mail_id']} | Name: {record['name']} | Company: {record['company']} | Address: {record['address']}")

    def COMMAND_TruncateAllTables(self):
        """Removes all records from the applications database."""
        self.executeQuery("TRUNCATE TABLE crm_data")
        self.executeQuery("TRUNCATE TABLE mailings")

    def COMMAND_updateTableRecord(self, passed_table, passed_condition, passed_change):
        """A method that allows for the modification of a table record."""
        self.executeQuery(f"UPDATE {passed_table} SET {passed_change} WHERE {passed_condition}")

    def dictList_ImportRecordsToCrmDataTable(self, passed_list):
        """Provides a method for the data that has been gathered and converts it into data for the database"""
        for item in passed_list:
            self.COMMAND_insertRecordIntoCrmDataTable(
                passed_fname=item['first_name'],
                passed_lname=item['last_name'],
                passed_company=item['company_name'],
                passed_address=item['address'],
                passed_city=item['city'],
                passed_state=item['state'],
                passed_zip=item['zip'],
                passed_primary_phone=item['phone1'],
                passed_secondary_phone=item['phone2'],
                passed_email=item['email']
            )

    def dictList_ImportRecordsIntoMailingTable(self, passed_list):
        """Inserts a list of records to the mailings table."""
        person = Customer()
        for item in passed_list:
            full_name = person.buildFullName(item['first_name'], item['last_name'])
            company = item['company_name']
            mailing_address = person.buildMailingAddress(item['address'], item['city'], item['state'], item['zip'])
            self.COMMAND_insertRecordToMailingTable(full_name, company, mailing_address)

    def importNewDatabase(self, passed_list):
        """A method that combines several functions for updating the database. Removes all contents from the current tables and replaces it with new data"""
        self.COMMAND_TruncateAllTables()
        self.dictList_ImportRecordsToCrmDataTable(passed_list)
        self.dictList_ImportRecordsIntoMailingTable(passed_list)