import requests
from requests.auth import HTTPBasicAuth
import json
import sys
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

username = input("Insert Username: ")
token = input("Insert Token: ")

domains = requests.get(url="https://api.name.com/v4/domains", auth=HTTPBasicAuth(username, token))

print("-------------------------------------------------------")
print("Domain list:")
i=0
for domain in domains.json()['domains']:
    print(str(i)+": "+domain['domainName'])
    i+=1

domain_choice = int(input("Insert Domain Number: "))
print("-------------------------------------------------------")
domain = domains.json()['domains'][int(domain_choice)]

records = requests.get(url="https://api.name.com/v4/domains/"+domain['domainName']+"/records", auth=HTTPBasicAuth(username, token))

print("-------------------------------------------------------")
print("Record list:")
i=0
for record in records.json()['records']:
    if record['type'] == "A":
        print(str(i)+": "+record['host']+" "+record['type']+" "+record['answer']+" "+str(record['ttl']))
    i+=1


record_choice = int(input("Insert Record Number: "))
record = records.json()['records'][int(record_choice)]

with open(os.path.join(__location__, 'config.json'), 'w') as outfile:
    base_data = {"username": username,"token": token,"domainName": domain["domainName"],"id": record["id"],"host": record["host"],"type": record["type"], "ttl": record["ttl"], "answer": record["answer"]}
    json.dump(base_data, outfile, indent=4)

print("data saved to config.json")
