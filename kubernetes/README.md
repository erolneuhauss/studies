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

