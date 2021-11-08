#!/usr/bin/env bash
# https://www.udemy.com/course/linux-shell-scripting-projects
# Linux Shell Scripting: A Project-Based Approach to Learning

# This script tests working with multiple arguments

# -u checks for unset variables
set -eu

usage() {
  echo "Usage: ${0} " >&2
  echo ''
  echo ''
  echo ''
  echo ''
  return 1
}

create_kind_cluster_recreate_if_exists() {
  echo "Creating kind cluster named \"'${CREATE}'\"." 
}

deploy_application_redeploy_if_exists() {
  echo "Deploying application named \"'${DEPLOY}'\"." 
}

remove_kind_cluster() {
  echo "Remove application named \"'${REMOVE}'\"." 
}

while getopts c:d:r: OPTIONS; do
  case ${OPTIONS} in
    c)
      CREATE="${OPTARG}"
      ;;
    d)
      DEPLOY="${OPTARG}"
      ;;
    r)
      REMOVE="${OPTARG}"
      ;;
    ?)
      usage
      ;;
  esac
done

echo "Number of before shift (OPTIND -1) args: ${#}"
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
