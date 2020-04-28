# ELK
Inject UDP syslog as test

cat /var/log/system.log|grep "macbook"|nc 127.0.0.1 5000
zcat < /var/log/system.log.*.gz|grep "macbook"|nc 127.0.0.1 5000

TODO: check if beats has double data from syslog in ELK DB