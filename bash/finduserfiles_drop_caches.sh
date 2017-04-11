#!/bin/bash

sync
sudo bash -c "echo 3 > /proc/sys/vm/drop_caches"
free -m
time find / -user user > /dev/null 2>&1
free -m
time find / -user user > /dev/null 2>&1
sync
sudo bash -c "echo 3 > /proc/sys/vm/drop_caches"
free -m
