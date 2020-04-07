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