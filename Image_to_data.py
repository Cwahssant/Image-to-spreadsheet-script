import install_missing_libraries
import csv
import sys

def main(file_name):
    output_file_name = file_name.split('.')[0]

    install_missing_libraries.check_dependencies()

    read_file(file_name)


#Returns the information from the image file 
def read_file(file):
    try:
        ptr = open(file, "r")

        ptr.close()
    except:
        print(file, "does not exist")


# Writes information to a csv file
def write_info(file_ptr):
    return