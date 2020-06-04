# Hackathon notes from April 2nd 2020

kubectl version --client
brew install int128/kubelogin/kubelogin
rm ~/.kube/config
touch ~/.kube/config
chmod 400 ~/.kube/config
ls -lh ~/.kube/config
mv ~/Downloads/kubeconfig-k8s04 ~/.kube/
export KUBECONFIG=~/.kube/kubeconfig-k8s04
kubectl config view
kubectl cluster-info
kubectl get pod
alias k='kubectl'
k cluster-info
source <(kubectl completion zsh)
k <tab> get <tab> ns
k get pod -n kube-system
k get services -n kube-system

k create deployment --dry-run=client --output=yaml --image busybox foo
k create deployment --dry-run=client --output=yaml --image nginx nginx
k expose deployment --dry-run=client --output yaml --image nginx nginx

k -n ene apply -f deployment-nginx.yaml
k -n ene apply -f service-nginx.yaml

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

watch -d -n2 'k get pods -o wide'

k -n ene port-forward nginx-79f5849f8d-q9flr 8080:80

k -n ene delete deployment.apps/nginx
k -n ene delete service/nginx


## Testing:

```
parallel --jobs 1000 ./my_curl.sh ::: {1..1000}

#!/bin/bash

curl 127.0.0.1:8080 -o /dev/null
```