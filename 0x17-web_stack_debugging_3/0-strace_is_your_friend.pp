# Fixes Apache server returning 500 error

$file_to_edit = '/var/www/html/wp-settings.php'

#fix the line which has "phpp" with "php"

exec { 'fix_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
