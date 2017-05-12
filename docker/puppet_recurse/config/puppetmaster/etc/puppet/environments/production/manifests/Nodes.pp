node 'client' {

  file { '/dataset/dataset_100000_files' :
    ensure  => directory,
    owner   => root,
    recurse => true,
  }

  file { '/tmp/erol_client.txt':
    ensure => present,
  }

}
