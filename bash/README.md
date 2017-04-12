# Learning bash

## Process and subprocess
[print_process_number.sh (ps $$)](./print_process_number.sh)

```
erol@erol-sony-VAIO  ~/Documents/GitHub/studies/bash (master)
$ ./print_process_number.sh
      PID    PPID    PGID     WINPID   TTY         UID    STIME COMMAND
     6264       1    6264       6264  ?         197610 09:16:04 /usr/bin/mintty
      808     216     808       6728  pty0      197610 09:19:43 /usr/bin/bash
     6980     808     808       5700  pty0      197610 09:19:43 /usr/bin/ps
      216    6264     216       6608  pty0      197610 09:16:04 /usr/bin/bash

erol@erol-sony-VAIO  ~/Documents/GitHub/studies/bash (master)
$ . ./print_process_number.sh
      PID    PPID    PGID     WINPID   TTY         UID    STIME COMMAND
     6264       1    6264       6264  ?         197610 09:16:04 /usr/bin/mintty
     6196     216    6196       3816  pty0      197610 09:19:47 /usr/bin/ps
      216    6264     216       6608  pty0      197610 09:16:04 /usr/bin/bash
```
### Hint 
notice that ```./<cmd>``` starts a subprocess (via exec)
while ```. /.<cmd>``` does not

