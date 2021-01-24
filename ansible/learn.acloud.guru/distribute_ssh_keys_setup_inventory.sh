#!/usr/bin/env bash
# WIP, fast and dirty
# scripts expects 5 arguments
username="cloud_user"
password="$1"
proxyserver1="$2"
dbserver1="$3"
webserver1="$4"
adminserver1="$5"

cat <<EOF >inventory
[proxy]
server1 ansible_host=$proxyserver1

[web]
webserver1 ansible_host=$webserver1

[db]
dbserver1 ansible_host=$dbserver1

[admin]
adminserver1 ansible_host=$adminserver1
EOF

cat <<EOF >ansible.cfg
[defaults]
inventory = inventory
host_key_checking = false
deprecation_warnings = false
interpreter_python = /usr/bin/python
EOF

cat <<EOF >group_vars/all.yml
ansible_become_pass: $password
ansible_remote_user: $username
EOF

for host in $proxyserver1 $webserver1 $dbserver1 $adminserver1; do
  sshpass -p $password ssh-copy-id -o StrictHostKeyChecking=no $username@$host
done

echo "Running test: ping"
ansible all -m ping

echo "Running test: facts"
ansible all -m setup -a 'filter=ansible_hostname'

echo "Running test: hostnamectl as sudo user"
ansible all -m shell -a 'hostnamectl' --become
