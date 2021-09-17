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

exit 0
