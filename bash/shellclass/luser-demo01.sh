#!/usr/bin/env bash

# This script displays various information to the screen
echo "Your UID is ${UID}"

# Display the username
USER_NAME=$(id -un) # alternatives: $USER, whoami
echo "Your username is ${USER_NAME}"

# Test if the command succeeded
if [[ "${?}" -ne 0 ]]; then
  echo "The id command did not execute successfully"
  exit 1
fi

# Display if the user is the root user or not
ROOT_UID=0
if [[ "${UID}" -eq "${ROOT_UID}" ]]; then
  echo 'You are root.'
else
  echo 'You are not root'
fi

# Only display if the UID does NOT match 1000
UID_TO_TEST_FOR=1000

if [[ "${UID_TO_TEST_FOR}" -ne "${UID}" ]]; then
  echo "Your UID does not match ${UID_TO_TEST_FOR}."
fi

# Test a string conditional
USER_NAME_TO_TEST_FOR='eneuhauss'
if [[ "${USER_NAME}" = "${USER_NAME_TO_TEST_FOR}" ]]; then
  echo "Your username matches ${USER_NAME_TO_TEST_FOR}"
  # exit 1
fi

# Test for inequality
if [[ "${USER_NAME}" != "${USER_NAME_TO_TEST_FOR}" ]]; then
  echo "Your username does not match ${USER_NAME_TO_TEST_FOR}"
  # exit 1
fi

# if you do not specify an exit code at the end
# the exit status of the most recently executed
# command will be used
exit 0
