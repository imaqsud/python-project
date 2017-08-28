import csv


f = open('FL_insurance_sample.csv', 'rU')

csvFile = csv.reader(f)

#csvList = list(csvFile)

'''
for csvRow in csvFile:
    print csvRow
'''

for csvRow in csvFile:
    try:
        print csvRow[0]
        print csvRow[1]
        print csvRow[2]
        print csvRow[3]
        print csvRow[4]
        print csvRow[5]
    except:
        pass

f.close()