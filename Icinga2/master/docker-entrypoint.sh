#!/bin/sh
set -e

    if /usr/sbin/icinga2 feature list|/bin/grep Enabled|/bin/grep -q "api"; then
        echo Icinga2 API already configured
    else
        echo Configuring Icinga2 API
        exec /usr/sbin/icinga2 api setup; reboot;
    fi

    exec /usr/sbin/icinga2 daemon -x warning
