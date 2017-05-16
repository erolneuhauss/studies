node 'client' {

  exec { 'list long state.yaml' :
    command   => '/bin/ls -lh /var/lib/puppet/state/state.yaml',
    logoutput => true,
    path      => ['/bin','/usr/bin','/usr/sbin','/sbin'],
    require   => File['/var/lib/puppet/state/state.yaml'],
  }

  file { '/var/lib/puppet/state/state.yaml':
    ensure  => present,
  }

}
