# Puppet 5 on Openshift
## Prerequisites
### Installation
```
brew info openshift-cli
brew install openshift-cli
```

### Prepare docker images for openshift: docker image must be able to run as a daemon
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
<output>
-- Checking OpenShift client ... OK
-- Create Docker machine ...
   Creating docker-machine openshift
-- Checking Docker client ... OK
-- Checking Docker version ...
   WARNING: Cannot verify Docker version
-- Checking for existing OpenShift container ... OK
-- Checking for openshift/origin:v1.5.1 image ...
   Pulling image openshift/origin:v1.5.1
   Pulled 0/3 layers, 3% complete
   Pulled 1/3 layers, 87% complete
   Pulled 2/3 layers, 93% complete
   Pulled 3/3 layers, 100% complete
   Extracting
   Image pull complete
-- Checking Docker daemon configuration ... OK
-- Checking for available ports ... OK
-- Checking type of volume mount ...
   Using Docker shared volumes for OpenShift volumes
-- Creating host directories ... OK
-- Finding server IP ...
   Using docker-machine IP 192.168.99.100 as the host IP
   Using 192.168.99.100 as the server IP
-- Starting OpenShift container ...
   Creating initial OpenShift configuration
   Starting OpenShift using container 'origin'
   Waiting for API server to start listening
   OpenShift server started
-- Adding default OAuthClient redirect URIs ... OK
-- Installing registry ... OK
-- Installing router ... OK
-- Importing image streams ... OK
-- Importing templates ... OK
-- Login to server ... OK
-- Creating initial project "myproject" ... OK
-- Removing temporary directory ... OK
-- Checking container networking ... OK
-- Server Information ...
   OpenShift server started.
   The server is accessible via web console at:
       https://192.168.99.100:8443

   You are logged in as:
       User:     developer
       Password: developer

   To login as administrator:
       oc login -u system:admin
   OpenShift server started.

docker-machine ls
oc cluster down --docker-machine='openshift'
oc cluster up --docker-machine='openshift'
```

### Basic Concept
  * create project (myproject is created per default)
  * add image to project - that creates deployment, pods and service
  * add route to service (routes and dns configuration takes a few minutes)

#### adding an image
```
oc import-image hello-openshift --from='docker.io/openshift/hello-openshift:latest' --confirm
```

#### create an output first (-o yaml)
```
oc new-app hello-openshift -i "hello-openshift" -o yaml
```
[examples/oc-new-app-hello-openshift.yaml](./examples/oc-new-app-hello-openshift.yaml)

#### create a new app
```
oc new-app hello-openshift -i "hello-openshift"
```

#### alternativ: create an app from yaml
```
oc create -f ./examples/oc-new-app-hello-openshift.yaml
# make changes to the .yaml file
oc apply -f ./examples/oc-new-app-hello-openshift.yaml
```
[examples/oc-new-app-hello-openshift.yaml](./examples/oc-new-app-hello-openshift.yaml)

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

#### Delete my app completly
```
oc delete all -l app=hello-openshift
oc delete route hello-openshift
oc delete imagestreams hello-openshift
```

#### HA-Proxy is configured to work with port 80/443 only
Therefore and by nature Puppetmaster is not suitable to work in an
openshift cluster.


### login into and work with oc cluster
```
oc --help
oc status -v
oc login -u system:admin
oc import-image hello-openshift --from='docker.io/openshift/hello-openshift:latest' --confirm
oc get apps
oc get dc
oc get deploy
oc get is
oc get pods
oc get projects
oc get services
```

## Links
  * [https://www.openshift.org/](https://www.openshift.org/)
  * [https://github.com/openshift/origin/blob/master/docs/cluster_up_down.md](https://github.com/openshift/origin/blob/master/docs/cluster_up_down.md)
  * [https://github.com/openshift/training](https://github.com/openshift/training)
  * [https://developers.openshift.com/getting-started/osx.html](https://developers.openshift.com/getting-started/osx.html)
