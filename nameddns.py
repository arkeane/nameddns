from re import S
from requests.auth import HTTPBasicAuth
import requests
import json
import os

# Used to reliably get the directory of config.json
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Get data from config.json
with open(os.path.join(__location__, 'config.json')) as json_file:
    data = json.load(json_file)
    username = data['username']
    token = data['token']
    domainName = data['domainName']
    id = data['id']
    host = data['host']
    type =  data['type']
    ttl = data['ttl']

# Get current IP
ip = requests.get('https://api.ipify.org?format=json')
answer = ip.json()['ip']

# Make a request to the API
base_url = 'https://api.name.com/v4/domains/{}/records/{}'
url = base_url.format(domainName, id)

# Create json data with host, type, answer and ttl
base_data = { "host": host, "type": type, "answer": answer, "ttl": ttl }
data = json.dumps(base_data)

# Make a request to the API
result = requests.put(url, data=data, auth=HTTPBasicAuth(username, token))

# Print the result
print(result.json())