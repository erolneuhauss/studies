# Class: profiles::base
class profiles::base {

  include motd

  user { 'eneuhauss':
    ensure => present,
  }

  package { 'ntp':
    ensure => present,
  }

}
