from distutils.core import setup
import py2exe, sys, os

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.author = "Kevin Gryspeerd"
        self.name = "DLS x64 Update"
        self.version = "1.0.0.0"

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

target = Target(
    script = "DLS_x64_Migration.py",
    description = "Replace the DLS.ini contents with x64 updates and remove the VC.ini file from each subfolder.",
    dest_base = "DLS_Program",
)

setup(
    options = {"py2exe": {"bundle_files": 1, "compressed": 1,}},
    console = [target],
    zipfile = None,
)