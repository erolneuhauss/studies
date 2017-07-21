# try out puppet version 5
In this project
  * there are two containers: puppet (puppetmaster) and node1
  * node1 gets modified by puppet
    * a text file motd in /etc gets created,
    * ntp package installed and 
    * user eneuhauss created

## Prerequisites
  * clone repo
  * install software according [puppet main study page](../../)

```
mkdir ~/git
cd !$
git clone git@github.com:erolneuhauss/studies.git
cd ~/git/studies/puppet/projects/puppet5
```

## Features
### hiera
### environments

## Create/Generate your first module
```
cd <your puppet code directory>
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
/usr/local/Cellar/ruby/2.4.1_1/bin/ruby ...
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
/usr/local/Cellar/ruby/2.4.1_1/bin/ruby...
....

Finished in 1.13 seconds (files took 1.73 seconds to load)
4 examples, 0 failures
```

### Run your puppet code in containers
```
cd ~/git/studies/puppet/projects/puppet5
docker-compose up
<output>
...
puppet    | Notice: Starting Puppet master version 5.0.0
node1     | 2017/07/21 12:55:45 Connected to tcp://puppet:8140
...
node1     | Notice: /Stage[main]/Motd/File[/etc/motd]/content: content changed '{md5}9830e3dbb6a828f2cc824db8db0ceaf7' to '{md5}b10a8db164e0754105b7a99be72e3fe5'
node1     | Notice: /Stage[main]/Motd/User[eneuhauss]/ensure: created
node1     | Notice: /Stage[main]/Motd/Package[ntp]/ensure: created
node1     | Info: Creating state file /opt/puppetlabs/puppet/cache/state/state.yaml
node1     | Notice: Applied catalog in 17.90 seconds
```

#### run your changed puppet code in container node1 without logging in
```
docker exec -it node1 puppet agent -t
Info: Using configured environment 'production'
Info: Retrieving pluginfacts
Info: Retrieving plugin
Info: Caching catalog for node1.ene.local
Info: Applying configuration version '1500650266'
Notice: /Stage[main]/Motd/File[/etc/motd]/owner: owner changed 'root' to 'eneuhauss'
Notice: Applied catalog in 0.04 seconds
```
