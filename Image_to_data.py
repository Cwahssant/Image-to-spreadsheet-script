import csv
import sys
from PIL import Image
import pytesseract

def main(file_name):
    file_extension_location = file_name.rfind('.')

    output_file_name = file_name[0:file_extension_location] + '.csv'

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\tiger\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe' #Delete later.
    row_data = read_file(file_name)
    row_data = remove_empty_lists(row_data)
    print(row_data)
    with open(output_file_name, "w", newline = '') as ptr:

        if ptr == None:
            print("Error opening", output_file_name)
            sys.exit(1)

        write_info(ptr, row_data)

    ptr.close()
    

#Returns the information from the image file 
def read_file(file):
    config = r'--oem 3 --psm %d' % 6

    try:
        dat = pytesseract.image_to_string(Image.open(file), config = config)
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


'''
Enhances the provided image file to improve accuracy of text recognition

This method will return the name of the enhanced image file
'''
def enhance_image(file):
    #Enhancing image work

    file_components = file.split(".")
    return file_components[0] + "_ENHANCED." + file_components[1]


#Takes a list of lists (the data) and removes all empty lists
def remove_empty_lists(data):
    result = []

    for row in data:
        if len(row) == 0:
            continue

        result.append(row)

    return result 