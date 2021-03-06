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
    answer = data['answer']

# Get current IP
base_ip = requests.get('https://api.ipify.org?format=json')
if base_ip.status_code == 200:
    ip = base_ip.json()['ip']
else:
    print('ERROR: {}'.format(base_ip.status_code))
    exit(1)

if ip != answer:
    print("INFO: IP has changed to {}, updating...".format(ip))

    # Make a request to the API
    base_url = 'https://api.name.com/v4/domains/{}/records/{}'
    url = base_url.format(domainName, id)

    # Create json data with host, type, answer and ttl
    base_data = { "host": host, "type": type, "answer": ip, "ttl": ttl }
    data = json.dumps(base_data)

    # Make a request to the API
    result = requests.put(url, data=data, auth=HTTPBasicAuth(username, token))
    if result.status_code == 200:
        with open(os.path.join(__location__, 'config.json'), 'w') as outfile:
            data['answer'] = ip
            json.dump(data, outfile, indent=4)

        print(result.json())
    else:
        print('ERROR: {}'.format(result.status_code))
        exit(1)
else:
    print("INFO: IP is the same, no need to update")
