# csv_practice.py
# Author: Ernesto Espinosa
# Module 12 Lab: Read a Sales CSV, Write a Cleaned Report

import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

# Exercise 1 
print("--- Exercise 1 ---")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE},")




# Exercise 2

print("--- Exercise 2 ---")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Exercise 3
print("--- Exercise 3 ---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)

# Exercise 4
print("--- Exercise 4 ---")
total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")


# Exercise 5
print("--- Exercise 5 ---")

high_value = []
rows_read = 0



with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader) 
    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity 
        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"{total:.2f}"])


with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Quantity", "Total"])
    for row in high_value:
        writer.writerow(row)


    print(f"Wrote {len(high_value)} of {rows_read} rows to {CLEANED_FILE}.")






# Exercise 6
print("--- Exercise 6 ---")

dict_total = 0
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${dict_total:.2f}")
        
# Exercise 7 
print("--- Exercise 7 ---")
summary = {}

with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader: 
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + total


for product in sorted (summary): 
    print(f"{product}: ${summary[product]:.2f}")


# Exercise 8 
print("--- Exercise 8 ---")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} total revenue: ${total_revenue:.2f}\n")


entries = 0
with open(LOG_FILE, "r") as f:
    for line in f:
        entries += 1
        print(line.strip())


print(f"Log entries so far: {entries}")










# Reflection 1:
# This compares to doing the same task in Excel in a ways such as the code that I type into Python is similar in a way because I also have to type in formulas and constantly update it. 
# It also compares in a way in auditability because for Python it is a full written script that records every line of correction. While on the other hand Excel auditability is lower and takes time to manually do it and delete certain information and leaves no trace once saved.
# Some things that Python can do that Excel can't do easily are make multiple files or process large files. A Python script can process a loop through a folder that contains a variety of cvs files. While on the other hand, Excel can not do it as easily and requires more tedious work.
# Some things that Excel can do that Python can not do as easily are letting you immediately scan columns and spot formats quickly. Also it is easier to to share with non technical teams because every one has Excel installed and knows how to opena and run it, while on Python you need to have a certain configuration of code. 
 

# Reflection 2:
# A a real business process that would benefit from an append-mode log file would be an automated nightly E-Commerce store that syncs orders.
# This can come in handy because making a script that extracts all orders placed that day and having it calculate taes and shipping fees and making it write a summary CSV for a team using the "w" so people always get a fresh and new report.
# The script can also use an append mode to write lines of status to seperate files. It would preserve historical context and prevents accidental data and information loss. 


