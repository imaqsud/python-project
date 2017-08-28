import requests

body = {'Name': 'Eric', 'Age': '26'}

response = requests.post("http://placekitten.com", "data=body")

print response

print response.status_code