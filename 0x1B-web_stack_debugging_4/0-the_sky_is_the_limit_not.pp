# Puppet manuscript to increase amount of traffic an Nginx web server can handle

# Increase ULIMIT of default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
