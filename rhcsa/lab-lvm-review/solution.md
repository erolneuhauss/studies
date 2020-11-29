# LVM
## Solutions

### resize partition
```
parted -s /dev/vdb resizepart 1 2G
```

### resize pv
```
pvresize -v /dev/vdb1
```

### lv sizing
```
lvextend -r -L 768M ...
lvextend -r -L 128M ...
```