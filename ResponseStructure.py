import requests

response = requests.get("http://placekitten.com/")

print response

print response.status_code

print response.request

print response.url

print response.content

print response.headers