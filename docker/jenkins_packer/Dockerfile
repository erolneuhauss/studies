FROM jenkins/jenkins
USER root
RUN apt update \
  && apt install -y software-properties-common \
  && curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - \
  && apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" \
  && apt update && apt-get install -y packer \
  && packer version
