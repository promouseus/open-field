#db-librenms:
#  environment:
#    - MYSQL_DATABASE=librenms
#    - MYSQL_PASSWORD=librenms
#    - MYSQL_ROOT_PASSWORD=password
#    - MYSQL_USER=librenms
#  image: 'mariadb:latest'
#  volumes:
#    - '/opt/docker_data/db/librenms-config:/etc/mysql/conf.d'
#    - '/opt/docker_data/db/librenms:/var/lib/mysql'
#memcached-librenms:
#  image: 'memcached:alpine'
#oxidized-librenms:
#  image: 'oxidized/oxidized:latest'
#web-librenms:
#  environment:
#    - LIBRENMS_db_host=db-librenms
#    - LIBRENMS_db_pass=librenms
#    - LIBRENMS_db_user=librenms
#  image: 'repoX/noc:librenms'
#  links:
#    - db-librenms
#    - memcached-librenms
#    - oxidized-librenms
#  ports:
#    - '80:80'
#    - '9955:9955/udp'
#    - '9956:9956/udp'
#  volumes:
#    - '/opt/docker_data/web/nfsen:/opt/nfsen'
#    - '/opt/docker_data/web/librenms-rrd:/opt/librenms/rrd'


#Junos user for oxidized
#login {
#        class oxidized {
#        permissions view-configuration;
#        allow-commands "show configuration.*|quit";
#        deny-commands .*;
#    }
#    user oXidiZeD {
#        full-name "Oxidixed User";
#        uid 2222;
#        class oxidized;
#        authentication {
#            encrypted-password ABCDhash
#        }
#    }
#}

##
## TODO: etc/hosts and nfsen need to be done at startup of host


# Ubuntu image from https://hub.docker.com/_/ubuntu/
FROM ubuntu:16.04
LABEL maintainer "no-reply@promouseus.io"

# To supress messages with apt-get like:
# debconf: unable to initialize frontend: Dialog
# debconf: (TERM is not set, so the dialog frontend is not usable.)
# debconf: falling back to frontend: Readline
ENV DEBIAN_FRONTEND=noninteractive

# Install and configure LibreNMS based on: http://docs.librenms.org/Installation/Installation-Ubuntu-1604-Apache/
RUN apt-get -q update \
  && apt-get -q -y install \
    libapache2-mod-php7.0 \
    php7.0-cli \
    php7.0-mysql \
    php7.0-gd \
    php7.0-snmp \
    php-pear \
    php7.0-curl \
    snmp \
    cron \
    graphviz \
    php7.0-mcrypt \
    php7.0-json \
    apache2 \
    fping \
    imagemagick \
    whois \
    mtr-tiny \
    nmap \
    python-mysqldb \
    snmpd \
    php-net-ipv4 \
    php-net-ipv6 \
    rrdtool \
    git

# cleaning data after X days
#$config['syslog_purge']                                   = 30;
#$config['eventlog_purge']                                 = 30;
#$config['authlog_purge']                                  = 30;
#$config['perf_times_purge']                               = 30;
#$config['device_perf_purge']                              = 30;


#RRDCached
# apt-get install rrdcached
$config['rrdcached']    = "unix:/var/run/rrdcached.sock";
# /etc/default/rrdcached to include:
WRITE_TIMEOUT=1800
WRITE_JITTER=1800
BASE_PATH=/opt/librenms/rrd/
SOCKGROUP=librenms
BASE_OPTIONS="-B -F"
#
# rrdcached service start and on boot
# service apache2 reload

# cron moet nog starten denk ik als service en file er in zetten
# cat /opt/librenms/librenms.nonroot.cron >> /etc/crontab
# apt-get -y install rsyslog
# service rsyslog start
# service cron start
# log in cat /var/log/syslog |grep CRON
# Let op: werkt niet samen met nfsen plugin ('error on creating graphs')


# php ini time zone
# echo 'date.timezone = "UTC"' >> /etc/php/7.0/cli/php.ini
# echo 'date.timezone = "UTC"' >> /etc/php/7.0/apache2/php.ini

#memcached
# apt-get install php-memcached
$config['memcached']['enable']  = true;
$config['memcached']['host']    = "memcached-librenms";
$config['memcached']['port']    = 11211;

#Oxidized
# vim /root/.config/oxidized/config

log: /root/.config/oxidized/logs
rest: 0.0.0.0:8888
source:
  default: http
  debug: true
  http:
    url: http://web-librenms/api/v0/oxidized
    scheme: http
    map:
      name: hostname
      model: os
      group: group
    headers:
      X-Auth-Token: 'authHash'
      Accept: 'application/json'
groups:
  default:
    username: rancid
    password: passwordR
  dataplace:
    username: oXidiZeD
    password: passwordO
output:
  default: git
  git:
    single_repo: true
    user: Oxidized
    email: o@example.com
    repo: "/var/lib/oxidized/devices.git"
model_map:
  cisco: ios
  juniper: junos
  arista_eos: eos


#set user rancid and pass in config

