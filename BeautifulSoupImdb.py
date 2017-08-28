import re
import json
import urllib2
from bs4 import BeautifulSoup
from pprint import pprint

request = urllib2.Request("http://www.imdb.com/search/title?release_date=2005-01-01,2017-01-01&user_rating=1.0,10")

response = urllib2.urlopen(request)

responseData = response.read()

response.close()

readHtml = BeautifulSoup(responseData, 'html.parser')

print readHtml.name

#print readHtml.prettify()

print readHtml.title

print readHtml.title.name

print readHtml.title.string

print readHtml.title.parent.name
#print readHtml.prettify()

print readHtml.p['class']

print readHtml.find_all('p')

print readHtml.a

#topTenMoviesByUserRating = readHtml.find_all('div', {'class': 'lister-item mode-advanced'})

#pprint(topTenMoviesByUserRating)


print readHtml.find_all('a')

print readHtml.find('a', {'href': '/?ref_=nv_home'})

print readHtml.find(href='/?ref_=nv_home')
'''''
for movie in topTenMoviesByUserRating:
    try:
        print movie.find_all('span', {'class': 'lister-item-index unbold text-primary'})[0].text
        print movie.find_all('a', {'href': '/?ref_=adv_li_tt'})[0].text
    except:
        pass
'''

linkDict = {}

itr = 0
for link in readHtml.find_all('a'):
    #print link.get('href')
    linkDict[itr] = link.get('href')
    itr+=1
print linkDict

print linkDict[0]

#print readHtml.get_text()

print type(readHtml.p)

tag = readHtml.p
print tag.name
print tag.string

print tag.attrs
print tag['class']

print tag.get_attribute_list('class')


print readHtml.head.contents

print readHtml.head.contents[0]
print readHtml.head.contents[1]

for string in readHtml.strings:
    print repr(string)

for string in readHtml.stripped_strings:
    print repr(string)
