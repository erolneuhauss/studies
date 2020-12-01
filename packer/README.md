# Packer
## build
```
packer build -var 'tag=0.0.1' packer.json
```

## run produced image
```
docker run --rm --name nodejs -dt -p 80:3000 \
  --entrypoint "/usr/local/bin/node" \
  readytalk/nodejs:0.0.1 /var/code/bin/www
```

