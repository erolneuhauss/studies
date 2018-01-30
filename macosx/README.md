# Learning Mac OS X
## Install important things first
### Homebrew
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Install software with brew
```
brew install --with-default-names grep
brew install ack
brew install bash
brew install curl
brew install docker
brew install docker-compose
brew install docker-machine
brew install elinks
brew install gawk
brew install git
brew install iproute2mac
brew install macvim
brew install nmap
brew install perl
brew install pstree
brew install psutil
brew install pwgen
brew install python
brew install ruby@2.3
brew install socat
brew install telnet
brew install tmux
brew install tree
brew install vim
brew install w3m
brew install watch
brew install wget
```

## some things are somewhat different from Linux
### netstat
```
netstat -anp tcp | grep -i "listen"
```

## lsof
```
sudo lsof -Pn -iTCP -sTCP:LISTEN
```
