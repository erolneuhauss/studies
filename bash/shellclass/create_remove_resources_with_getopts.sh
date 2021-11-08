#!/usr/bin/env bash
# https://www.udemy.com/course/linux-shell-scripting-projects
# Linux Shell Scripting: A Project-Based Approach to Learning

# This script tests working with multiple arguments

# -u checks for unset variables
set -eu

# always initiate variables, especially when working with options
# otherwise major area of bugs
ACTION=false
NAME=false
TYPE=false
THIS_SCRIPT="$(basename "${BASH_SOURCE[0]}")"

usage() {
  echo "Usage: ${0} " >&2
  echo ''
  echo ''
  echo ''
  echo ''
  return 1
}

create_resources() {
  echo "Creating '${TYPE}' named '${NAME}'."
}

remove_resources() {
  echo "Remove '${TYPE}' named '${NAME}'."
}

while getopts :crt:n: OPTIONS; do
  case ${OPTIONS} in
    c)
      ACTION=CREATE
      ;;
    r)
      ACTION=REMOVE
      ;;
    t)
      TYPE="${OPTARG}"
      ;;
    n)
      NAME="${OPTARG}"
      ;;
    :)
      echo "Option -${OPTARG} requires an argument"
      usage
      ;;
    ?)
      echo "You have provided an invalid option or argument"
      usage
  esac
done

# Inspect OPTIND
echo "OPTIND: ${OPTIND}"
echo "Number of args: ${#}"
set +u
echo "All args: ${*}"
set -u
echo "1st arg: ${1:-}"
echo "2nd arg: ${2:-}"
echo "3rd arg: ${3:-}"
echo "4th arg: ${4:-}"
echo "5th arg: ${5:-}"
echo "6th arg: ${6:-}"

echo "ACTION: ${ACTION}"
echo "NAME: ${NAME}"
echo "TYPE: ${TYPE}"


# if there is nothing, no flag no argument. Show usage
if [[ "${#}" -lt 1 ]]; then
  echo "${THIS_SCRIPT} expects OPTIONS and ARGUMENTS."
  usage
# also superfluous arguments should be noted.
elif [[ "${#}" -gt 5 ]]; then
  echo "You provided at some point an extra argument.
  You provided: ${THIS_SCRIPT} ${*}
  Expected: $THIS_SCRIPT -c|-r -t [app|ns|cluster] -n NAME"
  usage
fi

# check for valid user input
if [[ "${ACTION}" == 'false' ]]; then
  echo "Provide a valid OPTION. Expecting: '-c' or '-r'.
  Otherwise I don't know what to do"
  usage
elif [[ "${TYPE}" == 'false' ]] || [[ ! "${TYPE}" =~ app|ns|cluster ]]; then
  echo "Provide a valid TYPE. Expecting: '-t [app|ns|cluster]'"
  usage
elif [[ "${NAME}" == 'false' ]] || [[ "${NAME}" =~ ^- ]]; then
  echo "Provide a valid NAME. Expecting: '-n [NAME]'"
  usage
else
  case "${ACTION}" in
    CREATE)
      create_resources "${TYPE}" "${NAME}"
      ;;
    REMOVE)
      remove_resources "${TYPE}" "${NAME}"
      ;;
  esac
fi
