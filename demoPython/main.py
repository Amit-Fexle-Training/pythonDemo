import os
from simple_salesforce import Salesforce, format_soql
from pprint import pprint
from datetime import datetime
import configparser
import warnings
import time
import pandas as pd
import json

OrgCreds = configparser.ConfigParser()
OrgCreds.read('config.ini')

username = OrgCreds.get('my_credentials', 'username')
password = OrgCreds.get('my_credentials', 'password')
security_token = OrgCreds.get('my_credentials', 'security_token')
domain = OrgCreds.get('my_credentials', 'domain')

# Establish a connection to your Salesforce instance
print('Establish a connection to your Salesforce instance')
sf = Salesforce(username=username, password=password, security_token= security_token, domain= domain)
print('Connection Established')

result = sf.query_all("SELECT Id, Name, Email FROM Contact")
print(pd.DataFrame(result))
records = result['records']
for record in records:
    print(f"Id: {record['Id']}, Name: {record['Name']}, Email: {record['Email']}")

