# Ansible
## Prerequisites with Vagrant
### Download and Installation
Go to [https://www.vagrantup.com/downloads.html](https://www.vagrantup.com/downloads.html)
and download the version for your running hostsystem 

### Help on vagrant
```
vagrant
vagrant ssh -h
```

### First run
```
vagrant box add generic/centos7
vagrant init -m generic/centos7
vagrant up
vagrant ssh
(exit)
vagrant status
vagrant global-status
```

### Configuration on vagrant host
#### Lookup and modify ssh config and inventory for your needs
```
vagrant ssh-config
```

#### copy vagrant ssh-config to ssh client configuration (~/.ssh/config)

#### Ansible configuration in inventory file
##### vagrant_ansible_inventory

