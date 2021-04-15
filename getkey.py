import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

dataobj = '{"email": "' + os.getenv('MEATER_EMAIL') + '", "password": "' + os.getenv('MEATER_PASSWORD') + '"}'


key_request = requests.post(os.getenv('MEATER_URL') + '/login', data=dataobj, headers={'Content-Type': 'application/json'})

if key_request.status_code == 200:
  key_data = json.loads(key_request.text)
  try:
    print(f"API key: {key_data['data']['token']}")
  except:
    print(key_request.text)
else:
  print("An error occurred. Check your Meater account credentials.")
