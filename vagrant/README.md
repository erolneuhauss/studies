# Vagrant
## Download and Installation
Go to [https://www.vagrantup.com/downloads.html](https://www.vagrantup.com/downloads.html)
and download the version for your running hostsystem 
```
wget https://releases.hashicorp.com/vagrant/1.9.2/vagrant_1.9.2_x86_64.rpm
sudo rpm -ihv vagrant_1.9.2_x86_64.rpm
```

## First run
```
vagrant box add centos/7
vagrant init centos/7
vagrant up
vagrant ssh
(exit)
vagrant status
vagrant global-status
```

## how to access alternativly
```
ssh vagrant@localhost -p $SOME_PORT -i ~/.vagrant.d/insecure_private_key
```

## Plugins
