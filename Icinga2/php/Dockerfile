#PHP
# TODO: switch to newest PHP 7.2 when Icinga sesions are fixed: https://github.com/Icinga/icingaweb2/pull/3186
# FROM php:7.1-fpm-alpine
FROM php:7.3-fpm-alpine

# Install PHP intl and gettext
RUN apk add --no-cache icu-dev gettext-dev curl-dev \
    && docker-php-ext-install intl gettext pdo_mysql curl
#    && apk del --no-cache gettext-dev \
#    && apk del --no-cache icu-dev

# Install PHP curl for Director
# RUN apk add curl-dev 
# RUN docker-php-ext-install curl

# Create Icingaweb2 group with same ID as other servers:
RUN /usr/sbin/addgroup -g 103 icingaweb2 \
    && /bin/sed -i '/^icingaweb2:x:103:/ s/$/www-data/' /etc/group

# Set timezone to UTC
RUN echo "date.timezone = \"UTC\"" > /usr/local/etc/php/php.ini \
        # Header already send error on web api object GET, set bigger buffer
        && echo "output_buffering = 16384" >> /usr/local/etc/php/php.ini

##
#/etc/icingaweb2/config.ini
#