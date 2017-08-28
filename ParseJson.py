import json

from pprint import pprint

fileJson = open("FileJson", "r")

pets = json.loads(fileJson.read())

pprint(pets)