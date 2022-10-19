import csv


class CSVFile:
  @staticmethod
  def ReadCSVFile(filePath):
    data = []
    header = []
    with open(filePath) as csvFile:
      csv_reader = csv.reader(csvFile)
      header.extend(next(csv_reader)) 
      for line in csv_reader:
        data.append(line)
    return header, data

  @staticmethod
  def WriteCSVFile(filePath, header, data):
    with open(filePath, 'wt', newline='') as csvFile:
      csv_writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
      csv_writer.writerow(header)
      for row in data:
        csv_writer.writerow(row)

  @staticmethod
  def GetDataFromCSVFile(filePath):
    data = []
    with open(filePath) as csvFile:
      csv_reader = csv.reader(csvFile)
      next(csv_reader)
      for line in csv_reader:
        data.append(line)
    return data
