FROM centos:8
MAINTAINER eneuhauss@gmx.de

RUN yum install -y --setopt=tsflags=nodocs nginx && yum -y clean all && rm -rf /var/cache/yum
#CMD ["nginx", "-T"]
CMD ["nginx", "-g", "daemon off;"]
