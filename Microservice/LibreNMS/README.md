# LibreNMS API

## Force host add (set force to false for real hosts)
curl -X POST -d '{"hostname":"hostx.domain","version":"v3","community":"public", "authlevel":"authPriv", "authname":"userv3", "authpass":"userv3pass","authalgo":"MD5", "cryptopass":"secretX", "cryptoalg":"DES", "force_add":true}' -H 'X-Auth-Token: 64f21c05e0812d129bf16cf0fde09f36' http://localhost:8000/api/v0/devices

## Check if host is already there
curl -H 'X-Auth-Token: 64f21c05e0812d129bf16cf0fde09f36' http://localhost:8000/api/v0/devices/hostx.domain