# Kills a process named killmenow
exec { 'kill process':
  command => '/usr/bin/pkill --exact killmenow'
}
