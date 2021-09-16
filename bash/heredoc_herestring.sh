#!/usr/bin/env bash
# https://learn.acloud.guru/course/admin-guide-to-bash-scripting/dashboard
# The System Administrator’s Guide to Bash Scripting - NEW 2020

cat << "EOF"
no variable expansion
$USER
EOF

cat << EOF
variable expansion
$USER
EOF

cat <<- EOF
		preceding	tabs	get	eliminated
EOF

STRING="This is a string of words in a variable."

read -r -a Words <<< $STRING

echo "1. word is '${Words[0]}'"
echo "2. word is '${Words[1]}'"
echo "3. word is '${Words[2]}'"
echo "4. word is '${Words[3]}'"


ARRAY=(e1 e2 e3 {A..F})
echo "Iterate over an array with a while loop"
while read element; do
  echo $element
done <<< $(echo ${ARRAY[*]})

echo "Iterate over an array with a for loop"
for i in "${ARRAY[@]}"; do
  echo $i
done
