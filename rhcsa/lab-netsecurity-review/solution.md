# Netsecurity
## Problem
```
curl http://serverb.lab.example.com
[...] Failed to connect to serverb port 80: Connection refused

curl http://serverb.lab.example.com
[...] Failed to connect to serverb port 1001: Connection refused

curl http://localhost
[...] Failed to connect to serverb port 80: Connection refused

curl http://localhost:1001
[...] Failed to connect to serverb port 1001: Connection refused
```

## Diagnosis
### 
```
systemctl is-active httpd
inactive
systemctl enable --now httpd
...failed... exited with error code.
[...] permission denied ... could not bind to address 0.0.0.0:1001
failure

# check /var/log/audit/audit.log
...avc: denied...
``` 


## Solutions
### selinux
```
semanage port -l | grep http
semanage port -a -t http_port_t -p tcp 1001
```
### firewall public zone add port 1001
```
firewall-cmd --get-default-zone
firewall-cmd --list-all
firewall-cmd --add-port=1001/tcp --permanent
```