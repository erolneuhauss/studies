#!/bin/bash

ARG="$1"

case "$ARG" in
  up)
    vagrant up master --provision &
    vagrant up slave1 --provision &
    vagrant up slave2 --provision &
    vagrant up slave3 --provision
    ;;
  halt)
    vagrant halt slave3 &
    vagrant halt slave2 &
    vagrant halt slave1 &
    vagrant halt master
    ;;
  *)
    echo $"Usage: $0 {up|halt}"
esac
