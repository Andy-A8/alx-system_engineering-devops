# Create a manifest that kills a process named killmenow

exec { 'kill':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/:/usr/local/bin/:/bin/',
}