from distutils.core import setup
import py2exe, sys

class Target():
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.author = "Kevin Gryspeerd"
        self.name = "Update DLS File to x64"
        self.version = "1.0.0.0"

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

target = Target(
    script = "DLS_x64_Migration.py",
    description = "This program is designed to replace the contents of the DLS.ini file within subfolders under each user profile and deletes the VC.ini in each of the subfolders. The changes made within the file update it from an x86 edition to x64",
    dest_base = "DLS_Program",
)

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    zipfile = None,
    console = [target],
)