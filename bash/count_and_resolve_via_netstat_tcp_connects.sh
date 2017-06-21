/bin/bash

netstat -ante | awk '{ print $5 }' | sed 's/:[0-9]\{1,\}//' | sort | uniq -c | sort

for node in $(netstat -ante | awk '{ print $5 }' | sed 's/:[0-9]\{1,\}//' | sort | uniq -c | awk '{ print $2 }'); do
  host $node
done
