# Class: apache
class apache {
  package { 'apache2':
    ensure => present,
  }

}
