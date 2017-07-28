# Puppet 5 on Openshift
## Prerequisites
### Installation
```
brew info openshift-cli
```

## Prepare docker images for openshift: docker image must be able to run as a daemon
```
docker build -f Dockerfile.node1 -t eneuhauss/project_puppet5_node1:1.2 .
docker run -d eneuhauss/project_puppet5_puppetmaster:1.2
docker push eneuhauss/project_puppet5_puppetmaster:1.2
```
## oc cluster
### create oc cluster on VirtualBox
oc cluster must run on a Mac OS X in VirtualBox instead on naked host
```
oc cluster up --forward-ports=true --create-machine=true
docker-machine ls
oc cluster down --docker-machine='openshift'
oc cluster up --docker-machine='openshift'
<output>
   OpenShift server started.
   The server is accessible via web console at:
       https://192.168.99.100:8443

   You are logged in as:
       User:     developer
       Password: developer

   To login as administrator:
       oc login -u system:admin
```

### Basic Concept
  * create project
  * add image to project - that creates deployment, pods and service
  * add route to service (routes and dns configuration takes a few minutes)

### openshift/hello-openshift
#### Container/Pods
```
CONTAINER: HELLO-OPENSHIFT
Image: openshift/hello-openshift
Ports: 8080/TCP , 8888/TCP
```

#### Service
```
Selectors: deploymentconfig=hello-openshift
Type: ClusterIP
IP: 172.30.206.170
Hostname: hello-openshift.myproject.svc
Session affinity: None
```

#### Route
```
http://hello-openshift-myproject.192.168.99.100.xip.io

Path: none
Service: hello-openshift
Target Port: 8080-tcp
This target port will route to Service Port 8080 → Container Port 8080 (TCP).
```

#### Test my app on my host
```
curl http://hello-openshift-myproject.192.168.99.100.xip.io
<output>
Hello OpenShift!
```

#### HA-Proxy is configured to work with port 80/443 only
Therefore and by nature Puppetmaster is not suitable to work in an
openshift cluster.


### login into and work with oc cluster
```
oc --help
oc status -v
oc login -u system:admin
oc import-image puppet --from='docker.io/eneuhauss/project_puppet5_puppetmaster:1.2' --confirm
oc import-image hello-openshift --from='docker.io/openshift/hello-openshift:latest' --confirm
oc create -f puppet-deployment.yaml
oc create -f puppet-service.yaml
oc apply -f puppet-deployment.yaml
oc apply -f puppet-service.yaml
oc delete DeploymentConfig puppet
oc get DeploymentConfig
oc get app
oc get apps
oc get dc
oc get deploy
oc get is
oc get pods
oc get projects
oc get services
```

## Links
[https://www.openshift.org/](https://www.openshift.org/)
[https://github.com/openshift/origin/blob/master/docs/cluster_up_down.md](https://github.com/openshift/origin/blob/master/docs/cluster_up_down.md)
[https://github.com/openshift/training](https://github.com/openshift/training)
[https://developers.openshift.com/getting-started/osx.html](https://developers.openshift.com/getting-started/osx.html)
