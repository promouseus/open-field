# LibreNMS API

## Force host add (set force to false for real hosts)
curl -X POST -d '{"hostname":"hostx.domain","version":"v3","community":"public", "authlevel":"authPriv", "authname":"userv3", "authpass":"userv3pass","authalgo":"MD5", "cryptopass":"secretX", "cryptoalg":"DES", "force_add":true}' -H 'X-Auth-Token: 64f21c05e0812d129bf16cf0fde09f36' http://localhost:8000/api/v0/devices

## Check if host is already there
curl -H 'X-Auth-Token: 64f21c05e0812d129bf16cf0fde09f36' http://localhost:8000/api/v0/devices/hostx.domain

# Interface Description
Standard groups: Cust, Transit, Peering, Core

Interface description structure: group: description

Example interface description:
```console
Cust: customer XYZ
```

## Network device (general)
For most network devices the description can be set under the (sub)interface configuration. Simply set the decription to "Cust: custom XYZ".

## Ubuntu/Debian
For older Debian/Ubuntu (before netplan) like servers a script needs to be installed:
```console
wget https://raw.githubusercontent.com/librenms/librenms/master/scripts/ifAlias -O /usr/bin/ifAlias
chmod +x /usr/bin/ifAlias
```

Add the following line to snmpd.conf to link it to a snmp(walk) call:
```console
vim /etc/snmp/snmpd.conf
    pass .1.3.6.1.2.1.31.1.1.1.18 /usr/bin/ifAlias
systemctl restart snmpd
```

Add line with interface name and ifAlias to /etc/network/interface:
```console
# eth3: Cust: Example Customer
```
echo "$(grep -i "^# enp0s3:" /etc/network/interfaces | sed "s/^# enp0s3: //i")"


Newer files?
wget https://raw.githubusercontent.com/librenms/librenms/f38b1938ad6b98b60af711e1dd9c72293adf3456/scripts/ifAlias -O /usr/bin/ifAlias

# Icinga
curl -k -u root:a089eb37bcf244df -H 'Accept: application/json' \
 -X POST 'https://localhost:5665/v1/actions/process-check-result' \
-d '{ "type": "Service", "filter": "host.name==\"NodeNameA\" && service.name==\"remote-checkje\"", "exit_status": 2, "plugin_output": "PING CRITICAL - Packet loss = 100%", "performance_data": [ "rta=5000.000000ms;3000.000000;5000.000000;0.000000", "pl=100%;80;100;0" ], "check_source": "remote.check.host.dom.ext", "pretty": true }'

curl -k -u root:a089eb37bcf244df -H 'Accept: application/json' \
 -X POST 'https://localhost:5665/v1/actions/process-check-result' \
-d '{ "type": "Service", "filter": "host.name==\"NodeNameA\" && service.name==\"remote-checkje\"", "exit_status": 0, "plugin_output": "PING alive - Packet loss = 0%", "check_source": "remote.check.host.dom.ext", "pretty": true }'

curl -s for silent

#On master
/usr/sbin/icinga2 api setup #repeatble multiple times without effect, at boot before icinga enough!
cat /etc/icinga2/conf.d/api-users.conf  # password

curl -k -u root:a089eb37bcf244df 'https://localhost:5665/v1/objects/hosts'

## With performance data
curl -k -u root:a089eb37bcf244df -H 'Accept: application/json'  -X POST 'https://localhost:5665/v1/actions/process-check-result' -d '{ "type": "Service", "filter": "host.name==\"NodeNameA\" && service.name==\"remote-checkjePassive\"", "exit_status": 0, "plugin_output": "PING alive - Packet loss = 0%", "performance_data": [ "count=7000.000000ms", "Rebootcount=6", "MyPercentage=75%"], "check_source": "remote.check.host.dom.ext", "pretty": true }'


TODO: move settings like API key, pass to env

## API example
{
  object_name: 'AMS-SW01',
  object_type: object,
  address: '192.168.200.32',
  display_name: 'AMS-SW01',
  notes: 'JUNIPER ex2300',
  imports: [
    "Host ICMP up"
  ],
  vars: {
    location: 'AMS-01'
  }
}