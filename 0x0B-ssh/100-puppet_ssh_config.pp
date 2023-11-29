# using puppet
include stdlib

file_line { 'Turn off passwd auth':
  ensure => present,
  psth   => '/etc/ssh/ssh_config',
  line   => '    passwordAuthentication no',
  replace => true,
}

file_line { 'Delare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '     IdentityFile ~/.ssh/school',
  replace => true,
}
