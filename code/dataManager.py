import csv

class dataManager:
    def __init__(self, filename):
        self.filename = filename
        self.dataLength = 0
        self.data = {}
        self.headers = []
        self.readData()

    def readData(self):
        file = open("code/data/" + self.filename)
        csvreader = csv.reader(file)

        self.headers = next(csvreader)

        rows = []
        for row in csvreader:
            rows.append(row)
        self.dataLength = len(rows)

        file.close()

        header_index = 0
        for header in self.headers:
            self.data[header] = []
            for row in rows:
                self.data[header].append(row[header_index])
            header_index += 1

    def printData(self):
        print(self.headers)
        for i in range(self.dataLength):
            for header in self.headers:
                print(self.data[header][i], end=" ")
            print()

""" #CODE EXAMPLE
IBM = dataManager("daily_IBM.csv")
IBM.readData()
IBM.printData() """