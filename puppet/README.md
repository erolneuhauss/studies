# puppet
## Projects
With docker, I provision containers based on Debian to study and test different
[projects](./projects):
  * [logoutoput](./projects/logoutput): try out resource type tidy and excec attribute logoutput
  * [puppet5](./projects/puppet5): try out puppet version 5
  * [puppet_client](./projects/puppet_client): basic puppet client installation
  * [puppet_recurse](./projects/puppet_recurse): try out file attributes recurse and recurselimit

## Systemrequirements on Mac OS X
### Homebrew and other essential software for development
Read and follow instructions
[studies/bash/README.md#homebrew](https://github.com/erolneuhauss/studies/blob/master/bash/README.md#homebrew)

### Docker
This Puppet study works fine on Mac OS X and depends on certain requirements:
  * docker for Mac (17.06.0)
  * docker-compose (1.14.0)

### Puppet (latest on darwin) Installation on Mac OS X
```
gem install puppet
gem install puppet-lint rspec rspec-puppet
gem install bundler
```

## Run your module in containers
**Tested with project [puppet5](./projects/puppet5) and it worked out**
  * create directory 'git' in your home directory
  * change to newly created directory 'git'
  * clone this repository: [study](git@github.com:erolneuhauss/studies.git)
  * change to directory ~/git/puppet/projects/<a project>
  * run docker-compose up

### see for example project [puppet5](./projects/puppet5)

### useful gadgets
```
for module in \
  $(puppet module list --modulepath=. | grep '^[^/]' | cut -d' ' -f2); do
   puppet module uninstall $module --modulepath=.
done
```
