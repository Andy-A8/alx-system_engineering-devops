# Install and configure Nginx server with puppet

$new_config="server_name _;\n\trewrite ^/redirect_me/$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;"

package {'nginx':
  ensure  => 'present',
}

exec ('install':
  command  => 'sudo ap-get update ; sudo apt-get -y install nginx ; ufw allow 'Nginx HTTP',
  provider => shell,
}

exec {'string':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html,
  provider => shell',
}

exec {'redirect_301':
  command  => 'sed -i "s|server_name\ _;|$new_conf|" /etc/nginx/sites-available/default',
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
