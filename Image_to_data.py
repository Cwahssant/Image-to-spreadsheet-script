

def main():
    print("I'm in Image_to_data.py")

#Checks whether the user has the required dependencies installed. If not then it'll download them.
def check_dependencies():
    required = ['easyocr', 'csv']
    missing = []

    for library in required:
        print(library)
