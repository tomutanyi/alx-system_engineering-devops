# Killing a process called 'killmenow'

# Only kill the process while exist

# If it doesn't exists, puppet should exit
# with a 0 return code and not 1 .


exec {'kill `killmenow` process':
command => '/usr/bin/pkill -9 -f killmenow',
onlyif  => '/usr/bin/pgrep -f killmenow'
}
