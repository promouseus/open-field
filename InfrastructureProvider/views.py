from django.shortcuts import render
from django.conf import settings  # import secret for LeaseWeb API
import urllib.request
import json

# Create your views here.
def index(request):

    req = urllib.request.Request('https://api.leaseweb.com/v1/bareMetals')
    req.add_header('X-Lsw-Auth', settings.SECRET_LEASEWEB)
    #r = urllib.request.urlopen(req)

    r = ""
    with urllib.request.urlopen(req) as f:
        r += f.read().decode('utf-8')
    r = json.loads(r)

    context = {
        'leaseweb_string': r['bareMetals'],
    }
    return render(request, 'InfrastructureProvider/index.html', context)



'''
OLD Python2 code, rewrite to above Python3 code from httplib to urllib also

#import httplib
#import json
#from conf import LeasewebApiKey

# Request: LeaseWeb API (https://api.leaseweb.com/v1/bareMetals)
connection = httplib.HTTPSConnection('api.leaseweb.com')

#Set debug output bool
connection.set_debuglevel(1)

# Headers
headers = LeasewebApiKey

# Send synchronously
connection.request('GET', '/v1/bareMetals', None, headers)
try:
    response = connection.getresponse()
    #TODO: check if result is json before doing this
    bareMetal = json.loads(response.read())
    # Success
    print('Response status and reason ' + str(response.status) + ' ' + str(response.reason))
except httplib.HTTPException, e:
    # Exception
    print('Exception during request')

#Example output JSON
#print json.dumps(bareMetal, sort_keys=True, indent=4)
#    "bareMetals": [
#        {
#            "bareMetal": {
#                "bareMetalId": "195591",   #JWZF010 = 195604
#                "reference": null,
#                "serverName": "JWZF001",
#                "serverType": "Bare Metal"
#            }
#        },
for jef in bareMetal['bareMetals']:
    print jef['bareMetal']['serverName']

connection.request('GET', '/v1/bareMetals/195591/rootPassword.json', None, headers)
try:
    response = connection.getresponse()
    #TODO: check if result is json before doing this
    rootPass = json.loads(response.read())
    # Success
    print('Response status and reason ' + str(response.status) + ' ' + str(response.reason))
except httplib.HTTPException, e:
    # Exception
    print('Exception during request')

print rootPass['rootPassword']

connection.request('GET', '/v1/bareMetals/195604/installationStatus', None, headers)
try:
    response = connection.getresponse()
    #TODO: check if result is json before doing this
    osstatus = json.loads(response.read())
    # Success
    print('Response status and reason ' + str(response.status) + ' ' + str(response.reason))
except httplib.HTTPException, e:
    # Exception
    print('Exception during request')

print osstatus

connection.request('GET', '/v1/bareMetals/195604/switchPort', None, headers) #add /open or /close to enable or disable port
try:
    response = connection.getresponse()
    #TODO: check if result is json before doing this
    switch = json.loads(response.read())
    # Success
    print('Response status and reason ' + str(response.status) + ' ' + str(response.reason))
except httplib.HTTPException, e:
    # Exception
    print('Exception during request')

print switch

connection.request('GET', '/v1/bareMetals/195604/powerStatus', None, headers) #add /open or /close to enable or disable port
try:
    response = connection.getresponse()
    #TODO: check if result is json before doing this
    powerstatus = json.loads(response.read())
    # Success
    print('Response status and reason ' + str(response.status) + ' ' + str(response.reason))
except httplib.HTTPException, e:
    # Exception
    print('Exception during request')

print powerstatus

connection.request('GET', '/v1/bareMetals/195604/ips', None, headers) #add /open or /close to enable or disable port
try:
    response = connection.getresponse()
    #TODO: check if result is json before doing this
    ip = json.loads(response.read())
    # Success
    print('Response status and reason ' + str(response.status) + ' ' + str(response.reason))
except httplib.HTTPException, e:
    # Exception
    print('Exception during request')

print ip


#Create postheader and combine it with the normal header
postHeader = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
postHeader.update(headers)

connection.request('PUT', '/v1/bareMetals/195604/ips/85.17.25.77', "reverseLookup=my.domain.nl&nullRouted=0", postHeader) #add /open or /close to enable or disable port
try:
    response = connection.getresponse()
    #TODO: check if result is json before doing this
    ipUpdate = json.loads(response.read())
    # Success
    print('Response status and reason ' + str(response.status) + ' ' + str(response.reason))
except httplib.HTTPException, e:
    # Exception
    print('Exception during request')

print ipUpdate

connection.request('GET', '/v1/bareMetals/195604?billing=1&details=1', None, headers) #add /open or /close to enable or disable port
try:
    response = connection.getresponse()
    #TODO: check if result is json before doing this
    details2 = json.loads(response.read())
    # Success
    print('Response status and reason ' + str(response.status) + ' ' + str(response.reason))
except httplib.HTTPException, e:
    # Exception
    print('Exception during request')

print details2

connection.request('PUT', '/v1/bareMetals/195604', "reference=name", postHeader) #add /open or /close to enable or disable port
try:
    response = connection.getresponse()
    #TODO: check if result is json before doing this
    detailsUpdate = json.loads(response.read())
    # Success
    print('Response status and reason ' + str(response.status) + ' ' + str(response.reason))
except httplib.HTTPException, e:
    # Exception
    print('Exception during request')

print detailsUpdate

connection.close()
'''
