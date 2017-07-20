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
rake spec
bundle clean --force
rm Gemfile.lock
bundle config specific_platform true
bundle install
bundle update
rake spec
```
## Run
```
puppet apply Nodes.pp
```
