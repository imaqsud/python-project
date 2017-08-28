from urllib2 import Request, urlopen, URLError

url = "http://placekitten.com/"

request = Request(url)

try:
    response = urlopen(request)
    data = response.read()
    print data[559:1000]
except URLError, e:
    print e
