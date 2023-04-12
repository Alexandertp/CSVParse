import csv
from collections import Counter
CSVFileToParse = "Alle kommentarer, Studentpulse Mercantec export 2023-03-06 09_41_55.csv"
CSVStats = []
class CSVEntry:
    name = ""
    answers = []
    occurrence = 0



with open(CSVFileToParse) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}')
            line_count += 1
        i = 0
        while i < len(CSVStats):
            if row[2] == CSVStats[i].name:
                CSVStats[i].answers.append(row[7])
                CSVStats[i].occurence += 1
            else:
                CSVStats.append(CSVEntry)
                CSVStats[i].name = row[2]
                CSVStats[i].answers.append(row[7])
                CSVStats[i].occurence += 1



    print(f'Processed {line_count} lines.')