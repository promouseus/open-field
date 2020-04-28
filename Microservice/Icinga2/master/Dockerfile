#Master
FROM alpine:latest
#ADD . /code
#WORKDIR /code
RUN apk add --no-cache icinga2
RUN /usr/sbin/icinga2 feature enable checker notification
RUN mkdir /run/icinga2
RUN touch /run/icinga2/icinga2.pid
RUN chown icinga:icinga /run/icinga2 -R

#ADD *.conf /etc/icinga2/conf.d/

# Configure master for mysql
# TODO: create entrypoint script with ENV's for this
RUN /usr/sbin/icinga2 feature enable ido-mysql \
    && /bin/cp etc/icinga2/features-available/ido-mysql.conf /etc/icinga2/features-available/ido-mysql.conf.org \
    && echo "library \"db_ido_mysql\"" > /etc/icinga2/features-available/ido-mysql.conf \
    && echo "object IdoMysqlConnection \"ido-mysql\" {" >> /etc/icinga2/features-available/ido-mysql.conf \
    && echo -e "\tuser = \"icinga\"" >> /etc/icinga2/features-available/ido-mysql.conf \
    && echo -e "\tpassword = \"icingapwd\"" >> /etc/icinga2/features-available/ido-mysql.conf \
    && echo -e "\thost = \"db-icinga\"" >> /etc/icinga2/features-available/ido-mysql.conf \
    && echo -e "\tdatabase = \"icinga\"" >> /etc/icinga2/features-available/ido-mysql.conf \
    && echo "}" >> /etc/icinga2/features-available/ido-mysql.conf

# Enable perf (TODO: ENV needed)
RUN /usr/sbin/icinga2 feature enable graphite \
    && echo 'object GraphiteWriter "graphite" {' > /etc/icinga2/features-available/graphite.conf \
    && echo -e "\thost = \"perf\"" >> /etc/icinga2/features-available/graphite.conf \
    && echo -e "\tport = 2003" >> /etc/icinga2/features-available/graphite.conf \
    && echo -e "\tenable_send_thresholds = true" >> /etc/icinga2/features-available/graphite.conf \
    && echo "}" >> /etc/icinga2/features-available/graphite.conf

# vi /etc/icinga2/conf.d/hosts.conf
#icinga2 daemon -C
#icinga2 object list --type Host

# TODO: Move API to satelite? MANUAL run after finish, can't find cert error else
# TODO: Set api-user pass to d545dd08f5d2febb as in commandtransport.ini of web
# icinga2 node wizard (also does API)
#RUN /usr/sbin/icinga2 api setup
### Maybe icinga2 node wizard, setups both API and zone default for Director (only change is contats and NodeName = master?
# port 5665
# root pass in: /etc/icinga2/conf.d/api-users.conf
# Direcotyr needs Endpoint (hostname op container, hashlike now), master (container DNS) and API user/pass

#RUN apk add monitoring-plugins
#CMD ["icinga2", "feature", "list"]
## critical, warning, information, notice and debug
#ENTRYPOINT /usr/sbin/icinga2 -x warning
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
# Backwards compatible link
RUN ln -s /usr/local/bin/docker-entrypoint.sh /
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
#ENTRYPOINT /usr/sbin/icinga2 daemon -x warning
# CMD ["/usr/sbin/icinga2", "daemon", "-x", "warning"]

#Disabled features: api command compatlog debuglog elasticsearch gelf graphite ido-mysql ido-pgsql influxdb livestatus opentsdb perfdata statusdata syslog
#Enabled features: checker mainlog notification
#DAEMON="/usr/sbin/icinga2"
#ICINGA2_ERROR_LOG="/var/log/icinga2/error.log"
#ICINGA2_STARTUP_LOG="/var/log/icinga2/startup.log"
#ICINGA2_LOG="/var/log/icinga2/icinga2.log"
#ICINGA2_CONFIG_FILE="/etc/icinga2/icinga2.conf"
#ICINGA2_RUN_DIR="/run/icinga2"
#ICINGA2_STATE_DIR="/var/cache/icinga2"
#ICINGA2_CMD_DIR="${ICINGA2_RUN_DIR}/cmd"
#ICINGA2_PID_FILE="${ICINGA2_RUN_DIR}/icinga2.pid"
#ICINGA2_DAEMON_ARGS="daemon -c $ICINGA2_CONFIG_FILE -e $ICINGA2_ERROR_LOG -d"