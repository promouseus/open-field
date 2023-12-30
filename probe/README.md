NaniPi-Neo2

# http://wiki.friendlyarm.com/wiki/index.php/FriendlyCore_(based_on_ubuntu-core_with_Qt)#How_to_Install_Docker_4
sudo apt-get update
sudo apt-get upgrade
sudo apt-get autoremove
sudo apt-get install docker.io docker-compose

#docker pull amazonlinux

version: '2.0'
services:
  aws-linux:
    image: amazonlinux:latest
    command: bash -c "/usr/bin/yum -y update; /usr/bin/yum -y install iputils; /usr/bin/ping 192.168.2.1"
    ports:
    - "2222:22"

docker run -it amazonlinux:latest /bin/bash

Amazon A1. Are ARM instances

docker logs --follow --timestamps 65a0d4fc8589

Json logs: /var/lib/docker/containers/


sudo apt-get install --install-recommends linux-generic-hwe-18


# MTU check
ping 178.22.232.1 -s 1462 -t 10
	PING 178.22.232.1 (178.22.232.1) 1462(1490) bytes of data.
	From 192.168.178.1 icmp_seq=1 Frag needed and DF set (mtu = 1460)

ping 213.51.1.124 -s 1472 -M do
	PING 213.51.1.124 (213.51.1.124) 1472(1500) bytes of data.
	From 192.168.178.1 icmp_seq=1 Frag needed and DF set (mtu = 1460)
	ping: local error: Message too long, mtu=1460

# Timestamp packet (mostly only internal network)
ping 192.168.178.1 -s 1462 -t 10 -T tsandaddr
	PING 192.168.178.1 (192.168.178.1) 1462(1530) bytes of data.
	1470 bytes from 192.168.178.1: icmp_seq=1 ttl=63 time=3.62 ms
	TS: 	192.168.86.166	27903373 absolute
		192.168.86.1	301
		192.168.178.1	7197396
		192.168.178.1	0
	Unrecorded hops: 2

ping 192.168.178.1 -s 1462 -t 10 -T tsonly
	PING 192.168.178.1 (192.168.178.1) 1462(1530) bytes of data.
	1470 bytes from 192.168.178.1: icmp_seq=1 ttl=63 time=3.47 ms
	TS: 	27919686 absolute
		301
		7197393
		0
		-7197390
		-301

# interval 0.2 (as fast as possible send, lower then 0.2 needs super-user)
ping 192.168.86.1 -s 1500 -i 0.2 

# 16 byte padding in hex of “ThisIsPromouseus” 54686973497350726f6d6f7573657573
ping 192.168.86.1 -p 54686973497350726f6d6f7573657573
“«promouseus.io.»” c2ab70726f6d6f75736575732e696f2ec2bb
ping 192.168.86.1 -p c2ab70726f6d6f75736575732e696f2ec2bb

# Future add QoS ping -Q to compare results for different queu’s and settings. Can also set stuff like: minimal cost, reliability, throughput, low delay

# pipe (parallel packets, preload send x without waiting for reply) -l 1 or -l 3 (more then 3 is super-user)

# Record route:
# ping 192.168.178.1 -R
PING 192.168.178.1 (192.168.178.1) 56(124) bytes of data.
	64 bytes from 192.168.178.1: icmp_seq=1 ttl=63 time=2.17 ms
	RR: 	192.168.86.166
		192.168.178.254
		192.168.178.1
		192.168.178.1
		192.168.86.1
		192.168.86.166

	64 bytes from 192.168.178.1: icmp_seq=2 ttl=63 time=1.83 ms	(same route)
	64 bytes from 192.168.178.1: icmp_seq=3 ttl=63 time=1.92 ms	(same route)


Docker kill / stop (same effect, no ping wrap up for proc ID 1)

# First finds PID for docker proces on hypervisor/OS, seconds enters the namespace and sends SIGINT
PID=$(docker inspect --format {{.State.Pid}} <container_name_or_ID>)
nsenter --target $PID --mount --uts --ipc --net --pid kill -SIGINT <PID of your program inside your container>




# Docker API
curl --unix-socket /var/run/docker.sock http:/v1.40/containers/json