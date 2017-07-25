# studies
This is just a simple collection of my work which includes learning things
and make things work

## Table of contents
* [ansible](#ansible)
* [bash](#bash)
* [docker](#docker)
* [git](#git)
* [go](#go)
* [puppet](#puppet)
* [python](#python)
* [vagrant](#vagrant)

## ansible

## bash
### [basics](./bash)
* [Hello World](./bash/hello-world.sh)

## docker
### [Dockerfile](./docker/latex_minion)
CentOS7 Tex Live 2016 basic scheme Installation with koma-script and german language support
Docker commands:
```
docker pull eneuhauss/latex_minion
docker run --name devlatex -v $(pwd)/docker/latex_minion:/work:Z -it eneuhauss/latex_minion:v1 /bin/bash
```
(requires directory ```docker/latex_minion``` from this repository)

Inside the container:
```
cd /work
pdflatex job_appl_sample.tex
```
 
## git

## go
### [basics](./go)
* [Get Started](./go/01_get_started)
* [Numeral Systems](./go/02_numeral_systems)
* [Variables](./go/03_variables)
* [Scope](./go/04_scope)

## [puppet](./puppet)
  * [puppet5](./puppet/projects/puppet5) -- most advanced puppet in this repo so far
## python
## vagrant
## and more
