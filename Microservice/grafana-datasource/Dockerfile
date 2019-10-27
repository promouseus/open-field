FROM node:lts-alpine

RUN apk update; apk upgrade; apk add git
RUN git clone https://github.com/bergquist/fake-simple-json-datasource.git /usr/src/app

WORKDIR /usr/src/app
RUN npm install
CMD [ "node", "index.js" ]