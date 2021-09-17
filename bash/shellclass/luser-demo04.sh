#!/usr/bin/env bash

# This script creates an account on the local system
# You will be prompted for the account name and password

echo "We will be creating a user. Please supply your information."

# Check whether username exists
while true; do
  # Ask for the user name
  read -p "Type a username: " USER_NAME
  grep -w ${USER_NAME} /etc/passwd
  if [[ "${?}" != 1 ]]; then
    false
  else
    true
  fi
done

# Ask for the real name
read -p "Type the real name: " REAL_NAME

# Ask for the password
read -s -p "Type in your password: " USER_PASSWORD

# Create the user
while true; do
  sudo useradd -c "${REAL_NAME}" ${USER_NAME}
  useraddExitCode="$?"
  if [[ "${useraddExitCode}" = 9 ]]; then
    echo "Deleting existing ${USER_NAME}"
    sudo userdel --force ${USER_NAME}
  fi

  # Set the password for the user
  echo ${USER_PASSWORD} | sudo passwd ${USER_NAME} --stdin
  # Force password change on first login
  false
done
