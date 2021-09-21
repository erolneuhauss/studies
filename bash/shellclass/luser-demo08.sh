#!/usr/bin/env bash

set -u
# This scipt demonstrates I/O redirection

# Redirect STDOUT to a file
FILE="/tmp/data"
head -n3 /etc/passwd > ${FILE}

# read reads until \n. it does not iterate through the $FILE
# therefore it reads only the first line
read LINE < ${FILE}
echo "Line contains: ${LINE}"

# entire file can be showed
echo
echo "entire file:"
cat ${FILE}

# File descriptor (FD 0): STDIN
# File descriptor (FD 1): STOUT
# File descriptor (FD 2): STDERR

# implicit use of FD0
read X < /etc/hostname
# same as explicit use of FD0
read X 0< /etc/hostname

# implicit use of FD1
echo ${RANDOM} > random.out
# same as explicit use of FD1
echo ${RANDOM} 1> random.out
cat random.out

# random.out content would be directed to head.out, but the
# error message "head: cannot open 'non-existant-file' for reading:
# No such file or directory" would be printed out
# head random.out non-existant-file > head.out

# now, the error message is being redirected
head random.out non-existant-file 2> head.err

# both outputs are being redirected
head random.out non-existant-file > head.out 2> head.err

# use append instead of overwrite
head random.out non-existant-file > head.out 2>> head.err

# redirect both STDOUT and STDERR to a file
# 2>&1 actually it means redirect FD2 (STDERR) to FD1 (STDOUT)
head random.out non-existant-file > head.both 2>&1

# &> same as 2>&1 in bash
head random.out non-existant-file &> head.both

exit 0