curl -H 'X-Auth-Token: tokenkeyX' http://web-librenms/api/v0/oxidized

##Libre config
$config['oxidized']['enabled']         = TRUE;
$config['oxidized']['url']             = 'http://oxidized-librenms:8888';
$config['oxidized']['group_support'] = true;
$config['oxidized']['default_group'] = 'default';
$config['oxidized']['group']['hostname'][] = array('regex' => '/^dataplace/', 'group' => 'dataplace');
$config['oxidized']['features']['versioning'] = true;
$config['oxidized']['reload_nodes'] = true;

#nfsen
# apt-get install libmailtools-perl nfdump librrds-perl libsocket6-perl
# wget https://downloads.sourceforge.net/project/nfsen/stable/nfsen-1.3.8/nfsen-1.3.8.tar.gz
# tar zxvf nfsen-1.3.8.tar.gz
# cd nfsen-1.3.8
# cp etc/nfsen-dist.conf etc/nfsen.conf
#
## add to etc/nfsen.conf
# $BASEDIR = "/opt/nfsen";
# $HTMLDIR    = "/opt/librenms/html/nfsen/";
# $PREFIX  = '/usr/bin';
# $USER    = "www-data";
# $WWWUSER  = "www-data";
# $WWWGROUP = "www-data";
%sources = (
      'r0'    => { 'port' => '9955', 'col' => '#0000ff', 'type' => 'netflow' },
      'r1'    => { 'port' => '9956', 'col' => '#ff0000', 'type' => 'netflow' },
 );
## ./install.pl etc/nfsen.conf
## chmod g+w /opt/nfsen -R
##  /opt/nfsen/bin/nfsen start ### SET THIS AT BOOT!!!
## config librenms
$config['nfsen_enable'] = 1;
$config['nfsen_rrds'][] = '/opt/nfsen/profiles-stat/live/';
$config['nfsen_split_char']   = '_';
### Problems, check if flow is incomming: tcpdump -n -i any port 9956
# Prolems: conntrack wissen op Hypervisor OS ivm udp flow die al gekopped is aan andere/oude container: apt-get -y install conntrack; conntrack -F

RUN useradd librenms -d /opt/librenms -M -r \
  && usermod -a -G librenms www-data \
  && git clone https://github.com/librenms/librenms.git /opt/librenms \
  && mkdir /opt/librenms/logs \
  && mkdir /opt/librenms/rrd \
  && chmod 775 /opt/librenms/rrd

RUN printf "<VirtualHost *:80>\n\
  DocumentRoot /opt/librenms/html/\n\
  ServerName librenms.example.com\n\
  CustomLog /opt/librenms/logs/access_log combined\n\
  ErrorLog /opt/librenms/logs/error_log\n\
  AllowEncodedSlashes NoDecode\n\
\n\
  <Directory \"/opt/librenms/html/\">\n\
    Require all granted\n\
    AllowOverride All\n\
    Options FollowSymLinks MultiViews\n\
  </Directory>\n\
\n\
</VirtualHost>\n" > /etc/apache2/sites-available/librenms.conf

RUN printf "#!/bin/bash\n\
    if [ ! -f /opt/librenms/config.php ] && [ ! -z \"\$LIBRENMS_db_host\" ] && [ ! -z \"\$LIBRENMS_db_user\" ] && [ ! -z \"\$LIBRENMS_db_pass\" ];\n\
        then\n\
            cp /opt/librenms/config.php.default /opt/librenms/config.php\n\
            sed -i 's/'localhost''/''\$LIBRENMS_db_host'/' /opt/librenms/config.php\n\
            sed -i 's/'USERNAME''/''\$LIBRENMS_db_user'/' /opt/librenms/config.php\n\
            sed -i 's/'PASSWORD''/''\$LIBRENMS_db_pass'/' /opt/librenms/config.php\n\
            cd /opt/librenms\n\
            /usr/bin/php build-base.php\n\
            /usr/bin/php adduser.php jeffrey2 lminow 10 jeffrey@fusix.nl\n\
    fi\n" > /root/LibreNMS.sh\
    && chmod +x /root/LibreNMS.sh

# $config['peeringdb']['enabled'] = true;
## daily update maar manual 1e keer: php daily.php -f peeringdb, after that button on routing that shows peerings on IX's

RUN a2ensite librenms.conf \
  && a2enmod rewrite \
  && a2dissite 000-default \
  && chown -R librenms:librenms /opt/librenms \
  && chmod g+w /opt/librenms

#Use ENV for setting hosting name from stack
#sed -i 's/librenms.example.com/librenms.fusix.net/' jef.txt
#add blabla

#cp config.php.default config.php; sed -i 's/'PASSWORD''/''librenms'/' config.php; cat config.php|grep config
#$config['db_name'] = 'librenms';

EXPOSE 80
#Start WebInterface
CMD ["/usr/sbin/apache2ctl","-D FOREGROUND"]

#Start clean installed and ready to login
#CMD ["/root/libreNMS.sh"]