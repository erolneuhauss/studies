node 'client' {

  $statedir = '/var/lib/puppet/state'
  $stateyaml = '/var/lib/puppet/state/state.yaml'

  file { $stateyaml:
    ensure  => present,
  }

  exec { 'list long state.yaml' :
    command   => "/bin/ls -lh ${stateyaml}",
    logoutput => true,
    path      => ['/bin','/usr/bin','/usr/sbin','/sbin'],
    require   => File[$stateyaml],
  }

  exec { 'cp state.yaml to temp' :
    command => "/bin/cp ${stateyaml} /tmp",
    path    => ['/bin','/usr/bin','/usr/sbin','/sbin'],
    require => File[$stateyaml],
  }

  file { '/tmp/state.yaml':
    ensure  => present,
    mode    => '0644',
    require => Exec['cp state.yaml to temp'],
  }

  tidy { $statedir:
    size    => '3k',
    recurse => 1,
    matches => 'state.yaml'
  }

}
