# Python Blacklist Helper

A simple tool to edit the hosts file to block off any FQDN that your heart desires!

### Usage:
```
runas /user:Administrator "python PATH/TO/blacklist.py example.com"
```

### Arguments
```
./blacklist.py [domain] -ip [4.4.4.4]
```

`Domain`
Required argument to specify the blocked FQDN.

`-p`
Optional argument to specify a redirect IP.