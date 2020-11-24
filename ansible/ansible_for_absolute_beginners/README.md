# Setup
## Vagrantfile
### produce
## ansible onliner
```
ansible-config view
ansible-config dump
ansible-config list
ansible localhost -m setup --tree
ansible localhost -m setup -a 'filter=ansible_hostname'
ansible localhost -m ping
ansible localhost --become -m yum -a 'name=httpd state=present'
ansible localhost --become -m yum -a 'list=tcpdump'
ansible localhost --become -m yum -a 'name=tcpdump state=absent'
ansible localhost --become -m file -a 'path=/var/www/html state=directory'
ansible localhost --become -m firewalld -a 'service=http permanent=true state=enabled'
ansible localhost --become -m firewalld -a 'port=4444/tcp permanent=true state=disabled'
ansible localhost --become -m lineinfile -a "path=/var/www/html/index.php regex='^(.*)172.20.1.101(.*)$' line='\g<1>172.28.128.7\2' backrefs=true"
```

## ansible simple playbook
```
---
- name: latest
  become: true
  hosts: all
  tags: latest
  tasks:
  - name: install software
    yum:
      name: "{{ packages }}"
      state: present
    vars:
      packages:
        - httpd
        - git
        - tcpdump
        - php

  - name: create group
    group:
      name: web
      state: present

  - name: start/enable service httpd
    service:
      name: httpd
      state: started
      enabled: yes

  - name: create users
    user:
      name: "{{ item }}"
      groups: web
      append: yes
      state: present
    with_items: "{{ usernames }}"
    vars:
      usernames:
        - security
        - devs
        - admins
```
