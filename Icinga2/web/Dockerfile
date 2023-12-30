#Web
FROM httpd:alpine
#ADD . /code
#WORKDIR /code
RUN apk add --no-cache icingaweb2

# Configure webserver for Icingaweb2
# TODO: create entrypoint script with ENV's for this
# TODO: Place FilesMatch and DirecoryIndex between <Directory> in icingaweb2.conf
RUN echo "LoadModule rewrite_module modules/mod_rewrite.so" > /usr/local/apache2/conf/icingaweb2.conf \
    && echo "LoadModule proxy_module modules/mod_proxy.so" >> /usr/local/apache2/conf/icingaweb2.conf \
    && echo "LoadModule proxy_fcgi_module modules/mod_proxy_fcgi.so" >> /usr/local/apache2/conf/icingaweb2.conf \
    # Enable basic auth passtry to FPM backend (web/director API)
    && echo "SetEnvIf Authorization \"(.*)\" HTTP_AUTHORIZATION=$1" >> /usr/local/apache2/conf/icingaweb2.conf \
    && echo "<FilesMatch \.php$>" >> /usr/local/apache2/conf/icingaweb2.conf \
    && echo "SetHandler "proxy:fcgi://php:9000"" >> /usr/local/apache2/conf/icingaweb2.conf \
    && echo "</FilesMatch>" >> /usr/local/apache2/conf/icingaweb2.conf \
    && echo "DirectoryIndex index.php" >> /usr/local/apache2/conf/icingaweb2.conf \
    && icingacli setup config webserver apache >> /usr/local/apache2/conf/icingaweb2.conf \
    && echo "Include conf/icingaweb2.conf" >> /usr/local/apache2/conf/httpd.conf \
    # Forward root page to icingaweb2 subfolder
    && echo '<html><head><meta http-equiv="refresh" content="0; url=./icingaweb2" /></head><body>Forwarding to <a href="icingaweb2/">Icinga2web</a></body></html>' > /usr/local/apache2/htdocs/index.html

# Configure Icingaweb2
# TODO: create entrypoint script with ENV's for this? Currently comming from directory

RUN /bin/mkdir /etc/icingaweb2/enabledModules \
    && /bin/ln -s /usr/share/webapps/icingaweb2/modules/monitoring /etc/icingaweb2/enabledModules/monitoring
# Install perf module
RUN /usr/bin/install -d -m 0755 /usr/share/webapps/icingaweb2/modules/graphite \
    && /usr/bin/wget -q -O - https://github.com/icinga/icingaweb2-module-graphite/archive/v1.1.0.tar.gz | tar xfz - -C /usr/share/webapps/icingaweb2/modules/graphite --strip-components 1 \
    && /bin/ln -s /usr/share/webapps/icingaweb2/modules/graphite /etc/icingaweb2/enabledModules/graphite

ADD setup /etc/icingaweb2
RUN chown www-data:www-data /etc/icingaweb2/ -R
# TODO: remoce secret file in etc/icingaweb2 as it's not needed due to automated install
# TODO: check if config is working automatically (no need to config backends in GUI), ADD seems not to work completed ly (some config files not there): change to copy

# Install Director
#ADD https://github.com/Icinga/icingaweb2-module-director/archive/master.zip /usr/share/webapps/icingaweb2/modules
#RUN cd /usr/share/webapps/icingaweb2/modules \
#    && /usr/bin/unzip master.zip \
#    && /bin/mv icingaweb2-module-director-master director \
#    && /bin/ln -s /usr/share/webapps/icingaweb2/modules/director /etc/icingaweb2/enabledModules/director

##ADD kickstart.ini > /etc/icingaweb2/modules/director/kickstart.ini 
##RUN apk add curl
##RUN apk add php-curl
# Test API: curl -k -s -u root:1b1205c44c11c395 'https://master:5665/v1'
#RUN icingacli director kickstart run

#RUN echo "[global]" > /etc/icingaweb2/config.ini \
#    && echo "show_stacktraces = \"0\"" >> /etc/icingaweb2/config.ini \
#    && echo "config_backend = \"db\"" >> /etc/icingaweb2/config.ini \
#    && echo "config_resource = "icinga2web_db"" {" >> /etc/icingaweb2/config.ini \
#    && echo "object IdoMysqlConnection \"ido-mysql\" {" >> /etc/icingaweb2/config.ini \
#    && echo "object IdoMysqlConnection \"ido-mysql\" {" >> /etc/icingaweb2/config.ini \
#    && echo "object IdoMysqlConnection \"ido-mysql\" {" >> /etc/icingaweb2/config.ini \
#    && echo "object IdoMysqlConnection \"ido-mysql\" {" >> /etc/icingaweb2/config.ini \

#icingacli setup token create

### cleanup php from server but keep icingaweb2: how is this going to work with updates?
# /usr/share/webapps # cp -r icingaweb2 icingaweb2app
# cp -R icingaweb2app/* icingaweb2/
# rm -rf icingaweb2app/