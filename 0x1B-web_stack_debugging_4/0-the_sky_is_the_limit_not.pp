# Request limit increase
exec { 'increase':
  command => 'sed -i "s/15/15000/g" /etc/default/nginx && service nginx restart',
  path    => ['/sbin', '/usr/bin', '/bin', '/usr/sbin']
}
