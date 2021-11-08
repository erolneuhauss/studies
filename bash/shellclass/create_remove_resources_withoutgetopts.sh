#!/usr/bin/env bash
# https://www.udemy.com/course/linux-shell-scripting-projects
# Linux Shell Scripting: A Project-Based Approach to Learning

# This script tests working with multiple arguments

# -u checks for unset variables
set -eu

# always initiate variables, especially when working with options
# otherwise major area of bugs
ACTION="${1:-create}"
TYPE="${2:-cluster}"
NAME="${3:-stage}"
THIS_SCRIPT="$(basename "${BASH_SOURCE[0]}")"

usage() {
  echo "Usage: ${0} ACTION TYPE NAME" >&2
  echo ''
  echo 'Creates, deploys or removes defined resources'
  echo 'ARGS must be passed in exact order: ACTION TYPE NAME'
  echo ''
  echo '  ACTION can be one of: create|deploy|remove'
  echo '  TYPE can be one of:   app|cluster|ns'
  echo '  NAME should begin with a character [a-zA-Z]'
  return 1
}

create_resources() {
  echo "Creating '${TYPE}' named '${NAME}'."
}

remove_resources() {
  echo "Remove '${TYPE}' named '${NAME}'."
}

# Inspect OPTIND
echo "Number of args: ${#}"
set +u
echo "All args: ${*}"
set -u
echo "1st arg: ${1:-}"
echo "2nd arg: ${2:-}"
echo "3rd arg: ${3:-}"

echo "ACTION: ${ACTION}"
echo "NAME: ${NAME}"
echo "TYPE: ${TYPE}"


# superfluous arguments should be noted.
if [[ "${#}" -gt 3 ]]; then
  echo "You provided at some point an extra argument.
  You provided: ${THIS_SCRIPT} ${*}
  Expected: $THIS_SCRIPT ACTION TYPE NAME"
  usage
fi

# check for valid user input
if [[ ! "${ACTION}" =~ create|deploy|remove ]]; then
  echo "Provide a valid ACTION. Expecting: 'create|deploy|remove'
  Otherwise I don't know what to do"
  usage
elif [[ -z "${TYPE}" ]] || [[ ! "${TYPE}" =~ app|ns|cluster ]]; then
  echo "Provide a valid TYPE. Expecting: 'app|ns|cluster'"
  usage
elif [[ -z "${NAME}" ]]; then
  echo "Provide a valid NAME. Expecting: 'NAME', e.g. 'stage'"
  usage
else
  case "${ACTION}" in
    create|deploy)
      create_resources "${TYPE}" "${NAME}"
      ;;
    remove)
      remove_resources "${TYPE}" "${NAME}"
      ;;
  esac
fi
