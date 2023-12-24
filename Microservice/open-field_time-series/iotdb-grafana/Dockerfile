# syntax=docker/dockerfile:1
FROM maven:3-openjdk-11-slim AS builder
ENV version=v0.12.2
WORKDIR /
RUN apt-get -q update; apt-get -qq install git \
    && git -c advice.detachedHead=false clone https://github.com/apache/iotdb.git --branch ${version} \
    && cd iotdb \
    && mvn --quiet clean package -pl grafana -am -Dmaven.test.skip=true

FROM openjdk:11-jre-slim
RUN apt-get -q update; apt-get -qq install curl \
  && apt autoremove -y \
  && apt purge --auto-remove -y \
  && apt clean -y

WORKDIR /iotdb-grafana
COPY --from=builder /iotdb/grafana/target/iotdb-grafana-*.war iotdb-grafana.war
COPY --from=builder /iotdb/grafana/src/main/resources/application.properties .

# Application.properties needs 127.0.0.1 changed to iotdb
RUN sed -i 's/127.0.0.1/iotdb/g' /iotdb-grafana/application.properties
# https://docs.docker.com/engine/reference/builder/#healthcheck
EXPOSE 8888
HEALTHCHECK --interval=10s --timeout=3s \
  CMD curl -f http://localhost:8888/ || exit 1
ENTRYPOINT ["java" , "-jar", "iotdb-grafana.war"]

## Optional use (new) default docker image
#FROM apache/iotdb:0.12.4-grafana
## Application.properties needs 127.0.0.1 changed to iotdb
##RUN sed -i 's/127.0.0.1/iotdb/g' /iotdb-grafana/application.properties