import csv
import sys
from PIL import Image
import pytesseract
import cv2

def main(file_name):
    file_extension_location = file_name.rfind('.')
    output_file_name = file_name[0:file_extension_location] + '.csv'

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\tiger\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe' #Delete later.
    #enhance_image(file_name)
    row_data = read_file(file_name)
    row_data = remove_empty_lists(row_data)
    
    with open(output_file_name, "w", newline = '') as ptr:

        if ptr == None:
            print("Error opening", output_file_name)
            sys.exit(1)

        #write_info(ptr, row_data)

    ptr.close()
    

#Returns the information from the image file 
def read_file(file):
    config = r'--oem 3 --psm %d' % 6

    try:
        img = Image.open(file)
        dat = pytesseract.image_to_data(img, config = config, output_type='data.frame')
        img.close()

        dat = dat[dat.text.notnull()]
        print(dat.head())
    except:
        print("Unable to open", file)
        sys.exit(1)

    
    row_data = []

    #dat_list = dat.splitlines(keepends = True)
    
    #for line in dat_list:
        #row_data.append(line.split())

    return row_data


# Writes information to a csv file
def write_info(file_ptr, info):
    data_writer = csv.writer(file_ptr)
    
    for row in info:   
        data_writer.writerow(row)


#Takes a list of lists (the data) and removes all empty lists
def remove_empty_lists(data):
    result = []

    for row in data:
        if len(row) == 0:
            continue

        result.append(row)

    return result 


'''
Enhances the provided image file to improve accuracy of text recognition
'''
def enhance_image(file):
    file_extension_loc = file.rfind('.')
    result = file[0:file_extension_loc] + '_enhanced' + file[file_extension_loc:]

    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"unable to read {file}")
        sys.exit(1)

    threshold_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    cv2.resize(threshold_img, None, fx = 2, fy = 2, interpolation= cv2.INTER_CUBIC)
    blurred_img = cv2.GaussianBlur(threshold_img, (5, 5), 0)

    currDPI = blurred_img.info.get('dpi') #change img name
    if currDPI[0] < 300 or currDPI [1] < 300:
        blurred_img.save(result, dpi=(300,300)) #change img name

    return result
