#!/bin/bash
PATH="/usr/local/texlive/2016/bin/x86_64-linux:$PATH"
export PATH

yum install -y --setopt=tsflags=nodocs \
    git \
    perl-Digest-MD5 \
    perl-Tk \
    wget && \
yum -y clean all
# Install TeXLive basic with MinionPro Support
mkdir -p /usr/local/src &&  \
wget -q -P /usr/local/src   \
    http://ftp.gwdg.de/pub/ctan/systems/texlive/tlnet/install-tl-unx.tar.gz \
    https://raw.githubusercontent.com/erolneuhauss/studies/master/docker/latex_minion/job_appl_sample.tex \
    https://raw.githubusercontent.com/erolneuhauss/studies/master/docker/latex_minion/minionpro.tgz \
    https://raw.githubusercontent.com/erolneuhauss/studies/master/docker/latex_minion/myriadpro.tgz \
    https://raw.githubusercontent.com/erolneuhauss/studies/master/docker/latex_minion/octocat.png \
    https://raw.githubusercontent.com/erolneuhauss/studies/master/docker/latex_minion/texlive.profile && \
tar xzf /usr/local/src/install-tl-unx.tar.gz -C /usr/local/bin &&   \
perl /usr/local/bin/install-tl-*/install-tl \
    -profile /usr/local/src/texlive.profile && \
tlmgr option docfiles 0 && \
tlmgr option srcfiles 0 && \
tlmgr install \
    babel-german \
    collection-fontutils \
    csquotes \
    currvita \
    ec \
    etoolbox \
    fltpoint \
    fontaxes \
    hyphen-german \
    koma-script \
    mdsymbol \
    microtype \
    mnsymbol \
    paralist \
    pdfpages \
    ucs \
    xcolor \
    xkeyval && \
tar xzf /usr/local/src/minionpro.tgz -C /usr/local/texlive/texmf-local && \
tar xzf /usr/local/src/myriadpro.tgz -C /usr/local/texlive/texmf-local && \
mktexlsr /usr/local/texlive/texmf-local && \
updmap-sys --enable Map=MinionPro.map && \
updmap-sys --enable Map=MyriadPro.map && \
tex -version && \
latex -version && \
cd /usr/local/src && \
latex $(find /usr/local -name sample2e.tex) && \
pdflatex $(find /usr/local -name sample2e.tex) && \
pdflatex /usr/local/src/job_appl_sample.tex
