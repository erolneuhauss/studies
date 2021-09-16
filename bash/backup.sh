#!/usr/bin/env bash
# https://learn.acloud.guru/course/admin-guide-to-bash-scripting/dashboard
# The System Administrator’s Guide to Bash Scripting - NEW 2020

#set -eu

# Backing up required files

# Catch user input
if [[ -z $1 ]]; then
  echo "Missing argument. Supply log file name"
  exit 255
fi

# Variables
MYLOGFILE="$HOME/$1"
LOGFILE="/home/$USER/mylog"
BACKUP_SRC="/usr/bin"
BACKUP_TRG="/home/$USER/backup"

# Function to create backup target directory
function init {
  if [[ -d ${BACKUP_TRG} ]]; then
    echo "Directory already exists"
    echo "$(date +"%c")" >> $MYLOGFILE
    return 1
  else
    echo "Creating backup directory"
    mkdir $BACKUP_TRG 2> /dev/null
    return 0
  fi
}

# Function to override existing command
tail () {
  command tail -n $1
}

# Function is still a function even without "function ..."
cleanup () {
  rm -rf $BACKUP_TRG
  echo "RECEIVED CTRL-C" >> $MYLOGFILE
  exit
}

init
trap cleanup SIGINT

echo "Copying files"
cd $BACKUP_SRC
for i in $( ls su* ); do
  # testing trap
  sleep 1
  cp -v "${i}" $BACKUP_TRG/"${i}"-backup >> $MYLOGFILE 2>&1
done

#echo "Copying Files" && cp -v $BACKUP_SRC/su* $BACKUP_TRG >> $LOGFILE 2>&1

cd $HOME
grep -i sudo $MYLOGFILE | tail 2

exit 127
