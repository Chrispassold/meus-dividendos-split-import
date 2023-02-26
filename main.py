import math
import os

import pandas as pd
from jproperties import Properties

configs = Properties()
with open('local.properties', 'rb') as config_file:
    configs.load(config_file)

FULL_MOVIMENTS_CSV = configs.get("FULL_RECORDS_CSV").data
OUTPUT_PREFIX_CSV = "./output"
SPLIT_AFTER_N_ITEMS = 80

DELIMITER = ";" if configs.get("READ_DELIMITER_CSV").data is None else configs.get("READ_DELIMITER_CSV").data
DECIMAL = "," if configs.get("READ_DECIMAL_CSV").data is None else configs.get("READ_DECIMAL_CSV").data

full_csv = pd.read_csv(FULL_MOVIMENTS_CSV, delimiter=DELIMITER, decimal=DECIMAL, encoding="iso-8859-1", index_col=False)
amount_of_lines = len(full_csv)
amount_of_output_files = min(math.ceil(amount_of_lines/SPLIT_AFTER_N_ITEMS), amount_of_lines)

print("Amount of rows in file:", amount_of_lines)
print("Amount of files to output:",amount_of_output_files)

def create_file(df, idx):
    os.makedirs(OUTPUT_PREFIX_CSV,exist_ok=True)
    filename = os.path.join(OUTPUT_PREFIX_CSV, "output_{0}.csv".format(str(idx)))
    if os.path.exists(filename):
        os.remove(filename)
    
    df.to_csv(filename, header=None, sep=',', encoding='utf-8', index=False, decimal=",", lineterminator="\n")
    return filename


for idx in range(amount_of_output_files):
    start = idx * SPLIT_AFTER_N_ITEMS
    amount_left = len(full_csv[start:])+1
    end =  SPLIT_AFTER_N_ITEMS + start
    
    print("Output file created: ", create_file(full_csv[start:end], idx))

