#!/bin/bash

ssh master \
  "ansible all -m shell -a 	\
    'if [ -d /home/vagrant/studies ]; then  \
       cd ~/studies; 		\
       git pull origin master; 	\
       cd ~/;	 		\
     else			\
       git clone		\
       https://github.com/erolneuhauss/studies.git; \
     fi;			\
    cp ~/studies/ansible/provision/playbook.yml ~/'"
