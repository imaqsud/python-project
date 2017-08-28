import json
from pprint import pprint

f = open("JsonFile", "r")

jsonData = json.loads(f.read())

pprint(jsonData)

pprint(jsonData["id"])
pprint(jsonData["address"])
pprint(jsonData["nickNames"][0]["dateFrom"])

nickNames = jsonData["nickNames"]

for nickName in nickNames:
    pprint(nickName["dateFrom"])

address = jsonData["address"]
for addr in address:
    pprint(addr.firstChild.nodeValue)