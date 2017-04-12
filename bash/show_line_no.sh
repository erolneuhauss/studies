#!/bin/bash -x
export PS4='$LINENO: '

echo date: $(date)
echo whoami: $(whoami)
echo pwd: $(pwd)
echo who: $(who)
echo hostname: $(hostname)
echo ip addresses: $(hostname -I)
