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

connection.request('GET', '/v1/bareMetals/195591/rootPassword.json', None, headers)
print rootPass['rootPassword']

connection.request('GET', '/v1/bareMetals/195604/installationStatus', None, headers)
print osstatus

connection.request('GET', '/v1/bareMetals/195604/switchPort', None, headers) #add /open or /close to enable or disable port
print switch

connection.request('GET', '/v1/bareMetals/195604/powerStatus', None, headers)
print powerstatus

connection.request('GET', '/v1/bareMetals/195604/ips', None, headers)
print ip


#Create postheader and combine it with the normal header
postHeader = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
postHeader.update(headers)

connection.request('PUT', '/v1/bareMetals/195604/ips/85.17.25.77', "reverseLookup=my.domain.nl&nullRouted=0", postHeader)
print ipUpdate

connection.request('GET', '/v1/bareMetals/195604?billing=1&details=1', None, headers)
print details2

connection.request('PUT', '/v1/bareMetals/195604', "reference=name", postHeader)
print detailsUpdate
'''
