 # A puppet script to fix a server error in Wordpress file 'wp-settings.php'.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => 'usr/local/bin/:/bin/'
}
