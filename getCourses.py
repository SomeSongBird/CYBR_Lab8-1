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
    col = list(course.keys())[1]
    print(course[col])