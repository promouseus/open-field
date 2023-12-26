# PODMAN
```
apk add podman
rc-update add cgroups
rc-service cgroups start

apk add openssh
rc-update add sshd

openrc default
```

Enable port 2222 and Allow root@ loging from sshd_config

ssh-keygen -t ed25519

rc-service podman start
podman info