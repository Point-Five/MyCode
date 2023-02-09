#################################################################
#    Author: Kevin Gryspeerd                                    #
#      Date: February 9, 2023                                   #
#   Purpose: Update the DLS finance files from x86 to x64       #
#            This will rewrite the contents of only             #
#            user profiles that already have the file.          #
#            This also removes the VC.INI within                #
#            each subfolder.                                    #
#################################################################
import os

# Get the path of the working directory
directory = 'C:\\Users\\'
# List of subfolders for the directory that need to be modified
folder_list = ["DLS-CashMgt", "DLS-Invest", "DLS-LDP", "DLS-Trust"]

def overwrite_userprofile_file(passed_userprofile, passed_folder):
    """This function overwrites the DLS.INI file of each folder with the 64bit updates.
    Arguments:
        The userprofile being modified. The subfolder of where the DLS.INI file is located."""
    userprofile_file = passed_userprofile + "\\" + passed_folder + "\\DLS.ini"
    if os.path.isfile(userprofile_file):
        with open(userprofile_file, 'r+') as file:
            file.write("[CheckVer]\n")
            file.write(f"CmdPath=C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE {passed_userprofile}\\{passed_folder}\\DLS64.ACCDE\n")
            file.write(f"CheckPath=C:\\DLS\\{passed_folder}\\UPDATE.INI\n")
            file.write(f"OldVerPath={passed_userprofile}\\{passed_folder}\\DLS64.ACCDE\n")
            file.write(f"NewVerPath=C:\\DLS\\{passed_folder}\\DLS64.ACCDE\n")
            file.write(f"VCPath={passed_userprofile}\\{passed_folder}\\VC.INI\n")
            file.write("PgrmCode=DLS\n")
            file.write("AutoCopy=Y")

def remove_userprofile_file(passed_userprofile, passed_folder):
    """This function removes the VC.INI file of the userprofile and subfolder passed to it.
    Arguments:
        UserProfile to be traversed. The subfolder to remove it from."""
    file_to_remove = passed_userprofile + "\\" + passed_folder + "\\VC.INI"
    if os.path.isfile(file_to_remove):
        os.remove(file_to_remove)

# List all the contents of the directory
for entry in os.listdir(directory):
    # Create the userprofile path of C:\Users\%UserProfile%
    userprofile = directory + str(entry)
    if os.path.isdir(userprofile):
        for folder in folder_list:
            overwrite_userprofile_file(userprofile, folder)
            remove_userprofile_file(userprofile, folder)