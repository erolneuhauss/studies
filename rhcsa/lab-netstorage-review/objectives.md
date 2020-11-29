# Netstorage
## Presets
### serverb
* firewall
* nfs-server
* users and groups
* directories

## Tasks
### Install autofs on servera
### nfs /shares from serverb should be automounted
* create `/etc/auto.master.d/shares.autofs` and indirect map `/etc/auto.shares` respectively
  * use wildcard to mount /shares on serverb
* on servera automount `/remote` 
* `ls -lh /remote/management` as user `manager1`
* `ls -lh /remote/production` as user `dbuser1`
* `ls -lh /remote/operation` as user `contractor1`
