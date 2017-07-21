# puppet

## Systemrequirements
This Puppet study works fine on Mac OS X and depends on certain requirements:
  * docker for Mac (17.06.0)
  * docker-compose (1.14.0)

With docker, I provision containers based on Debian to study and test different
[projects](./projects):
  * [projects/logoutoput](./projects/logoutput): try out resource type tidy and excec attribute logoutput
  * [projects/puppet5](./projects/puppet5): try out puppet version 5
  * [projects/puppet_client](./projects/puppet_client): 
  * [projects/puppet_recurse](./projects/puppet_recurse): 

## Installation on Mac OS X
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

## Write and test your own module
```
vim spec/classes/init_spec.rb
rake spec
manifests/init.pp
```

### spec/classes/init_spec.rb
```
require 'spec_helper'
describe 'motd' do
  context 'with default values for all parameters' do
    it { should contain_class('motd') }
    it do
      should contain_file('/etc/motd').with({
        'content' => /Hello World/
      })
    end
    it { should contain_package('ntp') }
    it { should contain_user('eneuhauss') }
  end
end
```

### rake spec, example for failure
```
rake spec
/usr/local/Cellar/ruby/2.4.1_1/bin/ruby -I/usr/local/lib/ruby/gems/2.4.0/gems/rspec-support-3.6.0/lib:/usr/local/lib/ruby/gems/2.4.0/gems/rspec-core-3.6.0/lib /usr/local/lib/ruby/gems/2.4.0/gems/rspec-core-3.6.0/exe/rspec --pattern spec/\{aliases,classes,defines,unit,functions,hosts,integration,type_aliases,types\}/\*\*/\*_spec.rb --color
..F.

Failures:

  1) motd with default values for all parameters should contain Package[ntp]
     Failure/Error: it { should contain_package('ntp') }
       expected that the catalogue would contain Package[ntp]
     # ./spec/classes/init_spec.rb:10:in `block (3 levels) in <top (required)>'

Finished in 1.14 seconds (files took 1.75 seconds to load)
4 examples, 1 failure

Failed examples:

rspec ./spec/classes/init_spec.rb:10 # motd with default values for all parameters should contain Package[ntp]
```

### manifests/init.pp
```
# Class: motd
class motd {

  file { '/etc/motd':
    ensure  => present,
    content => 'Hello World',
  }

  user { 'eneuhauss':
    ensure => present,
  }

  package { 'ntp':
    ensure => present,
  }

}
```

### rake spec, example for success
```
rake spec
I, [2017-07-20T18:02:59.710995 #35133]  INFO -- : Creating symlink from spec/fixtures/modules/motd to /Users/eneuhauss/git/studies/puppet/provision/puppet5/config/puppet/opt/puppetlabs/puppet/modules/motd
/usr/local/Cellar/ruby/2.4.1_1/bin/ruby -I/usr/local/lib/ruby/gems/2.4.0/gems/rspec-support-3.6.0/lib:/usr/local/lib/ruby/gems/2.4.0/gems/rspec-core-3.6.0/lib /usr/local/lib/ruby/gems/2.4.0/gems/rspec-core-3.6.0/exe/rspec --pattern spec/\{aliases,classes,defines,unit,functions,hosts,integration,type_aliases,types\}/\*\*/\*_spec.rb --color
....

Finished in 1.13 seconds (files took 1.73 seconds to load)
4 examples, 0 failures
```

## Run
```
puppet apply Nodes.pp
```

## Installation on centos
```
puppetlabs-release-pc1-1.1.0-5.el7.noarch
puppet-agent-1.9.2-1.el7.x86_64
rubygem-puppet-lint-1.1.0-2.el7.noarch
```
