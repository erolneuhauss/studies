# Kubernetes
## terraform
```
cd <to the dir where your .tf's are>
terraform init
terraform plan
terraform apply
# a kubeconfig is produced
export KUBECONFIG=kubeconfig_<your_name>
```


## Hackathon notes from April 2nd 2020
kubernetes platform via aws existent (build with terraform)
### Configuration
```
kubectl version --client
brew install int128/kubelogin/kubelogin
rm ~/.kube/config
touch ~/.kube/config
chmod 400 ~/.kube/config
ls -lh ~/.kube/config
mv ~/Downloads/kubeconfig-k8s04 ~/.kube/
export KUBECONFIG=~/.kube/kubeconfig-k8s04
alias k='kubectl'
source <(kubectl completion zsh)
```

### Lookaround with kubectl
```
k <tab> get <tab> ns
k config view
k cluster-info
k get namespaces
k get po --all-namespaces -o=wide
k get pod -n kube-system
k get services -n kube-system
```

### Work with kubernetes (nginx and busybox)
```
k create namespace ene
# GEFAHR (namespace wird fixiert. Man vergisst of den context zu wechslen)
k config set-context --current --namespace=ene

k proxy
Starting to serve on 127.0.0.1:8001
# browse http://127.0.0.1:8001/api/v1/
# browse http://127.0.0.1:8001/api/v1/namespaces/ene/

k run nginx --image=nginx --port=80
k get pods -o wide
k get pods -o yaml > nging_pod.yaml
cat nging_pod.yaml
k delete pods nginx
kubectl apply -f https://k8s.io/examples/controllers/nginx-deployment.yaml
k describe deployments.apps
k get deployments.apps
k delete deployments.apps nginx-deployment

k create deployment --dry-run=client --output=yaml --image busybox foo
k create deployment --dry-run=client --output=yaml --image nginx nginx
k expose deployment --dry-run=client --output yaml --image nginx nginx

# browse http://127.0.0.1:8001/api/v1/namespaces/ene/pods
# browse http://127.0.0.1:8001/api/v1/namespaces/ene/services

k -n ene apply -f deployment-nginx.yaml
k -n ene apply -f service-nginx.yaml
k -n ene port-forward service/nginx 8080:80
# browse http://127.0.0.1:8080

k -n ene get pods -o wide
k -n ene exec -it nginx-86c57db685-km59p -- /bin/bash

k -n troubleshooting-5 logs -l app=busybox
k -n troubleshooting-5 logs -l app=busybox -p # previous
k -n troubleshooting-5 logs -l app=busybox -f # follow

k -n troubleshooting-1 get all
k -n troubleshooting-1 get pods
k -n troubleshooting-1 get event

k -n troubleshooting-1 describe pod broken-app
k -n troubleshooting-2 edit deployments.apps
k -n troubleshooting-3 create configmap config --dry-run=client

k -n troubleshooting-4 edit deployments.apps busybox
k -n troubleshooting-5 top pod
k -n troubleshooting-5 top node

watch -d -n2 'kubectl -n ene get pods -o wide'

k -n ene port-forward nginx-79f5849f8d-q9flr 8080:80

k -n ene delete deployment.apps/nginx
k -n ene delete service/nginx
```

## Testing:

```
parallel --jobs 1000 ./my_curl.sh ::: {1..1000}

#!/bin/bash

curl 127.0.0.1:8080 -o /dev/null
```
