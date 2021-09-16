#!/usr/bin/env bash
# https://learn.acloud.guru/course/admin-guide-to-bash-scripting
# The System Administrator’s Guide to Bash Scripting - NEW 2020

# set -x

read -p "Enter a filename to read: " FILE

COUNT=1

while read -r SUPERHERO; do
  if [[ $COUNT = 3 ]]; then
    continue
  else
    COUNT+=1
  fi
  echo "Superhero name: $SUPERHERO"
done < "${FILE}"
