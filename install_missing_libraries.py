import sys
from importlib.util import find_spec
from shutil import which


#Checks whether the user has the required dependencies installed.
def check_dependencies():
    required = ['pytesseract', 'cv2']
    missing = False
    
    for library in required:
        if find_spec(library) is None:
            print(f"missing: {library} \nType \"pip install {library}\" in the command line to install.")
            missing = True

    if which("tesseract") is None:
        print("Please install Tesseract at https://tesseract-ocr.github.io/tessdoc/Installation.html\n or Tesseract is not in your PATH")
        missing = True

    if missing:
        sys.exit(1)