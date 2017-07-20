# puppet
## Installation on centos
```
puppetlabs-release-pc1-1.1.0-5.el7.noarch
puppet-agent-1.9.2-1.el7.x86_64
rubygem-puppet-lint-1.1.0-2.el7.noarch
```
## Installation on Mac OSX
```
gem install puppet
gem install puppet-lint rspec rspec-puppet
gem install bundler
```
## Create/Generate your first module
```
cd config/puppet/opt/puppetlabs/puppet/modules/
puppet module generate eneuhauss-motd
cd motd
bundle install
```
## Run
```
puppet apply Nodes.pp
```
