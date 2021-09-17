#!/usr/bin/env bash

# This script creates an account on the local system
# You will be prompted for the account name and password

echo "We will be creating a user. Please supply your information."

# Ask for the user name
read -p "Type a username: " USER_NAME

# Ask for the real name
read -p "Type the real name: " REAL_NAME

# Ask for the password
read -s -p "Type in your password" USER_PASSWORD

# Create the user
useradd -c "${REAL_NAME}" 

# Set the password for the user
passwd ${USER_NAME}
# Force password change on first login
