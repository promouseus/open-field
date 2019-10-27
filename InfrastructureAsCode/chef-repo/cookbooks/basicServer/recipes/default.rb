#
# Cookbook:: basicServer
# Recipe:: default
#
# Copyright:: 2019, The Authors, All Rights Reserved.

execute 'debian7_repoFix' do
  command 'printf "deb http://archive.debian.org/debian/ ' \
        'wheezy main non-free contrib\n' \
    'deb-src http://archive.debian.org/debian/ ' \
        'wheezy main non-free contrib\n' \
    'deb http://archive.debian.org/debian-security/ ' \
        'wheezy/updates main non-free contrib\n' \
    'deb-src http://archive.debian.org/debian-security/ ' \
        'wheezy/updates main non-free contrib\n" ' \
    '> /etc/apt/sources.list; ' \
    'echo "Acquire::Check-Valid-Until false;" |' \
        'tee -a /etc/apt/apt.conf.d/10-nocheckvalid;' \
    'apt-get update;'
  only_if do
    node['platform'].include?('debian') &&
      node['platform_version'].to_i >= 7 &&
      node['platform_version'].to_i < 8
  end
end

node['snmp']['packages'].each do |snmppkg|
  package snmppkg
end

template '/etc/default/snmpd' do
  mode '0644'
  owner 'root'
  group 'root'
  only_if { node['platform_family'] == 'debian' }
end

service node['snmp']['service'] do
  action %i[start enable]
end

template node['snmp']['conffile'] do
  source 'snmpd.conf.erb'
  mode '0600'
  owner 'root'
  group 'root'
  notifies :restart, "service[#{node['snmp']['service']}]"
end

# NTP
execute 'debian10_repoUpdate' do
  command 'apt-get update'
  only_if do
    node['platform'].include?('debian') &&
      node['platform_version'].include?('buster')
  end
end

node['ntp']['packages'].each do |ntppkg|
  package ntppkg do
    action :install
  end
end
