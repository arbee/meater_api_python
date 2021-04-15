"""Utility functions for Meater API"""
import datetime


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