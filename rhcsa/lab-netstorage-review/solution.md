# Networkstorage
## Solutions
### Install autofs on servera
```
yum install -y autofs
systemctl enable --now autofs
```

### nfs /shares from serverb should be automounted
* `echo '/remote /etc/auto.shares' > /etc/auto.master.d/shares.autofs`
* `echo '* -fstype=nfs,rw,sync serverb:/shares/&' > /etc/auto.shares`
* `systemctl restart autofs`
* `ls -lh /remote/management` as user `manager1`
* `ls -lh /remote/production` as user `dbuser1`
* `ls -lh /remote/operation` as user `contractor1`