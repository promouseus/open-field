# syntax=docker/dockerfile:1
# Bases on: https://github.com/apache/iotdb/tree/master/docker/src/main

# Generated (UNSAFE!) self signed SSL so Grafana can run as TLS/H2 always!
#FROM debian AS builder
#RUN apt-get update; apt-get -y install openssl
#RUN openssl req -nodes -newkey rsa:4096 -x509 -keyout /etc/ssl/private/server.key -out /etc/ssl/private/server.crt -days 3654 -subj "/C=NL/ST=Noord-Holland/L=Zaanstad/O=Promouseus/OU=open-field/CN=open-field.local/emailAddress=noreply@open-field.local"
#RUN cat /etc/ssl/private/server.key > /etc/ssl/private/server.pem; cat /etc/ssl/private/server.crt >> /etc/ssl/private/server.pem
#RUN openssl pkcs12 -export -in /etc/ssl/private/server.pem -out /etc/ssl/private/keystore.pkcs12 -password pass:rootroot

FROM apache/iotdb:0.13.0-node
# Install curl for heatlcheck
RUN apt-get -q update; apt-get -qq install curl \
  && apt autoremove -y \
  && apt purge --auto-remove -y \
  && apt clean -y


# Enable REST service
#COPY --from=builder /etc/ssl/private/keystore.pkcs12 /iotdb/
RUN sed -i 's/# enable_rest_service=false/enable_rest_service=true/g' /iotdb/conf/iotdb-rest.properties && \
    sed -i 's/# rest_service_port=18080/rest_service_port=18080/g' /iotdb/conf/iotdb-rest.properties

# Create self-signed Cert voor REST
# Same setup as builder above (only need builder or line below, both have same error in iotdb: Is directory)
#RUN keytool -genkey -keyalg RSA -alias iotdb -keystore /selfsigned.jks -validity 1000 -keysize 2048 -storepass rootroot --noprompt -dname "CN=open-field.local, OU=open-field, O=Promouseus, C=NL, ST=Noord-Holland, L=Zaanstad, emailAddress=noreply@open-field.local"

EXPOSE 18080

HEALTHCHECK --interval=10s --timeout=3s \
  CMD curl -f http://localhost:18080/ping || exit 1