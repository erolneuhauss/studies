# Learning Mac OS X
## Install important things first
### Homebrew
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Install software with brew/brew cask
```
brew cask install homebrew/cask/iterm2
brew install zsh
brew cask install homebrew/cask-fonts/font-dejavu-sans-mono-for-powerline
brew cask install google-chrome
brew cask install tunnelblick
brew cask install homebrew/cask-versions/microsoft-remote-desktop-beta
brew cask install docker
brew cask install google-backup-and-sync
brew cask install apache-directory-studio
brew cask install alinof-timer gpg-suite java8

brew install --with-default-names grep
brew install ack curl elinks iproute2mac nmap perl pstree psutils pwgen socat telnet tree tmux watch wget w3m
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
