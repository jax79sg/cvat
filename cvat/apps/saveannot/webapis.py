import json
import requests
from requests.auth import HTTPBasicAuth

api_url_base = 'http://localhost:8080/api/v1/'
user = 'admin'
password = 'admin'


def getListOfTasks():
    api_url=api_url_base+"tasks?format=json"
    headers = {'Content-Type': 'application/json'}
    response = requests.get(api_url, headers=headers,  auth=HTTPBasicAuth(user, password))
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

