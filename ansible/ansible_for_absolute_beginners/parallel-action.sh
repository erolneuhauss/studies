#!/bin/bash

ARG="$1"

case "$ARG" in
  up)
    vagrant up controller --provision &
    vagrant up target1 --provision &
    vagrant up target2 --provision
    ;;
  halt)
    vagrant halt controller &
    vagrant halt target1 &
    vagrant halt target2
    ;;
  *)
    echo $"Usage: $0 {up|halt}"
esac
