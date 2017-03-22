#!/bin/bash

vagrant up master --provision &
vagrant up slave1 --provision &
vagrant up slave2 --provision &
vagrant up slave3 --provision &

