from bs4 import BeautifulSoup
import urllib2
from pprint import pprint
import re

request = urllib2.Request("https://www.youtube.com/watch?v=HfRKfxyLkrs&index=34&list=PL9ooVrP1hQOHY-BeYrKHDrHKphsJOyRyu")

response = urllib2.urlopen(request)

responseData = response.read()
soup = BeautifulSoup(responseData)

#print soup.prettify()

#print soup.name

#print soup.title

#print soup.find_all(re.compile('^b'))

'''
for tag in soup.find_all(re.compile('h')):
    print tag.name
   '''

firstTenLinks = soup.find_all('a', limit=10)

for link in firstTenLinks:
    print link.get('href')