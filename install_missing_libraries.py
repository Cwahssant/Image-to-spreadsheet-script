import sys
from importlib.util import find_spec
from shutil import which


#Checks whether the user has the required dependencies installed. If not then it'll download them.
def check_dependencies():
    required = ['pytesseract']
    missing = False
    
    for library in required:
        if find_spec(library) is None:
            print("missing: ", library + "\nType \"pip install pytesseract\" in the command line to install.")
            missing = True

    if which("tesseract") is None:
        print("Please install Tesseract at https://tesseract-ocr.github.io/tessdoc/Installation.html")
        missing = True

    if missing:
        sys.exit(1)