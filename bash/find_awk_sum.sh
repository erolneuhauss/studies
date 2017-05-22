#/bin/bash
#
# what this script is for: sum file size
# use cases: want to know the sum of all files with extension x 

# usage: ./find_awk_sum.sh ~/Desktop png

DIRECTORY=$1
EXTENSION=$2

find $DIRECTORY -name "*.$EXTENSION" -ls | awk \
  '{ SUM+=$7 } END { print SUM/1024/1024,"MB" }'
