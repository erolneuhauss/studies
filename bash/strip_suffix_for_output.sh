#/bin/bash
#
# what this script is for: sum file size
# use cases: want to know the sum of all files with extension x 

# usage: ./strip_suffix_for_output.sh ~/Desktop .png

DIRECTORY=$1
EXTENSION=$2

find $DIRECTORY | \
  while read list; do
    echo $(basename "$list" $EXTENSION)
  done
