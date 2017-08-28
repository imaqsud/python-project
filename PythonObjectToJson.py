import json

from pprint import pprint

students = {
    "101": {
        "name": "Maiq", "branch": "CSE", "college": "NIT Hamirpur"
    },
    "102": {
        "name": "Rahat", "branch": "ECE", "college": "NIT Rourkela"
    },
    "103": {
        "name": "Thomas", "branch": "EEE", "college": "MIT C"
    }
}

print repr(students)

jsonConverted = json.dumps(students, sort_keys=True, indent=2)

pprint(jsonConverted)


'''''for student in jsonConverted:
    pprint(student["101"])'''


pythonData = json.loads(jsonConverted)

pprint(pythonData["101"]["name"])