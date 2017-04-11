#!/bin/bash
# TASK: produce six images:
# eneuhauss/mycentos:java7
# eneuhauss/mycentos:java7tomcat7
# eneuhauss/mycentos:java7tomcat8
# eneuhauss/mycentos:java8
# eneuhauss/mycentos:java8tomcat7
# eneuhauss/mycentos:java8tomcat8

# SOLUTION A: instead of typing:
# docker build -f Dockerfile.java7 -t eneuhauss/mycentos:java7 .
# docker build -f Dockerfile.java7.tomcat7 -t eneuhauss/mycentos:java7tomcat7 .
# docker build -f Dockerfile.java7.tomcat8 -t eneuhauss/mycentos:java7tomcat8 .
# docker build -f Dockerfile.java8 -t eneuhauss/mycentos:java8 .
# docker build -f Dockerfile.java8.tomcat7 -t eneuhauss/mycentos:java8tomcat7 .
# docker build -f Dockerfile.java8.tomcat8 -t eneuhauss/mycentos:java8tomcat8 .

# SOLUTION B: use a for loop
IMAGE="eneuhauss/mycentos"
for java in java7 java8; do
    docker build -f Dockerfile.${java} -t ${IMAGE}:${java} .
    for tomcat in tomcat7 tomcat8; do
        docker build -f Dockerfile.${java}.${tomcat} -t ${IMAGE}:${java}${tomcat} .
    done
done
