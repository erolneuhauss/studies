# testing double quotes and
# make use auf rake tests
class profiles::cron_test {

  package { 'cron':
    ensure => installed,
  }

  $project_root       = '/var/www/rake'
  $project_dev_root   = '/var/www/rake-dev'

  cron { 'typo3-scheduler':
    ensure  => present,
    command => "/usr/bin/php ${project_dev_root}/typo3/sysext/core/bin/typo3 scheduler:run",
    user    => 'root',
    hour    => '*',
    minute  => '*',
  }

  cron { 'typo3-scheduler-dev':
    ensure  => present,
    command => "/usr/bin/php /var/www/rake-dev/typo3/sysext/core/bin/typo3 scheduler:run",
    user    => 'root',
    hour    => '*',
    minute  => '*',
  }
}

