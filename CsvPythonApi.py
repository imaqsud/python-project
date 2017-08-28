import csv
import urllib2
from pprint import pprint

request = urllib2.Request('https://www.ibm.com/support/knowledgecenter/SVU13_7.2.1/com.ibm.ismsaas.doc/reference/AssetsImportCompleteSample.csv?view=kc')

response = urllib2.urlopen(request)

#print response.json()

responseData = response.read()

pprint(responseData)

f = open('csvFileExample', 'w')
f.write(responseData)

fileCsv = open('csvFileExample', 'r')

csvFile = csv.reader(fileCsv)

for value in csvFile:
    try:
        print value[0]
        print value[1]
        print value[2]
        print value[3]
        print value[4]
    except:
        pass

