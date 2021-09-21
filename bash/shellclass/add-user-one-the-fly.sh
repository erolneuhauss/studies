#!/usr/bin/env bash

# This script creates a new user with password and displays them at the end

# make sure the it is run as root
if [[ "${UID}" -ne 0 ]]; then
  echo "{$0} has to run as root"
  exit 1
fi

# how to use this script
if [[ "${#}" -eq 0 ]]; then
  echo "USAGE: $0 USERNAME COMMENT"
  exit 1
fi

# capture first argument
USER_NAME="${1}"

# "cut off" first argument
shift

# capture the rest of arguments
COMMENT="${@}"

# create user
if ! (useradd -c "${COMMENT}" -m ${USER_NAME}); then
  echo "Something went wrong with setting the password. Exiting immediatly"
  exit 1
fi

# A little better password
PASSWORD=$(date +%s%N${RANDOM} | sha256sum | head -c32)

# set password for user
if ! (echo ${PASSWORD} | sudo passwd ${USER_NAME} --stdin); then
  echo "Something went wrong with setting the password. Exiting immediatly"
  exit 1
fi

HOST_NAME="$(hostname)"
echo "user: '${USER_NAME}', password: '${PASSWORD}', hostname: '${HOST_NAME}'"

exit 0
