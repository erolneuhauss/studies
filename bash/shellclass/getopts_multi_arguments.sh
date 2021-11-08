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
  echo "Creating '${TYPE}' named '${NAME}'."
}

deploy_application_redeploy_if_exists() {
  echo "Deploying application named '${DEPLOY}'."
}

remove_kind_cluster() {
  echo "Remove '${TYPE}' named '${NAME}'."
}

while getopts crt:n: OPTIONS; do
  case ${OPTIONS} in
    c)
      ACTION=CREATE
      ;;
    r)
      ACTION=REMOVE
      ;;
    t)
      TYPE="${OPTARG}"
      if [[ -z "${TYPE}" ]]; then
        echo "I definitly need the TYPE of the resource you want to create/deploy or remove"
        echo "Choose between 'app', 'ns' (namespace) and 'cluster'"
        exit 1
      elif [[ ! "${TYPE}" =~ app|ns|cluster ]]; then
        echo "Incorrect TYPE provided. Choose between 'app', ns' and 'cluster'"
        exit 1
      fi
      ;;
    n)
      NAME="${OPTARG}"
      if [[ -z "${NAME}" ]]; then
        echo "I definitly need the name of the app, namespace or cluster
        you want me to create/deploy or remove"
      fi
      ;;
    ?)
      usage
      ;;
  esac
done

# Inspect OPTIND
echo "OPTIND: ${OPTIND}"

# Remove the options that have been parsed by getopts from the parameter list
# while leaving the remaining arguments
# and so after that point, $1 will refer to the first non-option argument passed
# to the script
# shift "$(( OPTIND - 1 ))"

# if there is to any argumenst after the options, then display usage
if [[ "${#}" -lt 1 ]]; then
  usage
fi

case "${ACTION}" in
  CREATE)
    create_kind_cluster_recreate_if_exists "${TYPE}" "${NAME}" 
    ;;
  REMOVE)
    remove_kind_cluster "${TYPE}" "${NAME}"
    ;;
esac
