# ZSH

## Things That Makes Life SOOOO Much Easier!

### Subsearch History

```shell
vim # then press <c-r> to start the fzf-history-widget
```

```shell
vim # then press <c-t> to start the fzf-file-widget
```

```shell
vim **  # then press <TAB> to start the fzf-file-widget
# then select with <TAB> files to edit
```

```shell
kill -9 # then press <TAB> or type ** and then <TAB>
```
### Change Directories with fzf

Press <option-c> to start the fzf-cd-widget or

```shell
cd ~/.local**<TAB>

z   <TAB>   # or
zz  <TAB>

d           # list directory history
```

### Create (nested) directory and change into it

```shell
mkdcd path/subpath
```

### Edit file with fasd

```shell
v lua
v deploy sh
```

Opens files last opened with default editor

```shell
vim ,rc,lo<Tab>
vim /etc/rc.local

mv index.html d,www<Tab>
mv index.html /var/www/
```

More examples: https://github.com/clvv/fasd?tab=readme-ov-file#examples

### Open a new terminal tab in same directory

```shell
tab         # works with iterm2 (zplugin utility)
```

### Moar -- a less alternative

```shell
p vaules.yaml
```

Opens file with pager (set to moar)

### bat -- a cat alternative

Has syntax and git support

```shell
bat vaules.yaml
```

```shell
lll # alias for exa -l | moar
```

### Search for aliases

```shell
sa git
```
