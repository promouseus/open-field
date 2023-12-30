#DB-WEB
FROM mariadb:latest

ADD https://raw.githubusercontent.com/Icinga/icingaweb2/master/etc/schema/mysql.schema.sql /docker-entrypoint-initdb.d/
ADD setup/zAdminWebUser.sql /docker-entrypoint-initdb.d/
RUN /bin/chmod o+r /docker-entrypoint-initdb.d/*