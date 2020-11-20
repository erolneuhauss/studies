
# RHCE Preperation
## Recap

## pittfalls
### use "permanent"
Examples
```
setsebool --permanent httpd_use_nfs on
firewall-cmd --add-service=http --permanent
firewall-cmd --reload
```

### use sealert to check what is wrong
```
selalert -a /var/log/audit.log
```

### exotics
#### create a volume group with a certain physical extent size
```
vgcreate vg_name /dev/vda1 -s 32m
```

### systemd user unit files location
```
man systemd.unit # it is documented here
mkdir -p ~/.config/systemd/user
podman generate systemd --files --new --name webserver
systemctl --user enable --now container-webserver
```
