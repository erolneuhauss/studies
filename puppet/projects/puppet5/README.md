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
### hiera (Data Provider)
#### Hierarchy / Lookup and Merge strategy
```
 Debug: Lookup of 'classes'
   Searching for "classes"
     Merge strategy unique
       Global Data Provider (hiera configuration version 5)
         Using configuration "/etc/puppetlabs/puppet/hiera.yaml"
         No such key: "classes"
       Environment Data Provider (hiera configuration version 5)
         Using configuration "/etc/puppetlabs/code/environments/production/hiera.yaml"
         Merge strategy unique
           Hierarchy entry "Per-node data (yaml version)"
             Path "/etc/puppetlabs/code/environments/production/data/nodes/node1.ene.local.yaml"
               Original path: "nodes/%{::trusted.certname}.yaml"
               No such key: "classes"
           Hierarchy entry "Other YAML hierarchy levels"
             Path "/etc/puppetlabs/code/environments/production/data/common.yaml"
               Original path: "common.yaml"
               No such key: "classes"
```

#### directory structure
```
cd ~/git/studies/puppet/code/environments/production
tree -L 2
.
├── data
│   ├── common.yaml
│   └── nodes
├── environment.conf
├── hiera.yaml
├── manifests
│   └── site.pp
└── modules
    ├── apache
    ├── motd
    ├── profiles
    ├── roles
    └── stdlib
```


#### Environment Data Provider: hiera.yaml as in
"/etc/puppetlabs/code/environments/production/hiera.yaml"
```
hierarchy:
  - name: "Per-node data (yaml version)"
    path: "nodes/%{::trusted.certname}.yaml"
  - name: "Other YAML hierarchy levels"
    paths:
      - "common.yaml"
```

#### Per-node data: data/"nodes/%{::trusted.certname}.yaml" as in
"/etc/puppetlabs/code/environments/production/data/nodes/node1.ene.local.yaml"

#### data/common.yaml as in
"/etc/puppetlabs/code/environments/production/data/common.yaml"
```
---
classes:
  - motd
```

#### Lookup manifests/site.pp as in
"/etc/puppetlabs/code/environments/production/manifests/site.pp"
```
# 'lookup'
# Do a unique merge lookup of class names,
# then add all of those classes to the catalog (like hiera_include):
lookup('classes', Array[String], 'unique').include
```

### environments

## Create/Generate your first module
```
cd <your puppet module code directory>
# e.g. cd ~/git/studies/puppet/code/environments/production

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

### Validate your code
```
puppet parser validate motd/manifests/init.pp
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


### Test your code in a container without changing anything via --noop
```
docker exec -it puppet puppet apply --noop /etc/puppetlabs/code/environments/production/modules/motd/examples/init.pp
Warning: ModuleLoader: module 'motd' has unresolved dependencies - it will only see those that are resolved. Use 'puppet module list --tree' to see information about modules
   (file & line not available)
Notice: Compiled catalog for puppet.ene.local in environment production in 0.43 seconds
Notice: /Stage[main]/Motd/Package[ntp]/ensure: current_value 'purged', should be 'present' (noop)
Notice: Class[Motd]: Would have triggered 'refresh' from 1 event
Notice: Stage[main]: Would have triggered 'refresh' from 1 event
Notice: Applied catalog in 0.05 seconds
```

### Modules dependencies
#### Missing dependency
```
docker exec -it puppet puppet module list --tree
Warning: Missing dependency 'puppetlabs-stdlib':
  'eneuhauss-apache' (v0.1.0) requires 'puppetlabs-stdlib' (>= 1.0.0)
  'eneuhauss-motd' (v0.1.0) requires 'puppetlabs-stdlib' (>= 1.0.0)
  'eneuhauss-profiles' (v0.1.0) requires 'puppetlabs-stdlib' (>= 1.0.0)
/etc/puppetlabs/code/environments/production/modules
├─┬ eneuhauss-apache (v0.1.0)
│ └── UNMET DEPENDENCY puppetlabs-stdlib (>= 1.0.0)
├─┬ eneuhauss-motd (v0.1.0)
│ └── UNMET DEPENDENCY puppetlabs-stdlib (>= 1.0.0)
└─┬ eneuhauss-profiles (v0.1.0)
  └── UNMET DEPENDENCY puppetlabs-stdlib (>= 1.0.0)
/etc/puppetlabs/code/modules (no modules installed)
/opt/puppetlabs/puppet/modules (no modules installed)
```

