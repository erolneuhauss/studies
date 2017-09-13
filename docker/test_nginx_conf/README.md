# Want to be able to check nginx configuration
## build
docker-compose build

## run
docker-compose up

## Example
```
docker-compose up

Recreating test_config ...
Recreating test_config ... done
Attaching to test_config
test_config | 2017/09/13 12:30:29 [emerg] 1#1: PEM_read_bio_X509_AUX("/etc/ssl/certs/wildcard.........de.crt") failed (SSL: error:0906D06C:PEM routines:PEM_read_bio:no start line:Expecting: TRUSTED CERTIFICATE)
test_config | nginx: [emerg] PEM_read_bio_X509_AUX("/etc/ssl/certs/wildcard.........de.crt") failed (SSL: error:0906D06C:PEM routines:PEM_read_bio:no start line:Expecting: TRUSTED CERTIFICATE)
test_config | nginx: configuration file /etc/nginx/nginx.conf test failed
test_config exited with code 1

# do some editing and boot up
docker-compose up
Starting test_config ...
Starting test_config ... done
Attaching to test_config
test_config | nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
test_config | nginx: configuration file /etc/nginx/nginx.conf test is successful
test_config exited with code 0
```
