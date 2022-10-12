import csv

header = ['id', 'name', 'address', 'zip']
rows = [
    [1, 'Hope', 'Palestine, Jerusalem', 99503 ],
    [2, 'Yuki', 'Japan, Tokyo', 97401 ],
]

with open('./PythonBasics/CSVTask/CSVFiles/output.csv', 'wt', newline='') as f:
    csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)

    csv_writer.writerow(header) # write header

    for row in rows:
        csv_writer.writerow(row)