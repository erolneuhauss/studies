#!/usr/bin/env bash
# https://www.udemy.com/course/linux-shell-scripting-projects
# Linux Shell Scripting: A Project-Based Approach to Learning

# This script generates a random password
# The user sets the password length with -l
# and add a special character with -s.
# Verbose mode can be enabled with -v

# -u checks for unset variables
set -eu

usage() {
  echo "Usage: ${0} [-vs] [-l LENGTH]" >&2
  echo 'Generate a random password.'
  echo ' -l LENGTH  Specify the password length.'
  echo ' -s         Append a special character to the password.'
  echo ' -v         Increase verbosity.'
  return 1
}

display() {
  local MESSAGE="${@}"
  if [[ "${VERBOSE:-}" = 'true' ]]; then
    echo "${MESSAGE}"
  fi
}


# Set a default password length
LENGTH=48

while getopts vl:s OPTION; do
  case ${OPTION} in
    v)
      VERBOSE='true'
      display 'Verbose mode on.'
      ;;
    l)
      LENGTH="${OPTARG}"
      ;;
    s)
      USE_SPECIAL_CHARACTER='true'
      ;;
    ?)
      usage
      ;;
  esac
done

echo "Number of args: ${#}"
echo "All args: ${@}"
echo "First arg: ${1:-}"
echo "Second arg: ${2:-}"
echo "Third arg: ${3:-}"

# Inspect OPTIND
echo "OPTIND: ${OPTIND}"

# Remove the options that have been parsed by getopts from the parameter list
# while leaving the remaining arguments
# and so after that point, $1 will refer to the first non-option argument passed
# to the script
shift "$(( OPTIND - 1 ))"

echo 'After the shift:'
echo "Number of args: ${#}"
echo "All args: ${@}"
echo "First arg: ${1:-}"
echo "Second arg: ${2:-}"
echo "Third arg: ${3:-}"

# if there is to any argumenst after the options, then display usage
if [[ "${#}" -gt 0 ]]; then
  usage
fi

display 'Generating a password.'

PASSWORD=$(date +%s%N${RANDOM} | sha256sum | head -c${LENGTH})

# Append a special character if requested to do so.
if [[ "${USE_SPECIAL_CHARACTER:-}" = 'true' ]]; then
  display 'Selecting a random special character.'
  SPECIAL_CHARACTER=$(echo '!@#$%^&*()_+=' | fold -w1 | shuf | head -c1)
  PASSWORD="${PASSWORD}${SPECIAL_CHARACTER}"
fi

display 'Done.'
display 'Here is the password:'

# Display password
echo ${PASSWORD}
