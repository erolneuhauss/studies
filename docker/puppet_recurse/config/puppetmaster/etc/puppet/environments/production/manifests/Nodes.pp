node 'client' {

  file { '/dataset/dataset_10000_files' :
    ensure  => directory,
    owner   => root,
    recurse => true,
  }

  file { '/tmp/erol_client.txt':
    ensure => present,
  }

}
