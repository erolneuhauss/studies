#!/usr/bin/env bash

# This script demonstrages the case statement

if [[ "${1}" = 'start' ]]; then
  echo starting
elif [[ "${1}" = 'stop' ]]; then
  echo stopping
fi
