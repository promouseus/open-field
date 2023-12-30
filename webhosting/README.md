# Old docker-compose YAML (moved to Podman)
This file is only for reference, needs to be integrated in C2IT code later on

```
mod_dav (author/share/edit files over HTTP extension protocol, maybe for Parquet up/download?)
mod_asis (add HTTP headers to top of raw file
mod_dumpio (dump raw in/out from server, just before/after SSL))
mod_echo, mod_example_hooks (example module/c-code for building your own protocol)

mod_proxy_express (proxy backend from file/db, for Docker like/live new backends)
mod_log_forensic (write forensic log to pipe/program
mod_lua (alternative for own c modules, lua script hooks, database SQL already included)

mod_logio (add in/out bytes to login lines)
mod_proxy_hcheck (load balance based on heartbeat)
mod_brotli (pre and compress)

ssh -i c:\Users\jeffr\Documents\aws-hosting-ssh.pem ubuntu@2a05:d014:186:7300:1c98:2e9b:cbe3:c57

# Maybe use full-upgrade (to also update/remove packages when needed)
sudo apt update && NEEDRESTART_MODE=a sudo apt -y upgrade
# Above needs to auto accept pop-ups/questions
# Check if restart required
cat /var/run/reboot-required
# Packages that need the reboot
cat /var/run/reboot-required.pkgs

# Check running services
service --status-all
# Check OS version
lsb_release -a
# Hardware info
hostnamectl

# Check updates
sudo apt list --upgradable
sudo apt-mark hold mariadb-server
apt-mark showhold
sudo apt-mark unhold mariadb-server
# Holdbacks can be installed by apt install name them specific
```

