# Login and open

exec {'open':
  command => 'sed -i "s/5/15000/g; s/4/5000/g" /etc/security/limits.conf',
  path    => ['/usr/bin', '/bin', '/sbin', '/usr/sbin']
}
