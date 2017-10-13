# Class roles::webserver
class roles::webserver {
  include profiles::base
  include profiles::web
  include profiles::cron_test

}
