__author__ = 'Promouseus'

import httplib
import json
from conf import LeasewebApiKey

# Request: LeaseWeb API (https://api.leaseweb.com/v1/bareMetals)
connection = httplib.HTTPSConnection('api.leaseweb.com')

# Headers
headers = LeasewebApiKey

# Send synchronously
connection.request('GET', '/v1/bareMetals', None, headers)
try:
    response = connection.getresponse()
    #TODO: check if result is json before doing this
    bareMetal = json.loads(response.read())
    # Success
    print('Response status ' + str(response.status))
except httplib.HTTPException, e:
    # Exception
    print('Exception during request')

print bareMetal