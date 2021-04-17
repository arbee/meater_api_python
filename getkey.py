"""Utility script to fetch access token and attempt to save it to the .env"""
import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

if os.getenv('MEATER_KEY'):
  print("Key already exists. If this key no longer works delete the MEATER_KEY line from your .env file and run this script again.")
  quit()
  
dataobj = '{"email": "' + os.getenv('MEATER_EMAIL') + '", "password": "' + os.getenv('MEATER_PASSWORD') + '"}'


key_request = requests.post(os.getenv('MEATER_URL') + '/login', data=dataobj, headers={'Content-Type': 'application/json'})

if key_request.status_code == 200:
  key_data = json.loads(key_request.text)
  try:
    with open('.env', 'a') as varsfile:
      varsfile.write(f"\nMEATER_KEY={key_data['data']['token']}")
  except:
    print("Could not automatically write the token to your .env file.")
    print("Use output below to add METER_KEY=<key value> to the file.")
    print(key_request.text)
else:
  print("An error occurred. Check your Meater account credentials.")
