# Testing JAVA 7 and 8 against tomcat 7 and 8
## Requirements
### Download Java7 and Java8 from Oracle and place it relativ to current directory
```
mkdir -p $(PWD)/usr/local/src
ls -lh $(PWD)/usr/local/src
jdk-7u80-linux-x64.tar.gz  jdk-8u121-linux-x64.tar.gz
```

### Build
```
IMAGE="eneuhauss/mycentos"

for java in java7 java8; do
    docker build -f Dockerfile.${java} -t ${IMAGE}:${java} .
    for tomcat in tomcat7 tomcat8; do
        docker build -f Dockerfile.${java}.${tomcat} -t ${IMAGE}:${java}${tomcat} .
    done
done
```
