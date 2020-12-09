# Connect to a server without password with puppet
file_line {'password turn off':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    match  => 'PasswordAuthentication yes',
}
file_line {'connect':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/holberton',
}
