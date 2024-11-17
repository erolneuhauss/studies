#!/usr/bin/env bash

#################################################
# Author  : Erol Neuhauß
# Date    : 24 May 2024
# Version : 0.2
#
# This script will clone a git repository
# in the right place
# paste following function in ~/.zshrc or ~/.bashrc
#
# cg() {
#   source ${HOME}/.local/bin/clonegit.sh "$1"
# }

# USAGE Example:
# cg git@github.com:junegunn/fzf-git.sh.git
#################################################

REPO_URL="${1}"       # User input (a git repo git@...)
# Extract site
# Removes everything before and including the @ character
SITE="${REPO_URL#*@}"
# Removes everything after the colon (:), leaving github.com or gitlab.com.
SITE="${SITE%%:*}"

# Extract GROUP and PROJECT
REPO_PATH="${REPO_URL#*:}"    # Remove everything before and including ':'
REPO_PATH="${REPO_PATH%.git}" # Remove the trailing '.git', if it exists

# Extract GROUP (everything before the final '/')
GROUP="${REPO_PATH%/*}"

# Extract PROJECT (the final part after the last '/')
PROJECT="${REPO_PATH##*/}"

# Print the variables (for testing purposes)
echo "SITE: $SITE"
echo "GROUP: $GROUP"
echo "PROJECT: $PROJECT"

cd "${HOME}/${SITE}" || return

# directory exists
if [[ ! -d "${GROUP}" ]]; then
  echo "Path '${GROUP}' does not exist"
  echo "Creating path '${GROUP}'"
  mkdir -p "${HOME}/${SITE}/${GROUP}"
else
  echo "Path '${GROUP}' already exists"
fi

cd "${HOME}/${SITE}/${GROUP}" || return

if [[ ! -d "${PROJECT}" ]]; then
  echo "Project '${PROJECT}' does not exist"
  git clone "${REPO_URL}"
else
  echo "Project '${PROJECT}' already exists"
fi

echo "cd \"${HOME}/${SITE}/${GROUP}/${PROJECT}\""
cd "${HOME}/${SITE}/${GROUP}/${PROJECT}" || return
