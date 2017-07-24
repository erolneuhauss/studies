# Class: motd
class motd {

  file { '/etc/motd':
    ensure  => present,
    owner   => 'eneuhauss',
    content => 'Hello World',
    require => User['eneuhauss'],
  }

  user { 'eneuhauss':
    ensure => present,
  }

  package { 'ntp':
    ensure => present,
  }

}
