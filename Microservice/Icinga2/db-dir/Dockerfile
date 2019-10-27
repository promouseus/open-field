#DB-DIR
FROM mariadb:latest

ADD https://raw.githubusercontent.com/Icinga/icingaweb2-module-director/master/schema/mysql.sql /docker-entrypoint-initdb.d/
RUN /bin/chmod o+r /docker-entrypoint-initdb.d/*