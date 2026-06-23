import csv
import sys
from PIL import Image
import pytesseract

def main(file_name):
    output_file_name = file_name.split('.')[0] + '.csv'
    
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\tiger\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe' #Delete later.
    row_data = read_file(file_name)

    with open(output_file_name, "w", newline = '') as ptr:

        if ptr == None:
            print("Error opening", output_file_name)
            sys.exit(1)

        write_info(ptr, row_data)

    ptr.close()


#Returns the information from the image file 
def read_file(file):
    try:
        dat = pytesseract.image_to_string(Image.open(file))    
    except:
        print("Unable to open", file)
        sys.exit(1)

    row_data = []

    dat_list = dat.splitlines(keepends = True)
    for line in dat_list:
        row_data.append(line.split())

    return row_data


# Writes information to a csv file
def write_info(file_ptr, info):
    data_writer = csv.writer(file_ptr)

    for row in info:
        data_writer.writerow(row)