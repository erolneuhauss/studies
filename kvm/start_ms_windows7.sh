#!/bin/bash

LANG=C
export LANG

  vmname="ms_windows7"
  vmvolume="/home/erol/kvm_images/ms_windows7/ms_windows7.qcow2"
  vmovl="/home/erol/kvm_images/ms_windows7/ms_windows7_2016-07-25.ovl"
  mem=4096
  macaddr="52:54:00:12:34:56"
  net="tap"
  SPICE_PORT=5920
  VGA=vmware

  exec qemu-system-x86_64 \
    -machine type=pc,accel=kvm,usb=off \
    -enable-kvm \
    -localtime \
    -no-hpet \
    -monitor unix:/tmp/monitor,server,nowait \
    -cpu host \
    -smp 2,maxcpus=4,sockets=1,cores=2,threads=1 \
    -realtime mlock=off \
    -rtc base=localtime \
    -k de \
    -m $mem \
    -name $vmname \
    -device virtio-balloon \
    -device virtio-serial-pci \
    -device virtserialport,chardev=vdagent,name=com.redhat.spice.0 \
    -chardev spicevmc,id=vdagent,name=vdagent \
    -soundhw hda \
    -vga ${VGA} \
    -spice port=${SPICE_PORT},addr=127.0.0.1,disable-ticketing \
    -net nic,macaddr=$macaddr,model=virtio \
    -net $net \
    -drive file=$vmovl,if=virtio,cache=none,media=disk,index=0 \
    -boot c
