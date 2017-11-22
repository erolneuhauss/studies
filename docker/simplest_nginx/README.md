# Run nginx
## Steps
### download image
docker pull nginx

### create container to test
docker run --name nginx -p 80:80 -d nginx

### curl url
Result should be HTTP/1.1 200 OK

```
curl -v erol01
* Rebuilt URL to: erol01/
*   Trying 10.1.103.31...
* TCP_NODELAY set
* Connected to erol01 (10.1.103.31) port 80 (#0)
> GET / HTTP/1.1
> Host: erol01
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: nginx/1.13.6
< Date: Wed, 22 Nov 2017 15:50:06 GMT
< Content-Type: text/html
< Content-Length: 612
< Last-Modified: Thu, 14 Sep 2017 16:35:09 GMT
< Connection: keep-alive
< ETag: "59baafbd-264"
< Accept-Ranges: bytes
<
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
[...]
```

### Stop and remove container
```
docker stop nginx
docker rm nginx
```


### mount html volume and simple index.html

```
cat > index.html << EOF
<html>
	<body>
		Hi there
	</body>
</html>
EOF

docker run --name nginx -v $(pwd):/usr/share/nginx/html -p 80:80 -d nginx

curl -v erol01
* Rebuilt URL to: erol01/
*   Trying 10.1.103.31...
* TCP_NODELAY set
* Connected to erol01 (10.1.103.31) port 80 (#0)
> GET / HTTP/1.1
> Host: erol01
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: nginx/1.13.6
< Date: Wed, 22 Nov 2017 15:53:38 GMT
< Content-Type: text/html
< Content-Length: 43
< Last-Modified: Tue, 21 Nov 2017 14:24:32 GMT
< Connection: keep-alive
< ETag: "5a143720-2b"
< Accept-Ranges: bytes
<
<html>
	<body>
		Hi there
	</body>
</html>
```
