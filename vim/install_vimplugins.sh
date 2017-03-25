#!/bin/bash

mkdir -p ~/.vim/{autoload,bundle}
curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim

cd ~/.vim/bundle
git clone https://github.com/tpope/vim-fugitive
git clone https://github.com/scrooloose/nerdtree
git clone https://github.com/scrooloose/syntastic
git clone https://github.com/ctrlpvim/ctrlp.vim
git clone https://github.com/altercation/vim-colors-solarized
git clone https://github.com/bling/vim-airline
git clone https://github.com/vim-airline/vim-airline-themes
git clone https://github.com/mhinz/vim-startify
git clone --depth 1 https://github.com/ryanoasis/nerd-fonts
git clone https://github.com/ryanoasis/vim-webdevicons
cd nerd-fonts
./install.sh DejaVuSansMono

curl -LSso ~/.vimrc https://raw.githubusercontent.com/erolneuhauss/studies/master/vim/vimrc
