# Learning bash
Keep in mind that some commands behave differently depending on platform
e.g. BSD vs GNU and release date.

## for loops
### count lines in a file matching a date
Consider `/var/log/messages` with entries like
```
Nov  2 03:33:04 compute-infra01 journal: {"type":"response","@timestamp":"2018-11-02T02:33:04Z","tags":[],"pid":67,"method":"head","statusCode":200,"req":{"url":"/","method":"head","headers":{"user-agent":"curl/7.29.0","host":"localhost:5601","accept":"*/*"},"remoteAddress":"127.0.0.1","userAgent":"127.0.0.1"},"res":{"statusCode":200,"responseTime":2,"contentLength":9},"message":"HEAD / 200 2ms - 9.0B"}
```
You may want to know, how many lines is added by monthly, daily, hourly or by minutes or seconds at a time

```
for month in Oct Nov; do
  for day in {1..31}; do
    for hour in {00..23}; do
      if grep -q -P "^${month}\s+${day}\s+${hour}" \
        messages; then
          echo -n "${month} ${day} ${hour} hits: "
          grep -c -P "^${month}\s+${day}\s+${hour}" \
            messages
      fi
    done
  done
done
```

## sort and uniq
### count with uniq
show me the top 20 number of occurrences 4th column of a file
```
awk '{ print $4 }' debug-20190327 | sort | uniq -c | sort -rn | head -n20
```

## grep
### grep for real ip addresses, count occurrence and sort them
```
grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" /var/log/apache2/access.log | sort | uniq -c | sort -n
```

### grep only-matching non-greedy extended regex style
```
grep -o -E '"certname":"[^"]+"' whichrolesarebeingused.json
```

### grep only-matching non-greedy perl style
```
grep -o -P '"certname":".+?"' whichrolesarebeingused.json
```

### grep only-matching substring non-greedy perl style with positive lookbehind
```
grep -o -P '(?<=roleOccupant: uid=)[^,]+' ldap.out
```

## find
### mv files selected with find
```
find . -type f -mtime -3 -name '*.list' -exec mv -t eneuhauss_tsm_helper/ {} +
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
echo '' > !!^
<output> echo '' > data/nodes/node2.ene.local.yaml
^2^1^
<output> echo '' > data/nodes/node1.ene.local.yaml

```
### Links for History

  * [https://www.cyberciti.biz/faq/bash-history-repeat-substitution-command-syntax](https://www.cyberciti.biz/faq/bash-history-repeat-substitution-command-syntax)

## make directories with given permissions and owner
```
install -o postgres -g backup -m 750 -d /var/backups/local/postgres/daily
```

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

## date
### calculate days between two dates
```
expr $(expr $(date -d '20180123' +%s) - $(date -d '20160303' +%s)) / 86400
```

## HTTP Response Time with curl
```
git clone https://gist.github.com/8888552.git curl-format
cd curl-format
cat curl-format
\n
            time_namelookup:  %{time_namelookup}\n
               time_connect:  %{time_connect}\n
            time_appconnect:  %{time_appconnect}\n
           time_pretransfer:  %{time_pretransfer}\n
              time_redirect:  %{time_redirect}\n
         time_starttransfer:  %{time_starttransfer}\n
                            ----------\n
                 time_total:  %{time_total}\n
\n

curl -w "@curl-format" -o /dev/null -s https://www.google.de

            time_namelookup:  0.004209
               time_connect:  0.012263
            time_appconnect:  0.058706
           time_pretransfer:  0.058961
              time_redirect:  0.000000
         time_starttransfer:  0.096120
                            ----------
                 time_total:  0.096361

while true
  do sleep 10
  curl \
    -w "%{time_total}\n" \
    -o /dev/null \
    -s https://github.com/erolneuhauss/studies/blob/master/bash/README.md
done
```



## Mac OS X
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
