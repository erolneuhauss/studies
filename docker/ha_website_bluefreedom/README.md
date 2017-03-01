# Nginx proxied and load balanced website
## website
```
wget http://static.oswd.org/designs/3682/bluefreedom3.zip
mkdir -p /home/user/docker/bluefreedom/var/www/html
unzip bluefreedom3.zip -d /home/user/docker/bluefreedom/var/www/html
```
## docker containers
### build
TODO: do it with a Dockerfile instead of doing it manualy
### start
```
docker run -itd --name web1 -v /home/user/docker/bluefreedom/var/www/html:/var/www/html:z -p 8081:80 eneuhauss/mycentos:6v1baseweb /bin/bash
docker run -itd --name web2 -v /home/user/docker/bluefreedom/var/www/html:/var/www/html:z -p 8082:80 eneuhauss/mycentos:6v1baseweb /bin/bash
docker run -itd --name web3 -v /home/user/docker/bluefreedom/var/www/html:/var/www/html:z -p 8083:80 eneuhauss/mycentos:6v1baseweb /bin/bash
```
TODO: do it with docker-compose instead of manualy

Hint:
```
version: '2'
services:
  web1:
    image: "eneuhauss/mycentos:6v1baseweb"
    ports:
      - "8081:80"
    volumes:
      - /home/user/docker/bluefreedom/var/www/html:/var/www/html
  web2:
    image: "eneuhauss/mycentos:6v1baseweb"
    ports:
      - "8082:80"
    volumes:
      - /home/user/docker/bluefreedom/var/www/html:/var/www/html
  web2:
    image: "eneuhauss/mycentos:6v1baseweb"
    ports:
      - "8083:80"
    volumes:
      - /home/user/docker/bluefreedom/var/www/html:/var/www/html
```

## nginx on host
```
nginx-1.10.2-1.el7.x86_64
```
### Configuration bluefreedom.conf
```
upstream containerapp {
	server 172.31.117.211:8081;
	server 172.31.117.211:8082;
	server 172.31.117.211:8083;
}
server {
	listen *:80;
	server_name eneuhauss1.mylabserver.com;
	index index.html index.htm index.php
	access_log /var/log/nginx/containerapp_access;
	error_log /var/log/nginx/containerapp_error;

	location / {
		proxy_pass http://containerapp;
	}
}
```

# Problems
## SELinux
SElinux denied nginx access on localhost port 8081-8031

Solution:
```
sudo grep nginx  /var/log/audit/audit.log | grep denied | sudo audit2allow -M proxypassnginx
sudo semodule -i proxypassnginx.pp
```
SElinux denied access on mounted volume
```
ls: cannot open directory /var/www/html: Permission denied
```
Solution
* ```-v /home/user/docker/bluefreedom/var/www/html:/var/www/html:z``` or
* run ```chcon -Rt svirt_sandbox_file_t /home/user/docker/bluefreedom/var/www/html``` first
