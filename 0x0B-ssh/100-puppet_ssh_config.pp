#!/usr/bin/env bash
# using puppet to make changes to your config

file { 'etc/ssh/ssh_config':
        ensure => present,

content =>"

        #SSH client configuration
        host*
        IdentityFile ~/.ssh/school
        passwordAuthentication no
	",
}
