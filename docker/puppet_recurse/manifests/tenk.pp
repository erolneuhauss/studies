  $owner         = 'root'
  $TenK = '/dataset_10000_files'
  $FiveK    = '/dataset_5000_files'

 file { [$TenK ]:
    ensure  => directory,
    owner   => $owner,
    recurse => true,
  }
