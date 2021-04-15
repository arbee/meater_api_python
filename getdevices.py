import os
import requests
import json
from dotenv import load_dotenv
import utils
load_dotenv()

key = os.getenv('MEATER_KEY')


devices_request = requests.get(os.getenv('MEATER_URL') + '/devices', headers={'Authorization': 'Bearer {}'.format(key)})
device_data = json.loads(devices_request.text)

if device_data['data']['devices']:
  devices = (device for device in device_data['data']['devices'])

  for device in devices:
    temp_internal = utils.c_to_f(device['temperature']['internal'])
    temp_ambient = utils.c_to_f(device['temperature']['ambient'])
    print("Device ID {}".format(device['id']))
    print(f"\tInternal temp: {temp_internal:.2f}")
    print(f"\tAmbient temp: {temp_ambient:.2f}")
    if device['cook']:
      print(f"Current cook: {device['cook']['name']}")
      print(f"\tTarget temp: {round(utils.c_to_f(device['cook']['temperature']['target']))}")
      print(f"\tPeak temp: {utils.c_to_f(device['cook']['temperature']['peak']):.2f}")
      print(f"\tElapsed time: {utils.time_format(device['cook']['time']['elapsed'])}")
      print(f"\tRemaining time: {utils.time_format(device['cook']['time']['remaining'])}")
else:
  print("No devices currently connected")