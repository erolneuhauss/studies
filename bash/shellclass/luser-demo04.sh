#!/usr/bin/env bash

set -eu
# This script creates an account on the local system
# You will be prompted for the account name and password
# In order to practice if-conditions, I added the sudo requirement
# inside this script in opposite to the good practice to run sudo
# outside the script, e.g. sudo ./luser-demo04.sh

# Package sudo needs to be installed in order this to work
if ! (rpm -qa | grep -q sudo); then
  echo "This script requires sudo package to be installed. Exiting immediatly."
  exit 1
fi

# Check if user is allowed to run sudo at all
if ! (sudo -v 2> /dev/null); then
  echo "USER '${USER}' may not run sudo. Exiting immediatly"
  exit 1
fi

# Has the user sudo rights and does he has to provide a password
if ! (sudo -l -U "${USER}" | grep -q -P "NOPASSWD:\s+?ALL"); then
  echo "NOPASSWD sudo powers required to run this script. Exiting immediatly"
  exit 1
fi

echo "We will be creating a user. Please supply your information."

USER_EXISTS=true
while [[ "${USER_EXISTS}" = "true" ]]; do
  # Ask for the user name
  read -p "Type a username: " USER_NAME

  # Check whether username exists
  if (grep -w ${USER_NAME} /etc/passwd > /dev/null 2>&1); then
    USER_EXISTS=true
    echo "Username already exits. You need to use another username"
  else
    USER_EXISTS=false
    # Ask for the real name
    read -p "Type the real name: " REAL_NAME

    # Create the user
    sudo useradd -c "${REAL_NAME}" -m ${USER_NAME}
  fi
done

# Ask for the password
read -s -p "Type in your password: " USER_PASSWORD

# Set the password for the user
if ! (echo ${USER_PASSWORD} | sudo passwd ${USER_NAME} --stdin) ; then
  echo "Something went wrong with setting the password. Exiting immediatly"
  exit 1
fi

# Force password change on first login
sudo passwd --expire ${USER_NAME}

exit 0
