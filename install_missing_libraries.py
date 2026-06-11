from pkgutil import iter_importers

#Checks whether the user has the required dependencies installed. If not then it'll download them.
def check_dependencies():
    required = ['easyocr']
    missing = []

    for library in required:
        print(iter_importers(library))

    