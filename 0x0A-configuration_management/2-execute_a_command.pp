# The killme code
exec { 'killmenow':
 command  => '/usr/bin/pkill killmenow',
 provider => 'shell',
 returns  => [1, 0],
}
