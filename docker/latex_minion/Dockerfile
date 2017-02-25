# Dockerfile based on the latest CentOS 7 image
FROM centos:7
MAINTAINER eneuhauss@gmx.de
# Install required packages first
RUN yum update -y && 	\
    yum install -y --setopt=tsflags=nodocs \ 
        git \
        perl-Tk \
        perl-Digest-MD5 \
        wget \
        curl \
    && yum -y clean all
# Install TeXLive basic
RUN mkdir -p /usr/local/src &&  \
    wget -q -P /usr/local/src http://ftp.gwdg.de/pub/ctan/systems/texlive/tlnet/install-tl-unx.tar.gz && \
    tar xzf /usr/local/src/install-tl-unx.tar.gz -C /usr/local/bin &&   \
    rm -f /usr/local/src/install-tl-unx.tar.gz
COPY texlive.profile /usr/local/src
RUN perl /usr/local/bin/install-tl-*/install-tl -profile /usr/local/src/texlive.profile && rm -rf /usr/local/src/install-tl-*
ENV PATH /usr/local/texlive/2016/bin/x86_64-linux:$PATH
CMD tex -version
CMD latex -version
CMD latex $(find /usr/local -name sample2e.tex)
CMD pdflatex $(find /usr/local -name sample2e.tex)
RUN tlmgr option docfiles 0
RUN tlmgr option srcfiles 0
RUN tlmgr install csquotes microtype pdfpages xcolor etoolbox babel-german currvita paralist ucs mdsymbol koma-script collection-fontutils fltpoint ec mnsymbol fontaxes
COPY minionpro.tgz /usr/local/src/
RUN tar xzf /usr/local/src/minionpro.tgz -C /usr/local/texlive/texmf-local/ && rm -f /usr/local/src/minionpro.tgz
RUN mktexlsr /usr/local/texlive/texmf-local
RUN updmap-sys --enable Map=MinionPro.map
COPY job_appl_sample.tex /usr/local/src/
COPY octocat.png /usr/local/src/
RUN cd /usr/local/src && pdflatex /usr/local/src/job_appl_sample.tex
RUN cd /usr/local/src && pdflatex /usr/local/src/job_appl_sample.tex
