# Want to test upload files with nginx as proxy
## build
docker-compose build

## run
docker-compose up

## Example
```
docker-compose up
[...]

curl -F "fileupload=@5M_file"  http://127.0.0.1/upload/upload.php
<pre>
Array
(
    [fileupload] =&gt; Array
        (
            [name] =&gt; 5M_file
            [type] =&gt; application/octet-stream
            [tmp_name] =&gt; /tmp/phpadOpKA
            [error] =&gt; 0
            [size] =&gt; 5242880
        )

)
</pre>

curl -F "fileupload=@10M_file"  http://127.0.0.1/upload/upload.php
<html>
<head><title>413 Request Entity Too Large</title></head>
<body bgcolor="white">
<center><h1>413 Request Entity Too Large</h1></center>
<hr><center>nginx</center>
</body>
</html>

curl -F "fileupload=@10M_file"  http://127.0.0.1/upload/20mfiles/upload.php
<pre>
Array
(
    [fileupload] =&gt; Array
        (
            [name] =&gt; 10M_file
            [type] =&gt; application/octet-stream
            [tmp_name] =&gt; /tmp/phpIEKFee
            [error] =&gt; 0
            [size] =&gt; 10485760
        )

)
</pre>

curl -F "fileupload=@20M_file"  http://127.0.0.1/upload/20mfiles/upload.php
<html>
<head><title>413 Request Entity Too Large</title></head>
<body bgcolor="white">
<center><h1>413 Request Entity Too Large</h1></center>
<hr><center>nginx</center>
</body>
</html>
```
