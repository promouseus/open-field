LABEL org.opencontainers.image.authors="input@00010110.nl"
FROM httpd:alpine
VOLUME /usr/local/apache2/md

COPY httpd-ssl.conf conf/extra/httpd-ssl.conf
COPY httpd.conf conf/httpd.conf
COPY c2it.py cgi-bin/c2it

RUN chmod +x cgi-bin/c2it
RUN chown www-data:www-data cgi-bin/c2it

#RUN sed -i \
#        -e 's/^#\(Include .*httpd-ssl.conf\)/\1/' \
#		-e 's/^#\(LoadModule .*mod_ssl.so\)/\1/' \
#		-e 's/^#\(LoadModule .*mod_socache_shmcb.so\)/\1/' \
#        -e 's/^#\(LoadModule .*mod_http2.so\)/\1/' \
#        -e 's/^#\(LoadModule .*mod_watchdog.so\)/\1/' \
#        -e 's/^#\(LoadModule .*mod_md.so\)/\1/' \
#        -e 's/^#ServerName .*/ServerName webserver:80/g' \
#		conf/httpd.conf

RUN apk --no-cache add python3

#RUN \
#    apk --no-cache add sudo && \
#    echo 'www-data ALL=(root) NOPASSWD: /usr/local/apache2/bin/apachectl graceful' >> /etc/sudoers.d/apachectl

EXPOSE 443
# FROM image also EXPOSES 80