# Learning Mac OS X
## Install important things first
### Homebrew -- https://brew.sh
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Install via brew
```
brew install \
  iproute2mac
```

## Historic -- pre 2021
### Install software with brew/brew cask
```
brew cask install \
  alinof-timer \
  anki \
  apache-directory-studio \
  copyq \
  cyberduck \
  docker \
  firefox \
  flash-npapi \
  flash-player \
  font-dejavu-sans-mono-for-powerline \
  font-dejavusansmono-nerd-font-mono \
  google-backup-and-sync \
  google-chrome \
  gpg-suite \
  iterm2 \
  java8 \
  microsoft-remote-desktop-beta \
  mysql-shell \
  mysqlworkbench \
  tunnelblick

brew install --with-default-names grep

brew install \
  ack \
  autoconf \
  awscli \
  bdw-gc \
  cfssl \
  curl \
  elinks \
  gawk \
  gdbm \
  gettext \
  glib \
  gmp \
  htop \
  httpie \
  iproute2mac \
  kubernetes-cli \
  ldapvi \
  libevent \
  libffi \
  libidn2 \
  libtool \
  libunistring \
  lz4 \
  lzo \
  mpfr \
  ncdu \
  ncurses \
  nmap \
  openshift-cli \
  openssl \
  openssl@1.1 \
  openvpn \
  pcre \
  peco \
  perl \
  pkg-config \
  popt \
  pstree \
  psutils \
  pv \
  pwgen \
  python \
  python@2 \
  rbenv \
  readline \
  ruby-build \
  socat \
  sqlite \
  telnet \
  terraform \
  tig \
  tmux \
  tree \
  v \
  w3m \
  watch \
  wget \
  xz \
  zsh
```

## .dotfiles
```
ln -s ~/.dotfiles/zlogout ~/.zlogout
ln -s ~/.dotfiles/zlogin ~/.zlogin
ln -s ~/.dotfiles/zshrc ~/.zshrc
ln -s ~/.dotfiles/zpreztorc ~/.zpreztorc
ln -s ~/.dotfiles/zprofile ~/.zprofile
ln -s ~/.dotfiles/zshenv ~/.zshenv
ln -s ~/.dotfiles/vimrc ~/.vimrc
ln -s ~/.dotfiles/tmux.conf ~/.tmux.conf
ln -s ~/.dotfiles/gitconfig ~/.gitconfig
ln -s ~/.dotfiles/zhistory ~/.zhistory
ln -s ~/.dotfiles/bin ~/bin
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
