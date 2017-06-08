/bin/bash

lsof +aL1 /var

lsof +aL1 /var | awk '{ SUM+=$7 } END { print SUM/1024/1024,"MB" }'
