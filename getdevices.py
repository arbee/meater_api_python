from meater import Meater

device_data = Meater().get_devices()

if device_data['data']['devices']:
  devices = (device for device in device_data['data']['devices'])

  for device in devices:
    temp_internal = device['temperature']['internal']
    temp_ambient = device['temperature']['ambient']
    print(f"Device ID {device['id']}")
    print(f"\tInternal temp: {temp_internal:.2f}")
    print(f"\tAmbient temp: {temp_ambient:.2f}")
    if device['cook']:
      print(f"Current cook: {device['cook']['name']}")
      print(f"\tTarget temp: {round(device['cook']['temperature']['target'])}")
      print(f"\tPeak temp: {device['cook']['temperature']['peak']:.2f}")
      print(f"\tElapsed time: {device['cook']['time']['elapsed']}")
      print(f"\tRemaining time: {device['cook']['time']['remaining']}")
else:
  print("No devices currently connected")