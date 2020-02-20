# modifies file
exec { 'file fix':
command => "sed -ie 's/.phpp/.php/g' /var/www/html/wp-settings.php",
path    => '/bin/',
}
