#!/usr/bin/env bash

# This script creates an account on the local system
# You will be prompted for the account name and password

echo "We will be creating a user. Please supply your information."

USER_EXISTS=true
while [[ "${USER_EXISTS}" = "true" ]]; do
  # Ask for the user name
  read -p "Type a username: " USER_NAME

  # Check whether username exists
  grep -w ${USER_NAME} /etc/passwd

  if [[ "${?}" = 0 ]]; then
    USER_EXISTS=true
    echo "You need to use another username"
  else
    USER_EXISTS=false
    # Ask for the real name
    read -p "Type the real name: " REAL_NAME

    # Create the user
    sudo useradd -c "${REAL_NAME}" ${USER_NAME}
  fi
done

# Ask for the password
read -s -p "Type in your password: " USER_PASSWORD

# Set the password for the user
echo ${USER_PASSWORD} | sudo passwd ${USER_NAME} --stdin

# Force password change on first login
sudo passwd --expire ${USER_NAME}

exit 0
