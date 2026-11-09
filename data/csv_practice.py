# csv_practice.py
# Author: Ernesto Espinosa
# Module 12 Lab: Read a Sales CSV, Write a Cleaned Report

import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

# Exercise 1 
print("--- Exercise 1---")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE},")




# Exercise 2

print("--- Exercise 2")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader
    print(row)






# Reflection 1:


# Reflection 2:


