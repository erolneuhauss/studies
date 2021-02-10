k rollout history deployment nginx-deploy
ls -lh /etc/kubernetes/manifests/etcd.yaml
k create role developer --resource=pods --verb=create,list,get,update,delete --namespace=development
k -n development auth can-i --as=john update pods
k expose pod nginx-resolver --name=nginx-resolver-service --port=80 --target-port=80 --type=ClusterIP
k run --rm -it busybox --image=busybox:1.28 --restart Never -- wget --spider --timeout=1 nginx-resolver-service
k run --rm -it busybox --image=busybox:1.28 --restart Never -- nslookup 10-244-1-3.default.pod.cluster.local
k run --rm -it busybox --image=busybox:1.28 --restart Never -- nslookup nginx-resolver-service
