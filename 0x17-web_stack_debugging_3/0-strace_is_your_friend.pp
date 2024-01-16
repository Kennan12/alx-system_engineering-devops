# Strace is your friend and fix the error
exec { 'fix-wordpress':
  command  => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  }
exec {'restart web server':
  command  => '/usr/sbin/service apache2 restart'
}
