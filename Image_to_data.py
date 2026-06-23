import csv
import sys
from PIL import Image
import pytesseract

def main(file_name):
    output_file_name = file_name.split('.')[0] + '.csv'
    
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\tiger\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe' #Delete later.
    read_file(file_name)


#Returns the information from the image file 
def read_file(file):
    try:
        dat = pytesseract.image_to_string(Image.open(file))    
    except:
        print("Unable to open", file)
        sys.exit(1)

    prepped_data = []

    dat_list = dat.splitlines(keepends = True)
    for line in dat_list:
        prepped_data.append(line.split())

    return prepped_data


# Writes information to a csv file
def write_info(file_ptr, info):
    return
