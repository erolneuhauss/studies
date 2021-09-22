#!/usr/bin/env bash
# https://www.udemy.com/course/linux-shell-scripting-projects
# Linux Shell Scripting: A Project-Based Approach to Learning

# This script generates a list a random passwords
# but not so secure ones for practice

# Display what the user typed on the command line
# e.g. script name
echo "You executed this command: ${0}"

NUMBER_OF_PARAMETERS="${#}"
echo "You supplied ${NUMBER_OF_PARAMETERS} argument(s) on the command line"

# Display the first three parameters
echo "Parameter 1: ${1}"
echo "Parameter 2: ${2}"
echo "Parameter 3: ${3}"

# Make sure they at least supply one argument all loop through all parameters
while [[ "${#}" -gt 0 ]]; do
  echo "${NUMBER_OF_PARAMETERS}"
  echo "Parameter 1: ${1}"
  echo "Parameter 2: ${2}"
  echo "Parameter 3: ${3}"
  echo
  # without shift while condition would create an endless loop.
  # if supplied one parameter, condition would be true for all eternity
  # shift "cuts off" one parameter and with while, it repeats until 0
  shift
done

exit 0
