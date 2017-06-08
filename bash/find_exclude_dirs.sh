/bin/bash

find /var -not \( -path /var/tmp -path /var/log -path /var/lib/hobbit/tmp \) -ls | awk '{ SUM+=$7 } END { print SUM/1024/1024,"MB" }'
