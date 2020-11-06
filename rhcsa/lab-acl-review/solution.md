# ACL
## Tipps
open tmux, create a second pane and check constantly with
```
watch -d -n2 'ls -lhd /shares/cases && gefacl /shares/cases'
```
resize pane down 10 line  with `ctrl + b :resize-pane -D 10`

and work with pane 1

## Solutions
needs to be done as user `root`

### set folder setgit bit
```
chmod g+s /shares/cases
```

### set folder group owner
```
chgrp managers /shares/cases/
```

### set acl group `contractors` rwx
```
setfacl -m g:contractors:rwx  /shares/cases/
```

### set acl user `contractor3` r-x
```
setfacl -m u:contractor3:r-x /shares/cases/
```

### set default acl group  `contractors` rwx
```
setfacl -d -m g:contractors:r-x /shares/cases/
```

### set default acl user `contractors3` r-x
```
setfacl -d -m u:contractor3:r-x /shares/cases/
```
