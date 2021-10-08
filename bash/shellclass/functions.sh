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

# probably a more appropiate approach would be to use
# -v varname
#       True if the shell variable varname is set (has been assigned a value).
# because -z and -n checks for the length of the string
# -z string
#       True if the length of string is zero.
# -n string
#       True if the length of string is non-zero.

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

my_logger() {
  # This function sends a message to syslog and to stdout if VERBOSE is true
  local MESSAGE="${@}"
  if [[ "${VERBOSE}" = 'true' ]]; then
    echo "${MESSAGE}"
  fi
  # Log independ of VERBOSE
  logger -t functions.sh "${MESSAGE}"
}

readonly VERBOSE='false'
my_logger 'Hello!'
my_logger 'This is fun!'

backup_file() {
  # This function creates a backup of a file. Returns non-zero status on error

  local FILE="${1}"

  # Make sure the file exists.
  if [[ -f "${FILE}" ]]; then
    local BACKUP_FILE="/var/tmp/$(basename ${FILE}).$(date +%F-%N)"
    my_logger "Backing up ${FILE} to ${BACKUP_FILE}."

    # The exit status of the function will be the exit status of the cp command
    cp -p ${FILE} ${BACKUP_FILE}
  else
    # The file does not exists, so return a non-zero exit status
    return 1
  fi
}

backup_file /etc/passwd
