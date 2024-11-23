# ZSH

## [junegunn/fzf -- Fuzzy completion for bash and zsh](https://github.com/junegunn/fzf?tab=readme-ov-file#fuzzy-completion-for-bash-and-zsh)

```shell
# Files under the current directory
# - You can select multiple items with TAB key
vim **<TAB>

# Files under parent directory
vim ../**<TAB>

# Files under parent directory that match `fzf`
vim ../fzf**<TAB>

# Files under your home directory
vim ~/**<TAB>


# Directories under current directory (single-selection)
cd **<TAB>

# Directories under ~/github that match `fzf`
cd ~/github/fzf**<TAB>

```
### FZF keybindings

#### `<CTRL-R>` -- fzf-history-widget

```shell
vim # then press <c-r> to start the fzf-history-widget
```

#### `<CTRL-T>` -- fzf-file-widget

```shell
vim # then press <c-t> to start the fzf-file-widget
```

```shell
vim ~/.zprezto/**<TAB> to start the fzf-file-widget
# then select with <TAB> (multiple) files to edit
```

```shell
kill -9 # then press <TAB> or type ** and then <TAB>
```
#### `<ALT-C>` -- fzf-cd-widget

Press `<option-c>` to start the fzf-cd-widget or

```shell
cd ~/.local**<TAB>

z   <TAB>   # or
zz  <TAB>

d           # list directory history
```

## Create (nested) directory and change into it

```shell
mkdcd path/subpath
```

## [clvv/fasd](https://github.com/clvv/fasd)

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

## Open a new terminal tab in same directory

```shell
tab         # works with iterm2 (zplugin utility)
```

## `p` defaults to `$PAGER`

```shell
p vaules.yaml
```

Opens file with pager (set to moar)

## bat -- a cat alternative

Has syntax and git support

```shell
bat vaules.yaml
```

```shell
lm # alias for eza --all --long | moar
```

## Search for aliases

```shell
sa git
```
