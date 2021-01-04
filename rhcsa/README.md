# Learned so far
## Not only by this course but with all

### sudo
Rather than `sudo su -` use `sudo -i` (simulated initial login shell with environment variables)

### old cmd inline search and replace string in last command globally
`^foo^bar^:G`

### bash line editing
Type `fc` to edit your last command
`fc -s foo=bar`

### grep
`grep -w foo` respects word boundaries and omits `foobar`

### Exam preparation
* https://training.linuxfoundation.org/wp-content/uploads/2019/10/LFCS-Practice-Questions-v1.1.pdf
* redo the SUSE 11 Exam!

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
