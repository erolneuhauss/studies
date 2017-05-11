client {

  file { '/dataset_5000_files' :
    ensure  => directory,
    owner   => root,
  }

  file { '/tmp/erol_client.txt':
    ensure => present,
  }

}
