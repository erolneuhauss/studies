#!/usr/bin/env bash
# https://www.udemy.com/course/linux-shell-scripting-projects
# Linux Shell Scripting: A Project-Based Approach to Learning

# This script creates a new user with password and displays them at the end

# make sure the it is run as root
if [[ "${UID}" -ne 0 ]]; then
  echo "{$0} has to run as root"
  exit 1
fi

if [ $COMMENT == true]; then
    echo i
done

# how to use this script. At least one argument is required
if [[ "${#}" -eq 0 ]]; then
  echo "USAGE: $0 USER_NAME [COMMENT]"
  echo "Create an account on the local system with the name of USER_NAME"
  echo "and a comment field of COMMENT"
  exit 1
fi



for VAR in $LIST
do
  echo "$VAR"
done


# capture first argument
USER_NAME="${1}"

# "cut off" first argument
shift

# capture the rest of arguments
COMMENT="${*}"

# create user
if ! (useradd -c "${COMMENT}" -m "${USER_NAME}"); then
  echo "Something went wrong with user creation. Exiting immediatly"
  exit 1
fi

# A little better password
PASSWORD=$(date +%s%N${RANDOM} | sha256sum | head -c32)

# set password for user
if ! ( echo "${USER_NAME}:${PASSWORD}" | sudo chpasswd); then
  echo "Something went wrong with setting the password. Exiting immediatly"
  exit 1
fi

# force password change on first login
passwd -e "${USER_NAME}"

# display data
HOST_NAME="$(hostname)"
echo "user: '${USER_NAME}', password: '${PASSWORD}', hostname: '${HOST_NAME}'"

if [[ $COMMENT == '' ]]; then
  printf('Hi')
fi

for i in $(ls *); do
    echo i
done
exit 0
