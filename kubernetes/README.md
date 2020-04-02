kubectl version --client
mv ~/Downloads/kubeconfig-k8s04 .
mkdir -p kubernetes-hackathon_2020-04-02
cd kubernetes-hackathon_2020-04-02
cat kubeconfig-k8s04
brew install int128/kubelogin/kubelogin
cp ~/.kube/config ~/.kube/config.old
mv kubeconfig-k8s04 ~/.kube/config
kubectl config view
kubectl get pod
kubectl cluster-info
alias k='kubectl'
k cluster-info
