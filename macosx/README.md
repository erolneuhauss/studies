# Learning MacOS

## Install important things first

### Homebrew -- <https://brew.sh>

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Install via brew

```bash
brew install \
  bat \
  bats-core \
  chezmoi \
  curl \
  direnv \
  exa \
  fd \
  font-hack-nerd-font \
  fzf \
  git-delta \
  helm \
  htop \
  iproute2mac \
  kubectl \
  ncdu \
  neovim \
  node \
  npm \
  pstree \
  psutils \
  pv \
  pwgen \
  ranger \
  rg \
  romkatv/powerlevel10k/powerlevel10k \
  shellcheck \
  svn \
  telnet \
  terraform \
  thefuck \
  tldr \
  tree \
  watch \
  wget \
  yq
```

### Install via pip3

```bash
/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip
pip3 install \
    ansible==2.9.26 \
    awscli \
    boto \
    jmespath
    molecule==2.22 \
    pynvim \
    python-vagrant \
    yamllint \
```

### Install via npm

```bash
npm install -g \
    pyright \
    yarn \
    bash-language-server \
    neovim \
```

### Install via yarn

```bash
yarn global add \
    ansible-language-server \
    diagnostic-languageserver

yarn global bin
```

## Historic -- pre 2021

### Install software with brew/brew cask

```bash
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

```bash
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

```bash
netstat -anp tcp | grep -i "listen"
```

## lsof

```bash
sudo lsof -Pn -iTCP -sTCP:LISTEN
```
