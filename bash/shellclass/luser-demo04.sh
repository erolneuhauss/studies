#!/usr/bin/env bash

# This script creates an account on the local system
# You will be prompted for the account name and password
# In order to practice if-conditions, I added the sudo requirement
# inside this script in opposite to the good practice to run sudo
# outside the script, e.g. sudo ./luser-demo04.sh

# Package sudo needs to be installed in order this to work
SUDO_INSTALLED=$(rpm -qa | grep -q sudo)
if [[ "${SUDO_INSTALLED}" -ne "0" ]]; then
  echo "This script requires sudo package to be installed."
fi

# Has the user sudo rights and does he has to provide a password
USER_HAS_SUDO=$(sudo -l -U | grep -q -P "NOPASSWD:\s+?ALL")
if [[ "${USER}" -ne "vagrant" || "${USER_HAS_SUDO}" -ne "0" ]]; then
  echo "NOPASSWD sudo powers required to run this script"
  exit 1
fi

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
    sudo useradd -c "${REAL_NAME}" -m ${USER_NAME}
  fi
done

# Ask for the password
read -s -p "Type in your password: " USER_PASSWORD

# Set the password for the user
echo ${USER_PASSWORD} | sudo passwd ${USER_NAME} --stdin

# Force password change on first login
sudo passwd --expire ${USER_NAME}

exit 0
