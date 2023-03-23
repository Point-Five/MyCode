import csv, json
import os, shutil, time

class File_Handler():
    """A class that handles manupulation of data"""
 
    def __init__(self, passed_directory="text_files"):
        """Initialize an instance of the file manager class."""
        self.text_files_directory = passed_directory
        self.file_data = []

    def backupCsvAndJsonFiles(self):
        """Creates a backup of all csv and json files within the declared directory"""
        directory = self.text_files_directory
        # Make sure the text file directory exists if data is imported from elsewhere
        if not os.path.isdir(directory):
            os.mkdir(directory)
        # Create a backup directory within the text files if one does not exist.
        if not os.path.isdir(f"{directory}/backups"):
            os.mkdir(f"{directory}/backups")
        # Iterate through the files that exist and backup csv and json files.
        for entry in os.listdir(directory):
            directory_file = f"{directory}/{str(entry)}"
            backup_file = f"{directory}/backups/{str(entry)}.backup.{str(time.time())}"
            # Split extension from filename and test via normalized lowercase letters.
            ext = os.path.splitext(directory_file)[-1].lower()
            if ext == ".csv":
                shutil.copy2(directory_file, backup_file)
            elif ext == ".json":
                shutil.copy2(directory_file, backup_file)

    def dictList_ExportToCsv(self, passed_list, output_file_name):
        """Exports a python list of dictionary items to a csv file.
        Arguments:
            passed_list: a list of dictionaries, output_file_name: the file that will be written to."""
        keys = passed_list[0].keys()
        with open(output_file_name, "w", newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(passed_list)

    def dictList_ExportToJson(self, passed_list, output_file_name):
        """Exports a python list of dictionary items to a json file.
        Arguments:
            passed_list: a list of dictionaries, output_file_name: the file that will be written to."""
        with open(output_file_name, "w") as output_file:
            json.dump(passed_list, output_file)

    def dictList_RemoveDuplicates(self, passed_list):
        """Removes duplicate records from a list of dictionary items.
        Arguments:
            passed_list: A python list filled with dictionary items
        Returns:
            A cleaned pythin list of dictionary items that have duplicates removed."""
        clean_list = []
        for item in range(len(passed_list)):
            if passed_list[item] not in clean_list[item + 1:]:
                clean_list.append(passed_list[item])
        return clean_list

    def importNewTextFile(self, passed_file):
        """Imports the data from a text file and backs up existing csv and json files."""
        with open(passed_file) as file:
            first_line = file.readline()
            header = self.getHeader(first_line)
            data = []
            for line in file:
                cleaned_line = self.convertPipedStringToList(line)
                line_dict = {header[i]: cleaned_line[i] for i in range(len(header))}
                data.append(line_dict)
        self.file_data = self.dictList_RemoveDuplicates(data)
        self.backupCsvAndJsonFiles()
        self.dictList_ExportToCsv(self.file_data, f"{self.text_files_directory}/customers.csv")
        self.dictList_ExportToJson(self.file_data, f"{self.text_files_directory}/customers.json")

    def validateFileExists(self, passed_path):
        """Checks to see if a file exists, and returns a true or false boolean."""
        try:
            if os.path.isfile(passed_path):
                return True
        except FileNotFoundError:
            return False

#### Begin region for text file line handling ####

    def convertPipedStringToList(self, passed_string):
        """Takes a passed string and cleans it for processing.
        Returns:
            A cleaned list item to process."""
        cleaned_line = self.removePoundSymbol(passed_string)
        tmp_line = cleaned_line.split("|")
        if tmp_line.__contains__("\n"):
            tmp_line.remove("\n")
        return tmp_line

    def getHeader(self, passed_string):
        """Takes a passed string and cleans the data for a header file.
        Returns:
            A cleaned list with no new line characters, no empty records."""
        cleaned_line = self.removePoundSymbol(passed_string)
        tmp_header = cleaned_line.split("|")
        if tmp_header.__contains__("\n"):
            tmp_header.remove("\n")
        if tmp_header.__contains__(""):
            tmp_header.remove("")
        return tmp_header 

    def removePoundSymbol(self, passed_string):
        """Removes the pound symbol from a string of characters
        Returns:
            A cleaned string with no pound symbol characters."""
        output_string = ""
        for character in passed_string:
            if character != "#":
                output_string = output_string + character
        return output_string

#### End region for text file line handling ####