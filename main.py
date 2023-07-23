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
source_sf = Salesforce(username=username, password=password, security_token= security_token, domain= domain)
print('Connection Established')

