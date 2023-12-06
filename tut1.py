import csv

with open('MANUFACTURER.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(''.join(row[0]))