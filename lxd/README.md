# Setup LXD on a chromebook
Follow these steps: https://ubuntu.com/blog/using-lxd-on-your-chromebook
## Attention
Use your gateway ip when `lxc remote add chromeos 100.115.92.193:8443` and your ip address


## Install updated version of LXC/LXD
```
sudo apt install libsquashfuse0 squashfuse fuse
sudo apt install snap
sudo snap install --stable hello-world
sudo snap install core
sudo snap install snapd
sudo snap install lxd --channel=4.0/stable
sudo ls -lh /snap/lxd
sudo ln -r -s /snap/lxd/[...]/bin/lxc /usr/local/bin/lxc 
sudo usermod -aG lxd myself
bash
lxc --version
4.0.5
lxc launch images:ubuntu/20.04 u20
```

read: https://www.realjenius.com/2020/01/12/kde-neon-snap-apps-missing/
