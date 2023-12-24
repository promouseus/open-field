#!/bin/bash
export DOCKER_HOST=tcp://localhost:9001
iotdbCli='docker exec -it iotdb /iotdb/sbin/start-cli.sh -h 127.0.0.1 -p 6667 -u root -pw root'
#iotdbCli='/iotdb/sbin/start-cli.sh -h 127.0.0.1 -p 6667 -u root -pw root'

# Create Time-series
${iotdbCli} -e "set storage group to root.customer"
${iotdbCli} -e "CREATE TIMESERIES root.customer.portal.ipv4.\"8.8.8.8\".rtt WITH DATATYPE=FLOAT, ENCODING=RLE"
${iotdbCli} -e "CREATE TIMESERIES root.customer.portal.ipv4.\"1.1.1.1\".rtt WITH DATATYPE=FLOAT, ENCODING=RLE"

# Create values for Time-series
# requires: apt-get -y install iputils-ping gawk
timestamp=`date +%s%3N`
rtt1=`ping 8.8.8.8 -qc1|tail -n 1|awk -F' ' '{print $4}'|awk -F'/' '{print $1}'`
rtt2=`ping 1.1.1.1 -qc1|tail -n 1|awk -F' ' '{print $4}'|awk -F'/' '{print $1}'`

${iotdbCli} -e "INSERT INTO root.customer.portal.ipv4.\"8.8.8.8\"(timestamp,rtt) values(${timestamp},${rtt1})"
${iotdbCli} -e "INSERT INTO root.customer.portal.ipv4.\"1.1.1.1\"(timestamp,rtt) values(${timestamp},${rtt2})"

# Single line example:
# start-cli.sh -h 127.0.0.1 -p 6667 -u root -pw root -e "INSERT INTO root.open_field(timestamp,status,temperature) values(`date +%s%3N`,false,`ping 8.8.8.8 -qc1|tail -n 1|awk -F' ' '{print $4}'|awk -F'/' '{print $1}'`)"

# Export to CSV
# /iotdb/tools# ./export-csv.sh -h localhost -p 6667 -u root -pw root -td .

#Time,root.customer.portal.ipv4."1.1.1.1".rtt,root.customer.portal.ipv4.text.rtt,root.customer.portal.ipv4."10.20.20.254".rtt,root.customer.portal.ipv4."192.168.0.22".rtt
#2021-12-26T09:59:08.402Z,,19.31,,
#2021-12-26T17:32:29.650Z,,15.68,,
#2021-12-26T17:53:01.538Z,18.93,18.93,,19.7
#2021-12-26T17:53:26.215Z,17.1,17.1,19.47,17.66
#2021-12-26T17:53:33.063Z,16.15,16.15,19.82,16.33


# All files in tree ordered on change date (oldest timeline to the newest)
# find . -name '*-*-*-*-*' -printf "%T@ %p\n"|sort -n|cut -d' ' -f2|xargs -I{} cat {} > /opt/concat.csv

# Add start line to CSV for names:
# Time,root.customerx.nl.custcall.vpbx001.cpu.user,root.customerx.nl.custcall.vpbx001.cpu.nice,root.customerx.nl.custcall.vpbx001.cpu.system,root.customerx.nl.custcall.vpbx001.cpu.idle,root.customerx.nl.custcall.vpbx001.cpu.iowait,root.customerx.nl.custcall.vpbx001.cpu.irq,root.customerx.nl.custcall.vpbx001.cpu.softirq,root.customerx.nl.custcall.vpbx001.cpu.steal,root.customerx.nl.custcall.vpbx001.cpu.guest,root.customerx.nl.custcall.vpbx001.cpu.guest_nice

# docker cp concat.csv iotdb:/
# docker exec -it iotdb /bin/bash
# export _JAVA_OPTIONS=-Xmx4096m
# import-csv.sh -h localhosT -p 6667 -u root -pw root -f /concat.csv