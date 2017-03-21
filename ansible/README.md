# Ansible
## Prerequisites with Vagrant
### Download and Installation
Go to [https://www.vagrantup.com/downloads.html](https://www.vagrantup.com/downloads.html)
and download the version for your running hostsystem 
```
wget https://releases.hashicorp.com/vagrant/1.9.2/vagrant_1.9.2_x86_64.rpm
sudo rpm -ihv vagrant_1.9.2_x86_64.rpm
```

### Help on vagrant
```
vagrant
vagrant ssh -h
```

### First run
```
vagrant box add centos/7
vagrant init centos/7
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
cp insecure_private_key ~/.ssh/id_rsa
```

#### copy vagrant ssh-config to ssh client configuration (~/.ssh/config)
```
HOST master
  HostName 127.0.0.1
  User vagrant
  Port 2222
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile C:/Users/eroln.DESKTOP-QMFK1LG/.vagrant.d/insecure_private_key
  IdentitiesOnly yes
  LogLevel FATAL

HOST slave1
  HostName 127.0.0.1
  User vagrant
  Port 2200
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile C:/Users/eroln.DESKTOP-QMFK1LG/.vagrant.d/insecure_private_key
  IdentitiesOnly yes
  LogLevel FATAL

HOST slave2
  HostName 127.0.0.1
  User vagrant
  Port 2201
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile C:/Users/eroln.DESKTOP-QMFK1LG/.vagrant.d/insecure_private_key
  IdentitiesOnly yes
  LogLevel FATAL
```
#### Ansible configuration in inventory file

##### vagrant_ansible_inventory
```
master ansible_ssh_host=172.28.128.3 ansible_ssh_port=22 ansible_ssh_user='vagrant' ansible_ssh_private_key_file='~/.ssh/id_rsa' ansible_host_key_checking=false ansible_ssh_common_args='-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
slave1 ansible_ssh_host=172.28.128.4 ansible_ssh_port=22 ansible_ssh_user='vagrant' ansible_ssh_private_key_file='~/.ssh/id_rsa' ansible_host_key_checking=false ansible_ssh_common_args='-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
slave2 ansible_ssh_host=172.28.128.5 ansible_ssh_port=22 ansible_ssh_user='vagrant' ansible_ssh_private_key_file='~/.ssh/id_rsa' ansible_host_key_checking=false ansible_ssh_common_args='-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
```

### Check on nodes from vagrant host
```
for node in master slave1 slave2; do ssh $node "hostname; ansible --version"; done

master
ansible 2.2.1.0
  config file = /etc/ansible/ansible.cfg
  configured module search path = Default w/o overrides
slave1
ansible 2.2.1.0
  config file = /etc/ansible/ansible.cfg
  configured module search path = Default w/o overrides
slave2
ansible 2.2.1.0
  config file = /etc/ansible/ansible.cfg
  configured module search path = Default w/o overrides
```

### Check on nodes from ansible client indirectly form the vagrant host  

```
ssh master "ansible all -m ping"
master | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
slave1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
slave2 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}


ssh master "ansible -i vagrant_ansible_inventory all -a 'ansible --version'"
slave1 | SUCCESS | rc=0 >>
ansible 2.2.1.0
  config file = /etc/ansible/ansible.cfg
  configured module search path = Default w/o overrides
master | SUCCESS | rc=0 >>
ansible 2.2.1.0
  config file = /etc/ansible/ansible.cfg
  configured module search path = Default w/o overrides
slave2 | SUCCESS | rc=0 >>
ansible 2.2.1.0
  config file = /etc/ansible/ansible.cfg
  configured module search path = Default w/o overrides
```
## Ansible help
```
ansible --help

ansible-doc -l

ansible-doc setup
```

## Ansible facts
```
ansible master -m setup
ssh master "ansible master -m setup -a filter=ansible_default_ipv4"
ssh master "ansible master -m setup -a filter=*ipv4"
ssh master "ansible master -m setup -a filter="ansible_virt*"
ssh master "ansible master -m setup -a filter="ansible_dist*"

```

## Ansible orchestration
```
sudo cp vagrant_ansible_inventory /etc/ansible/hosts

ssh master "ansible all -a 'ansible --version'"
ssh master "ansible all --list-hosts"
ssh master "ansible master -m debug -a 'var=groups'"

ssh slave2 "ansible slaves -m yum -a 'pkg=httpd,ntp state=absent' --become"
ssh slave2 "ansible masters -m yum -a 'pkg=httpd,ntp state=absent' --become"

```


## Ansible Playbook
```
---
- hosts: '{{myhosts}}'
  become: true
  tasks:
    - name: ensure ntpd is at the latest version
      yum: pkg=ntp state=latest
      notify:
      - restart ntpd
  handlers:
    - name: restart ntpd
      service: name=ntpd state=restarted
```

### Run manually
```
ssh master "ansible-playbook -e myhosts=master -v playbook.yml --become"
ssh master "ansible-playbook -v playbook.yml --become"
```
#### Possible outcome
```
No config file found; using defaults                                                                      
                                                                                                          
PLAY [all] *********************************************************************                          
                                                                                                          
TASK [setup] *******************************************************************                          
ok: [db]                                                                                                  
ok: [web]                                                                                                 
                                                                                                          
TASK [ensure ntpd is at the latest version] ************************************                          
ok: [web] => {"changed": false, "msg": "", "rc": 0, "results": ["All packages providing ntp are up to date
", ""]}                                                                                                   
ok: [db] => {"changed": false, "msg": "", "rc": 0, "results": ["All packages providing ntp are up to date"
, ""]}                                                                                                    
                                                                                                          
PLAY RECAP *********************************************************************                          
db                         : ok=2    changed=0    unreachable=0    failed=0                               
web                        : ok=2    changed=0    unreachable=0    failed=0
```
