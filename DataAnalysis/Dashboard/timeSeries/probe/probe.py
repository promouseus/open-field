from redistimeseries.client import Client
import os
import time
import subprocess

rts = Client(host="redis", port="6379", db="0")
#rts.create('test', labels={'Time':'Series'})
#TS.CREATE ping:google:dns1:min RETENTION 1209600000 DUPLICATE_POLICY LAST LABELS probe_id 1
#TS.CREATE ping:google:dns1:avg RETENTION 1209600000 DUPLICATE_POLICY LAST LABELS probe_id 1
#TS.CREATE ping:google:dns1:max RETENTION 1209600000 DUPLICATE_POLICY LAST LABELS probe_id 1
#TS.CREATE ping:google:dns1:mdev RETENTION 1209600000 DUPLICATE_POLICY LAST LABELS probe_id 1
#TS.CREATE ping:google:dns1:total RETENTION 1209600000 DUPLICATE_POLICY LAST LABELS probe_id 1
#TS.CREATE ping:google:dns1:loss RETENTION 1209600000 DUPLICATE_POLICY LAST LABELS probe_id 1
# Key names: https://redis.io/topics/data-types-intro
#1209600000 # 14 days

def ping(server='8.8.8.8', count=3, deadline=1, preload=3, pattern="c2ab70726f6d6f75736575732e696f2ec2bb"):

    cmd = "ping -c {} -w {} -l {} -p {} {}".format(count, deadline, preload, pattern, server).split(' ')
    #print(cmd)
    try:
        output = subprocess.check_output(cmd).decode().strip()
        lines = output.split("\n")
        total = lines[-2].split(',')[3].split()[1]
        loss = lines[-2].split(',')[2].split()[0]
        timing = lines[-1].split()[3].split('/')
        return {
            'type': 'rtt',
            'min': timing[0],
            'avg': timing[1],
            'max': timing[2],
            'mdev': timing[3],
            'total': total,
            'loss': loss,
        }
    except Exception as e:
        print(e)
        return None


while 1:
    results = ping()
    #print(results)
    rts.add('ping:google:dns1:min', '*', results['min'])
    rts.add('ping:google:dns1:avg', '*', results['avg'])
    rts.add('ping:google:dns1:max', '*', results['max'])
    rts.add('ping:google:dns1:mdev', '*', results['mdev'])
    rts.add('ping:google:dns1:total', '*', results['total'].removesuffix('ms'))
    rts.add('ping:google:dns1:loss', '*', results['loss'].removesuffix('%'))
    time.sleep(1)
