#!/usr/bin/env bash
# https://learn.acloud.guru/course/admin-guide-to-bash-scripting
# The System Administrator’s Guide to Bash Scripting - NEW 2020

# set -x

# read -p "Enter a filename to read: " FILE
FILE="super.txt"

COUNT=1

echo "first while iteration "
while read -r SUPERHERO; do
  echo "Superhero name: $SUPERHERO"
done < "${FILE}"
printf "\n"

echo "second while iteration with break"
while read -r SUPERHERO; do
  echo "Superhero name: $SUPERHERO"
  break
done < "${FILE}"
printf "\n"

echo "third while iteration with count to 3"
while read -r SUPERHERO; do
  if [[ $COUNT = 3 ]]; then
    continue
  else
    let COUNT+=1
  fi
  echo "Superhero name: $SUPERHERO"
done < "${FILE}"

