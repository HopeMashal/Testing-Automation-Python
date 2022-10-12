import csv

with open('./PythonBasics/CSVTask/CSVFiles/input.csv', 'rt') as f:
    csv_reader = csv.reader(f)

    next(csv_reader) # skip the header

    for line in csv_reader:
        print(line)  # Print as Array