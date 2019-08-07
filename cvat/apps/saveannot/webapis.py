import json
import requests
from requests.auth import HTTPBasicAuth
from xml.dom import minidom


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

def getTaskAnnotationXML(taskid):
    api_url=api_url_base+"tasks/"+taskid+"/annotations/" + taskid+ "?format=CVAT XML 1.1 for videos&action=download"
    headers = {'Content-Type': 'application/json'}
    response = requests.get(api_url, headers=headers,  auth=HTTPBasicAuth(user, password))
    
    while response.status_code == 202:
        response = requests.get(api_url, headers=headers,  auth=HTTPBasicAuth(user, password))
    if response.status_code == 200:
        xmlString=response.content.decode('utf-8')
        return minidom.parseString(xmlString), xmlString
    else:
        return None
        
def getTaskAnnotationXMLforImages(taskid):
    api_url=api_url_base+"tasks/"+taskid+"/annotations/" + taskid+ "?format=CVAT XML 1.1 for images&action=download"
    headers = {'Content-Type': 'application/json'}
    response = requests.get(api_url, headers=headers,  auth=HTTPBasicAuth(user, password))
    
    while response.status_code == 202:
        response = requests.get(api_url, headers=headers,  auth=HTTPBasicAuth(user, password))
    if response.status_code == 200:
        xmlString=response.content.decode('utf-8')
        return minidom.parseString(xmlString), xmlString
    else:
        return None