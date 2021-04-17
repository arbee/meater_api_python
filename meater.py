"""Main Meater class and supporting functions"""
import os
import requests
from dotenv import load_dotenv
import datetime
load_dotenv()

def c_to_f(temp:float)->float:
  """Convert celsius to fahrenheit

  Args:
      temp (float): temperature in celcius

  Returns:
      float: temperature in fahrenheit
  """
  return (temp * 1.8) + 32


def time_format(time:int)->str:
  """Format the time in seconds to hh:mm:ss

  Args:
      time (int): time, in seconds

  Returns:
      str: formatted time string
  """
  if time == -1:
    return "Estimating..."
  else:
    delta = datetime.timedelta(seconds=time)
    return delta


class Meater():
  """Main Meater class"""
  
  apiurl = os.getenv('MEATER_URL')
  key = os.getenv('MEATER_KEY')
  
  def __init__(self, convert_temp:bool=True):
    """init method

    Args:
        convert_temp (bool, optional): Whether to convert temperatures from 
        Celcius to Fahrenheit. Defaults to True.
    """
    self.convert = convert_temp
    if not os.getenv('MEATER_KEY'):
      print("API key missing")
      quit()
  
  @staticmethod    
  def _output_format(device:object, convert:bool):
    """Private method to format the response from the Meater API"""
    if convert:
      device['temperature']['internal'] = c_to_f(device['temperature']['internal'])
      device['temperature']['ambient'] = c_to_f(device['temperature']['ambient'])
    if device['cook']:
      # format times
      device['cook']['time']['elapsed'] = time_format(device['cook']['time']['elapsed'])
      device['cook']['time']['remaining'] = time_format(device['cook']['time']['remaining'])
      # convert cook temps if applicable
      if convert:
        device['cook']['temperature']['peak'] = c_to_f(device['cook']['temperature']['peak'])
        device['cook']['temperature']['target'] = c_to_f(device['cook']['temperature']['target'])    
    return device


  def get_devices(self)->dict:
    """Get information about all connected Meater probes

    Returns:
        dict: Formatted API response
    """
    req = requests.get(Meater.apiurl + '/devices',
                                   headers={'Authorization': f'Bearer {Meater.key}'}).json()
    for device in req['data']['devices']:
      device = Meater._output_format(device, self.convert)
          
    return req


  def get_device(self, deviceid:str)->dict:
    """Get information for a single probe

    Args:
        deviceid (str): ID of the connected Meater probe

    Returns:
        dict: Formatted API response
    """
    req = requests.get(Meater.apiurl + '/devices/' + deviceid,
                                   headers={'Authorization': f'Bearer {Meater.key}'}).json()
    req['data'] = Meater._output_format(req['data'], self.convert)
    
    return req
