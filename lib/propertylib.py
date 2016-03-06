'''Application property setter for a single
base-code with multiple appengine projects.
'''

import json
import os

__author__ = 'me@digyter.com (Mark Angelo Libantino)'

class Properties(object):
  '''Class object of creating and getting list of
  property of each appengine project

  To use:
  PROPERTIES = Properties().get_or_create()
  '''
  properties = {}

  def __init__(self):
    '''Instantiates property object based on application
    id of the running project
    '''
    self.application_id = os.environ['APPLICATION_ID']
    shard_index = self.application_id.find('~')
    if shard_index != -1:
      self.application_id = self.application_id[shard_index+1:]
    if self.application_id == 'None':
      raise RuntimeError('Please declare application id in app.yaml.')


  def get(self):
    '''Gets content of property file
    Returns:
      results: Application properties in a json object
    '''
    path = os.path.dirname(os.path.abspath(__file__))
    filename = '{0}.{1}'.format(self.application_id, 'json')
    path = os.path.abspath(os.path.join(path, '../', 'properties', filename))
    if not os.path.exists(path):
      raise RuntimeError(path + " doesn't exists.")
    else:
      properties = ''
      with open(path) as property_file:
        for line in property_file:
          properties += line
      results = json.loads(properties)
      return results
