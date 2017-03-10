# Ansible
## Prerequisites with Vagrant
### Download and Installation
Go to [https://www.vagrantup.com/downloads.html](https://www.vagrantup.com/downloads.html)
and download the version for your running hostsystem 
```
wget https://releases.hashicorp.com/vagrant/1.9.2/vagrant_1.9.2_x86_64.rpm
sudo rpm -ihv vagrant_1.9.2_x86_64.rpm
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

## Ansible Playbook
```
---
- hosts: all
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
ansible-playbook -i vagrant_ansible_inventory -v playbook.yml
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

