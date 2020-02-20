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

# With performance data
curl -k -u root:a089eb37bcf244df -H 'Accept: application/json'  -X POST 'https://localhost:5665/v1/actions/prcess-check-result' -d '{ "type": "Service", "filter": "host.name==\"NodeNameA\" && service.name==\"remote-checkjePassive\"", "exit_status": 0, "plugin_output": "PING alive - Packet loss = 0%", "performance_data": [ "count=7000.000000ms", "Rebootcount=6", "MyPercentage=75%"], "check_source": "remote.check.host.dom.ext", "pretty": true }'


