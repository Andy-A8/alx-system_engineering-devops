# Puppet manuscript to enable login with the holberton user and open files without errors

# Increase limit of hard files for user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}
# Increase limit of soft files for user
exec {' increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
