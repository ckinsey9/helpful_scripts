import os

from xlsx2csv import Xlsx2csv

INPUT_DIR = r'xlsx_input'
OUTPUT_DIR = r'xlsx_output'

for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".xls") or filename.endswith(".xlsx"): 
        name, file_extension = os.path.splitext(filename)
        input_file = os.path.join(INPUT_DIR, filename)
        output_file = os.path.join(OUTPUT_DIR, name) + ".csv"
        Xlsx2csv(input_file, outputencoding="utf-8").convert(output_file)

