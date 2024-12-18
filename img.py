import requests
import pprint

response= requests.get('https://api.github.com')

print(response.text)
response_json =response.json()
pprint.pprint(response_json)