
  655* docker build  -f Dockerfile.puppet 
  784* cp Dockerfile.puppet Dockerfile.oc-puppe
# Puppet 5 on Openshift
## Lose history
```
docker build -f Dockerfile.node1 -t eneuhauss/project_puppet5_node1:1.2 .
docker run -d eneuhauss/project_puppet5_puppetmaster:1.2
docker push eneuhauss/project_puppet5_puppetmaster:1.2
oc cluster up
oc --help
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
oc get service
oc get services
oc help
oc import-image project_puppet5_puppetmaster:1.2 --from='docker.io/eneuhauss/project_puppet5_puppetmaster:1.2' --confirm
oc login -u system:admin
oc status
oc status -v
oc cluster down
```
