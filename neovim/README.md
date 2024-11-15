# NEOVIM/VIM

<!--toc:start-->
- [NEOVIM/VIM](#neovimvim)
  - [Common problems](#common-problems)
    - [Can't find file ... in path](#cant-find-file-in-path)
      - [Solution](#solution)
    - [Generate Table of Contents](#generate-table-of-contents)
  - [Pre lunarvim (pre 2022)](#pre-lunarvim-pre-2022)
    - [NEOVIM config as of April 27th 2021](#neovim-config-as-of-april-27th-2021)
      - [Directory tree](#directory-tree)
      - [Details in my dotfiles repo](#details-in-my-dotfiles-repo)
        - [Plugins I got to know, use and love](#plugins-i-got-to-know-use-and-love)
    - [VIM](#vim)
<!--toc:end-->

## Common problems

### Can't find file ... in path

when I type `gf`, cursor placed at `local`

```shell
PATH=~/.local/bin:$PATH
```

I get `E447: Can't find file "PATH=~/.local/bin" in path`

#### Solution

You can visually select the part of the string you want (~/.local/bin) and then
press gf.

### Generate Table of Contents

With `marksman` [chrisatmachine/lunarvim-improve-markdown-editing-with-marksman](https://medium.com/@chrisatmachine/lunarvim-improve-markdown-editing-with-marksman-739d06c73a26)
simply press `space l a`

<!-- History -->
## Pre lunarvim (pre 2022)

I switched to neovim really just for fun and have not regreted it so far.

### NEOVIM config as of April 27th 2021
#### Directory tree
```
exa --tree --level=2 .config/nvim
.config/nvim
├── coc-settings.json
├── init.vim
├── plug-config
│  ├── airline.vim
│  ├── ale.vim
│  ├── coc.vim
│  ├── codi.vim
│  ├── signify.vim
│  └── start-screen.vim
├── plugs
│  └── plugins.vim
└── session
   ├── __LAST__ -> ckad
   └── ckad
```
#### Details in my dotfiles repo
https://github.com/erolneuhauss/dotfiles

##### Plugins I got to know, use and love
```
Yggdroot/indentLine
altercation/vim-colors-solarized
bling/vim-airline
chr4/nginx.vim
ctrlpvim/ctrlp.vim
junegunn/fzf
junegunn/fzf.vim
junegunn/seoul256.vim
kevinhwang91/rnvimr
metakirby5/codi.vim
mhinz/vim-signify
mhinz/vim-startify
morhetz/gruvbox
dense-analysis/ale
neoclide/coc.nvim
numirias/semshi
pearofducks/ansible-vim
rodjek/vim-puppet
ryanoasis/vim-webdevicons
scrooloose/nerdtree
spinks/vim-leader-guide
tmhedberg/simpylfold
tpope/vim-commentary
tpope/vim-fugitive
tpope/vim-sensible
tpope/vim-surround
vim-airline/vim-airline-themes
jiangmiao/auto-pairs
liuchengxu/vista.vim
liuchengxu/vim-which-key
```

### VIM
Use `install_vim_plugins.sh`, if you want to use vim like in the old days.
