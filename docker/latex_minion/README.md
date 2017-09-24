# CentOS 7 Tex Live 2017 basic scheme Installation with koma-script and german language support
## Idea
I wanted to be able to run a ```pdflatex``` in a docker container.
I wanted TexLive 2017 somewhat portable via docker. This way I did not need to install
TexLive on every system I am working with. Instead I would just run that container
in order to produce pdf files. 

## Build
```
docker-compose build
```

## Edit docker-compose.yaml and run container
```
docker-compose up
```
