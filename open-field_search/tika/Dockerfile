# syntax=docker/dockerfile:1
# Bases on: https://github.com/apache/iotdb/tree/master/docker/src/main


FROM apache/tika:latest-full
# Install curl for heatlcheck & Dutch OCR

USER root

RUN apt-get -q update; apt-get -qq install curl tesseract-ocr-nld \
  && apt autoremove -y \
  && apt purge --auto-remove -y \
  && apt clean -y

USER nobody

# Enable REST service
#COPY --from=builder /etc/ssl/private/keystore.pkcs12 /iotdb/
#RUN sed -i 's/# enable_rest_service=false/enable_rest_service=true/g' /iotdb/conf/iotdb-rest.properties && \
#    sed -i 's/# rest_service_port=18080/rest_service_port=18080/g' /iotdb/conf/iotdb-rest.properties

# Create self-signed Cert voor REST
# Same setup as builder above (only need builder or line below, both have same error in iotdb: Is directory)
#RUN keytool -genkey -keyalg RSA -alias iotdb -keystore /selfsigned.jks -validity 1000 -keysize 2048 -storepass rootroot --noprompt -dname "CN=open-field.local, OU=open-field, O=Promouseus, C=NL, ST=Noord-Holland, L=Zaanstad, emailAddress=noreply@open-field.local"

#EXPOSE 18080

HEALTHCHECK --interval=10s --timeout=3s \
  CMD curl -f http://localhost:9998/version || exit 1