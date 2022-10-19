import requests
import json
from secret import APIKEY

url = 'https://dunwoody.instructure.com/api/v1/courses'
bearer = 'Bearer ' + APIKEY
headers = {'Authorization': bearer}
response = requests.get(url, headers=headers)
print('My courses:')
data = json.loads(response.content)
for course in data:
    print(course['name'])