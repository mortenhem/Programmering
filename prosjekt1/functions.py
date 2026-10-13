import os
from dotenv import load_dotenv
import keyring
import requests
import sys
import json


def get_env_property(name):
	load_dotenv()
	apikey = os.getenv(name.upper())
	
	if not apikey:
		print("Not found")
		return ""
	return apikey

def get_secret(app, name):

	key = keyring.get_password(app, name)
	if not key:
		print("Not found.")
		return ""
	return key

def get_request(url, headers):

	response = requests.get(url, headers=headers)
	
	if response.status_code == 200:
		data = response.text
		return json.loads(response.text)
	else:
		raise SystemError(f"Failed to retrieve data. Status code {response.status_code}")