#### Resolve dependency
```
root@puppet:/etc/puppetlabs/code/environments/production# puppet module install puppetlabs-stdlib
Notice: Preparing to install into /etc/puppetlabs/code/environments/production/modules ...
Notice: Downloading from https://forgeapi.puppet.com ...
Notice: Installing -- do not interrupt ...
/etc/puppetlabs/code/environments/production/modules
└── puppetlabs-stdlib (v4.17.1)
```

### Run your puppet code in containers
```
cd ~/git/studies/puppet/projects/puppet5
docker-compose up
<output>
...
puppet    | Notice: Starting Puppet master version 5.0.0
puppet    | Warning: /etc/puppetlabs/code/environments/production/data/common.yaml: file does not contain a valid yaml hash
puppet    | Debug: Lookup of 'classes'
puppet    |   Searching for "classes"
puppet    |     Merge strategy unique
puppet    |       Global Data Provider (hiera configuration version 5)
puppet    |         Using configuration "/etc/puppetlabs/puppet/hiera.yaml"
puppet    |         No such key: "classes"
puppet    |       Environment Data Provider (hiera configuration version 5)
puppet    |         Using configuration "/etc/puppetlabs/code/environments/production/hiera.yaml"
puppet    |         Merge strategy unique
puppet    |           Hierarchy entry "Per-node data (yaml version)"
puppet    |             Path "/etc/puppetlabs/code/environments/production/data/nodes/node1.ene.local.yaml"
puppet    |               Original path: "nodes/%{::trusted.certname}.yaml"
puppet    |               Found key: "classes" value: [
puppet    |                 "roles::webserver"
puppet    |               ]
puppet    |           Hierarchy entry "Other YAML hierarchy levels"
puppet    |             Path "/etc/puppetlabs/code/environments/production/data/common.yaml"
puppet    |               Original path: "common.yaml"
puppet    |               No such key: "classes"
puppet    |           Merged result: [
puppet    |             "roles::webserver"
puppet    |           ]
puppet    |       Merged result: [
puppet    |         "roles::webserver"
puppet    |       ]
puppet    | Debug: importing '/etc/puppetlabs/code/environments/production/modules/roles/manifests/init.pp' in environment production
puppet    | Debug: importing '/etc/puppetlabs/code/environments/production/modules/roles/manifests/webserver.pp' in environment production
puppet    | Debug: Automatically imported roles::webserver from roles/webserver into production
puppet    | Debug: importing '/etc/puppetlabs/code/environments/production/modules/profiles/manifests/init.pp' in environment production
node2     | Debug: Executing: '/usr/sbin/useradd eneuhauss'
puppet    | Debug: importing '/etc/puppetlabs/code/environments/production/modules/profiles/manifests/base.pp' in environment production
puppet    | Debug: Automatically imported profiles::base from profiles/base into production
puppet    | Debug: importing '/etc/puppetlabs/code/environments/production/modules/motd/manifests/init.pp' in environment production
puppet    | Debug: Automatically imported motd from motd into production
puppet    | Debug: importing '/etc/puppetlabs/code/environments/production/modules/profiles/manifests/apache.pp' in environment production
puppet    | Debug: Automatically imported profiles::apache from profiles/apache into production
puppet    | Debug: importing '/etc/puppetlabs/code/environments/production/modules/apache/manifests/init.pp' in environment production
puppet    | Debug: Automatically imported apache from apache into production
puppet    | Notice: Compiled catalog for node1.ene.local in environment production in 0.10 seconds
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


