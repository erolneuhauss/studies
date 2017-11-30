# Want to test upload files with nginx/php
## build
docker-compose build

## run
docker-compose up

## Example
```
docker-compose up
[...]

curl -F "fileupload=@50M_file"  http://127.0.0.1/upload.php
<pre>
Array
(
    [fileupload] =&gt; Array
        (
            [name] =&gt; 50M_file
            [type] =&gt; application/octet-stream
            [tmp_name] =&gt; /tmp/phpadOpKA
            [error] =&gt; 0
            [size] =&gt; 52428800
        )

)
</pre>

curl -F "fileupload=@100M_file"  http://127.0.0.1/upload.php
<html>
<head><title>413 Request Entity Too Large</title></head>
<body bgcolor="white">
<center><h1>413 Request Entity Too Large</h1></center>
<hr><center>nginx</center>
</body>
</html>

curl -F "fileupload=@100M_file"  http://127.0.0.1/upload/upload.php
<pre>
Array
(
    [fileupload] =&gt; Array
        (
            [name] =&gt; 100M_file
            [type] =&gt; application/octet-stream
            [tmp_name] =&gt; /tmp/phpIEKFee
            [error] =&gt; 0
            [size] =&gt; 104857600
        )

)
</pre>

curl -F "fileupload=@500M_file"  http://127.0.0.1/upload/upload.php
<html>
<head><title>413 Request Entity Too Large</title></head>
<body bgcolor="white">
<center><h1>413 Request Entity Too Large</h1></center>
<hr><center>nginx</center>
</body>
</html>
```
