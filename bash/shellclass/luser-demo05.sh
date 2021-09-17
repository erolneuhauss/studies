#!/usr/bin/env bash

# This script generates a list a random passwords

# A random number as a passwords
PASSWORD="${RANDOM}"
echo "${RANDOM}"

# Three random numbers together
PASSWORD="${RANDOM}${RANDOM}${RANDOM}"

echo "${PASSWORD}"

exit 0
