#!/usr/bin/env bash

# This script generates a list a random passwords
# but not so secure ones for practice

# A random number as a passwords
PASSWORD="${RANDOM}"
echo "${RANDOM}"

# Three random numbers together
PASSWORD="${RANDOM}${RANDOM}${RANDOM}"
echo "${PASSWORD}"

# A better password
PASSWORD=$(date +%s%N | sha256sum | head -c32)
echo "${PASSWORD}"

# A little better password
PASSWORD=$(date +%s%N${RANDOM} | sha256sum | head -c32)
echo "${PASSWORD}"

# last way to generate a password
# Append a special character to the password
SPECIAL_CHAR=$(echo '!@#$%^&**(_)-=+?><,./;[]{}' | fold -w1 | shuf | head -c1)
echo "${PASSWORD}${SPECIAL_CHAR}"

# Display what the user typed on the command line
# e.g. script name
echo "You executed this command: ${0}"

# Display the path and filename of the script
echo "You used $(dirname ${0}) as the path to the $(basename ${0}) script"

NUMBER_OF_PARAMETERS="${#}"

echo "You supplied ${NUMBER_OF_PARAMETERS} argument(s) on the command line"

# Make sure they at least supply one argument
if [[ "${NUMBER_OF_PARAMETERS}" -lt 1 ]]; then
  echo "Usage: ${0} USER_NAME [USER_NAME]..."
  exit 1
fi

for USER_NAME in "${@}"; do
  PASSWORD=$(date +%s%N${RANDOM} | sha256sum | head -c32)
  echo "Username: ${USER_NAME} password: ${PASSWORD}"
done

exit 0
