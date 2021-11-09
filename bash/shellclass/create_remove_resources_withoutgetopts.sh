#!/usr/bin/env bash
# https://www.udemy.com/course/linux-shell-scripting-projects
# Linux Shell Scripting: A Project-Based Approach to Learning

# This script tests working with multiple arguments

# -u checks for unset variables
set -eu

usage() {
  echo "Usage: ${0} ACTION TYPE CLUSTER_NAME [NAMESPACE1] [NAMESPACE2]..." >&2
  echo ''
  echo 'Creates or deletes defined resources'
  echo 'ARGS must be passed in exact order: ACTION TYPE CLUSTER_NAME'
  echo ''
  echo '  ACTION can be one of: create|delete'
  echo '  TYPE can be one of:   cluster|ns'
  echo '  Any CLUSTER_NAME or NAMESPACES should begin with a alpabetic character [a-zA-Z]'
  return 1
}

manage_resources() {
  ACTION="${1}"
  TYPE="${2}"
  CLUSTER_NAME="${3}"
  if [[ "${TYPE}" == 'ns' ]]; then
    manage_namespaces "${@}"
  else
    manage_kind_cluster "${ACTION}" "cluster" "${CLUSTER_NAME}"
    if [[ "${#}" -gt 3 && "${ACTION}" == 'create' ]]; then
      manage_namespaces "${@}"
    fi
  fi
}

manage_namespaces() {
  ACTION="${1}"
  CLUSTER_NAME="${3}"
  shift 3
  i=1
  for ns in "${@}"; do
    echo kubectl --config "${CLUSTER_NAME}" "${ACTION}" namespace "${ns}"
  done
}

loop_through_namespaces() {
  shift 3
  i=1
  echo "NAMESPACES: "
  for args in "${@}"; do
    echo "${i}. Namespace to create: ${args}"
    (( i+=1 ))
  done
}

manage_kind_cluster() {
  echo "ACTION: ${ACTION} ${TYPE} ${CLUSTER_NAME}"
}


# Show info about arguments
set +u
echo "Number of args: ${#}"
echo "All args: ${*}"
echo "1st arg: ${1:-}"
echo "2nd arg: ${2:-}"
echo "3rd arg: ${3:-}"
echo "4rd arg: ${4:-}"
echo "5rd arg: ${5:-}"
echo "6rd arg: ${6:-}"
set -u

echo '#########################################'
echo '############ BEGIN MAIN SCRIPT ##########'
echo '#########################################'

# MAIN SCRIPT
## WITHOUT ANY ARGUMENTS JUST CREATE DEFAULT CLUSTER
if [[ "${#}" -lt 1 ]]; then
  ACTION="default"
## EXAMINE INPUT
elif [[ "${1:-}" == 'help' ]]; then
  ACTION='help'
## EXAMINE EXISTENCE AND VALIDITY OF MANDATORY ARGUMENTS
elif [[ ! "${1:-}" =~ help|create|delete ]]; then
  echo "Provide a valid ACTION. Expecting: 'help|create|delete'"
  exit 1
elif [[ ! "${2:-}" =~ ns|cluster ]]; then
  echo "Provide a valid TYPE. Expecting: 'ns|cluster'"
  exit 1
elif [[ -z "${3:-}" ]]; then
  echo "Provide a valid NAME for the cluster. Expecting: 'STRING'"
  exit 1
else
  ACTION="${1}"
  TYPE="${2}"
  CLUSTER_NAME="${3}"
  ### IF ACTION on TYPE 'ns' WE NEED A LEAST A 4TH ARGUMENT
  if [[ "${TYPE}" == 'ns' && "${#}" -le 3 ]]; then
    echo "Provide a valid NAME for the namespace in cluster ${CLUSTER_NAME}.
    Expecting at least 1 'STRING' or whitespaced strings: 'STRING1' 'STRING2'..."
    exit 1
  fi
fi

case "${ACTION}" in
  default)
    manage_resources "create" "cluster" "stage"
    ;;
  create|delete)
    manage_resources "${@}"
    ;;
  help)
    echo "ACTION: ${ACTION}"
    ;;
esac
