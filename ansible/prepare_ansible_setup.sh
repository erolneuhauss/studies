#!/usr/bin/env bash
printf "Provide Password\n"
read password
username=cloud_user
sudoers_script="add_ansible_to_sudoers.sh"
ansible_line="ansible ALL=(ALL) NOPASSWD: ALL"
ansible_sudoers_file_local="ansible.sudo"
ansible_sudoers_file_remote="/etc/sudoers.d/ansible"

printf "${ansible_line}" > ${ansible_sudoers_file_local}
visudo -cf ${ansible_sudoers_file_local}

cat <<EOF >${sudoers_script}
#!/usr/bin/env bash
cp ${ansible_sudoers_file_local} ${ansible_sudoers_file_remote}
chmod 0440 ${ansible_sudoers_file_remote}
EOF

cat <<EOF >inventory
[webservers]
webserver1

[database]
dbserver1

[admins]
adminserver1
EOF

cat <<EOF >ansible.cfg
[defaults]
host_key_checking = false
inventory = inventory
deprecation_warnings = false
remote_user = ansible
interpreter_python = /usr/bin/python
EOF

yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
yum install -y tmux vim-enhanced vim-ansible sshpass

ssh-keygen -t rsa -f /root/.ssh/id_rsa -q -P ""

for host in webserver1 dbserver1 adminserver1; do
  sshpass -p $password ssh-copy-id -o StrictHostKeyChecking=no $username@$host
  scp -o StrictHostKeyChecking=no ${sudoers_script} $username@$host:
  scp -o StrictHostKeyChecking=no ${ansible_sudoers_file_local} $username@$host:
  ssh -o StrictHostKeyChecking=no $username@$host "chmod 755 ${sudoers_script} && echo ${password} | sudo -S ./${sudoers_script}"
  sshpass -p $password ssh-copy-id -o StrictHostKeyChecking=no ansible@$host
done

ansible all -m ping
