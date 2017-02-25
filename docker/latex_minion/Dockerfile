# Dockerfile based on the latest CentOS 7 image
FROM centos:7
MAINTAINER eneuhauss@gmx.de

ENV PATH /usr/local/texlive/2016/bin/x86_64-linux:$PATH

# Install required packages first
RUN yum update -y && 	\
    yum install -y --setopt=tsflags=nodocs \
        git \
        perl-Tk \
        perl-Digest-MD5 \
        wget \
        curl && \
    yum -y clean all
# Install TeXLive basic with MinionPro Support
RUN mkdir -p /usr/local/src &&  \
    wget -q -P /usr/local/src   \
        http://ftp.gwdg.de/pub/ctan/systems/texlive/tlnet/install-tl-unx.tar.gz \
        https://raw.githubusercontent.com/erolneuhauss/studies/master/docker/latex_minion/texlive.profile \
        https://raw.githubusercontent.com/erolneuhauss/studies/master/docker/latex_minion/job_appl_sample.tex \
        https://raw.githubusercontent.com/erolneuhauss/studies/master/docker/latex_minion/octocat.png \
        https://raw.githubusercontent.com/erolneuhauss/studies/master/docker/latex_minion/minionpro.tgz && \
    tar xzf /usr/local/src/install-tl-unx.tar.gz -C /usr/local/bin &&   \
    perl /usr/local/bin/install-tl-*/install-tl \
        -profile /usr/local/src/texlive.profile && \
    tlmgr option docfiles 0 && \
    tlmgr option srcfiles 0 && \
	tlmgr install \
		csquotes \
		microtype \
		pdfpages \
		xcolor \
		etoolbox \
		babel-german \
		currvita \
		paralist \
		ucs \
		mdsymbol \
		koma-script \
		collection-fontutils \
		fltpoint \
		ec \
		mnsymbol \
		fontaxes && \
    tar xzf /usr/local/src/minionpro.tgz -C /usr/local/texlive/texmf-local && \
    mktexlsr /usr/local/texlive/texmf-local && \
    updmap-sys --enable Map=MinionPro.map && \
    tex -version && \
    latex -version && \
    cd /usr/local/src && \
    latex $(find /usr/local -name sample2e.tex) && \
    pdflatex $(find /usr/local -name sample2e.tex) && \
    pdflatex /usr/local/src/job_appl_sample.tex && \
    pdflatex /usr/local/src/job_appl_sample.tex && \
    rm -f /usr/local/src/*
