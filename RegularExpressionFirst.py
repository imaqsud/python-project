import re
import urllib2
'''
wordsList = re.split(r'\s*', 'Hello, This is Thor')

for word in wordsList:
    print word
'''

data = 'm jknjkhvbhnjbnkdjsnibkvjShahpur Bangahuni, Waini, Samastipur, 848131'

address = re.findall(r'[A-Z][a-z]+', data)

print address

pin = re.findall(r'\d+', data)

print pin

fullAddress = address+pin
print fullAddress



nameAndAge = '''
                Thor is 31 and Shaique is 1
                Maiq is 23 and Rohan is 22
                Dwayne is 45 and Suhaan is 19
            '''
names = re.findall(r'[A-Z][a-z]+', nameAndAge)
ages = re.findall(r'\d{1,3}', nameAndAge)

itr=0

nameAgeDict = {}

for name in names:
    try:
        nameAgeDict[name] = ages[itr]
        itr+=1
    except:
        pass
print nameAgeDict



text = 'Hello, I am a software Engineer at Sprinklr. Sprinklr is a good company'

for sprinklr in re.finditer('Sprinklr', text):
    sprinklrTuple = sprinklr.span()
    print sprinklrTuple

randomText = 'sat, hat, mat, pat'
regText = re.findall(r'[shmp]at', randomText)
for rexT in regText:
    print rexT




anyThingBut = '222-555-678'
if re.search(r'\d{3}-\d{3}-\d{3}', anyThingBut):
    print 'Number found'


if not re.search(r'\D{3}-\D{3}-\D{3}', anyThingBut):
    print 'Number not found'






urlSite = 'https://www.summet.com/dmsi/html/codesamples/addresses.html'
request = urllib2.Request(urlSite)
response = urllib2.urlopen(request)
responseData = response.read()

print responseData

#regData = responseData.decode()

phoneNumbers = re.findall(r'\(\d{3}\) \d{3}-\d{4}', responseData)
for phoneNumber in phoneNumbers:
    print phoneNumber