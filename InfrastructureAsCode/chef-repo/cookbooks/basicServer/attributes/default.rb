default['snmp']['packages'] = case node['platform_family']
                              when 'debian'
                                %w[snmp snmpd]
                              else
                                %w[net-snmp net-snmp-utils]
                              end

# Same on supported platforms:
# redhat, centos, fedora, scientific, debian, ubuntu
default['snmp']['service'] = 'snmpd'
default['snmp']['conffile'] = '/etc/snmp/snmpd.conf'
default['snmp']['syslocationVirtual'] = 'Virtual Server'
default['snmp']['syslocationPhysical'] = 'Server Room'
default['snmp']['syscontact'] = 'Root <root@localhost>'
default['snmp']['sysname'] = node['fqdn']

default['snmp']['process_monitoring']['proc'] = []
default['snmp']['process_monitoring']['procfix'] = []

default['snmp']['include_all_disks'] = false
default['snmp']['all_disk_min'] = 100 # 100K
default['snmp']['disks'] = [{ mount: '/', min: '10%' }]
default['snmp']['load_average'] = { max1: '24', max5: '12', max15: '6' }

# Debian default file options
default['snmp']['snmpd']['pass'] = {}
default['snmp']['snmpd']['pass_persist'] = {}
default['snmp']['snmpd']['snmpd_run'] = 'yes'
default['snmp']['snmpd']['snmpd_opts'] = '-Lsd -Lf /dev/null -u snmp -g ' \
    'snmp -I -smux -p /var/run/snmpd.pid'
default['snmp']['snmpd']['trapd_run'] = 'no'
default['snmp']['snmpd']['trapd_opts'] = '-Lsd -p /var/run/snmptrapd.pid'
default['snmp']['snmpd']['snmpd_compat'] = 'yes'
default['snmp']['snmpd']['mibdirs'] = '/usr/share/snmp/mibs'
default['snmp']['snmpd']['mibs'] = nil

default['snmp']['v3user'] = 'user3'
default['snmp']['v3pass'] = 'user3password'
default['snmp']['v3key'] = 'user3encryption'

# ntp
default['ntp']['packages'] = case node['platform_family']
                             when 'rhel'
                               %w[ntp ntpdate]
                             else
                               %w[ntp]
                             end

default['ntp']['servers'] = [
  '0.pool.ntp.org',
  '1.pool.ntp.org',
  '2.pool.ntp.org',
  '3.pool.ntp.org'
]
