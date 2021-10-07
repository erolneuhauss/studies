#!/usr/bin/env bash
# https://www.udemy.com/course/linux-shell-scripting-projects
# Linux Shell Scripting: A Project-Based Approach to Learning

# -u checks for unset variables
set -eu

# https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_10_03.html
# without :- in "${VERBOSE:-}" set -u would complain
# Substitution ${VAR:-WORD}
# alternative +x in "${VERBOSE+x}". "x" not mandatory, could be "foo" instead
# "${VERBOSE+foo}"
variable_check_n() {
  if [[ -n "${VERBOSE:-}" ]]; then
    echo "'-n' returns 'true', because VERBOSE' variable IS set and has the value of ${VERBOSE}"
  else
    echo "'-n' returns 'false', because VERBOSE' variable is NOT set"
  fi
}
 # shorter, but somewhat harder to pick up
 # [[ -n "${VERBOSE}" ]] && echo "Variable defined" || echo "Variable NOT defined"

variable_check_z() {
  if [[ -z "${VERBOSE:-}" ]]; then
    echo "'-z' returns 'true', because VERBOSE' variable is NOT set"
  else
    echo "'-z' return 'false', because VERBOSE' variable IS set and has the value of ${VERBOSE}"
  fi
}

log() {
  local MESSAGE="${@}"
  if [[ -n "${VERBOSE:-}" ]]; then
    echo "${MESSAGE}"
  fi
}

echo "Variable 'VERBOSE' is NOT set"
variable_check_n
variable_check_z

echo "Variable 'VERBOSE' IS set"
VERBOSE='something'
variable_check_n
variable_check_z

unset VERBOSE
log 'The first line should be printed!'
VERBOSE='something'
log 'The second line should be printed!'

improved_log() {
  local VERBOSE="${1}"
  shift # otherwise 'true' would be printed out, too
  local MESSAGE="${@}"
  if [[ -n "${VERBOSE:-}" ]]; then
    echo "${MESSAGE}"
  fi
}

VERBOSITY='true'
improved_log "${VERBOSITY}" 'The first line should be printed!'
improved_log "${VERBOSITY}" 'The second line should be printed!'
