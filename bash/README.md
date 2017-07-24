# Learning bash
## grep
### grep for real ip addresses, count occurrence and sort them
```
grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" /var/log/apache2/access.log | sort | uniq -c | sort -n
```

## History
### use argument of specific command 
```
ls -lh /var/log/
cp /var/log/auth.log /tmp
less !ls:$/messages
<output> less /var/log/messages

locate Dockerfile.puppetmaster
/Users/eneuhauss/git/studies/puppet/provision/puppet_recurse/Dockerfile.puppetmaster
/Users/eneuhauss/git/studies/puppet/projects/logoutput/Dockerfile.puppetmaster
vim -p $(!!)
<output> vim -p /Users/eneuhauss/git/studies/puppet/projects/logoutput/Dockerfile.puppetmaster /Users/eneuhauss/git/studies/puppet/provision/puppet_recurse/Dockerfile.puppetmaster

vim !less:$
<output> less /var/log/messages

docker-compose -f ~/git/studies/puppet/projects/puppet5/docker-compose.yml down
pwd
/Users/eneuhauss/git/studies/puppet/code/environments/production/modules/motd
cd !docker:2:s/docker-compose.yml/
<output> cd ~/git/studies/puppet/projects/puppet5/

vim !cd:$:pREADME.md
vim ~/git/studies/puppet/projects/puppet5/README.md

cp data/nodes/node2.ene.local.yaml common.yaml
echo '' > !!^ !!^:s/2/1
<output> echo '' > data/nodes/node2.ene.local.yaml data/nodes/node1.ene.local.yaml

```
### Links for History

  * [https://www.cyberciti.biz/faq/bash-history-repeat-substitution-command-syntax](https://www.cyberciti.biz/faq/bash-history-repeat-substitution-command-syntax)

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

## Mac OS X
### Homebrew
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

#### Install software with brew
```
brew install python
brew install macvim
brew install curl
brew install git
brew install bash
brew install psutil
brew install pstree
brew install tree
brew install iproute2mac
```

#### Install software with python
```
install powerline-status
```

#### Configure Powerline for bash
### .bash_profile
```
POWERLINE_PATH=/usr/local/lib/python2.7/site-packages/powerline
source $POWERLINE_PATH/bindings/bash/powerline.sh
```
cp -av /usr/local/lib/python2.7/site-packages/powerline/config_files/* ~/.config/powerline/
```

### .tmux.conf
```
source '/usr/local/lib/python2.7/site-packages/powerline/bindings/tmux/powerline.conf'
```
#### Powerline git integration
https://github.com/jaspernbrouwer/powerline-gitstatus
