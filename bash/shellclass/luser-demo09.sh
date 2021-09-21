#!/usr/bin/env bash

# This script demonstrages the case statement

# action dependend of user statement via if
# if [[ "${1}" = 'start' ]]; then
#   echo 'Starting'
# elif [[ "${1}" = 'stop' ]]; then
#   echo 'Stopping'
# elif [[ "${1}" = 'status' ]]; then
#   echo 'Status: '
# else
#   echo 'Supply a valid option.'
#   exit 1
# fi

# instead of using if, use case
case "${1}" in
  start)
    echo 'Starting'
    ;;
  stop)
    echo 'Stopping'
    ;;
  status|state|--status|--state)
    echo 'Status:'
    ;;
  *)
    echo 'Supply a valid option.'
    exit 1
    ;;
esac

exit 0
