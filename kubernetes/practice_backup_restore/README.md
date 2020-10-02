# Backup and Restore
background [https://discuss.kubernetes.io/t/etcd-backup-and-restore-management/11019/5]

## Test and snapshot
```
export ETCDCTL_API=3 
etcdctl --endpoints "https://127.0.0.1:2379" --cert=/etc/kubernetes/pki/etcd/server.crt --cacert=/etc/kubernetes/pki/etcd/ca.crt --key=/etc/kubernetes/pki/etcd/server.key endpoint status

mv /etc/kubernetes/manifests/kube-apiserver.yaml .

etcdctl --endpoints "https://127.0.0.1:2379" --cert=/etc/kubernetes/pki/etcd/server.crt --cacert=/etc/kubernetes/pki/etcd/ca.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save snapshot.db

```
## restore

```
etcdctl --endpoints="https://127.0.0.1:2379" --name=master --data-dir=/var/lib/etcd-from-backup --initial-cluster=master=https://127.0.0.1:2380 --initial-advertise-peer-urls=https://127.0.0.1:2380 --initial-cluster-token=etcd-cluster-1 --cert=/etc/kubernetes/pki/etcd/server.crt --cacert=/etc/kubernetes/pki/etcd/ca.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot restore snapshot.db
```

## edit /etc/kubernetes/manifests/etcd.yaml
```
mv /etc/kubernetes/manifests/etcd.yaml .
grep backup /etc/kubernetes/manifests/etcd.yaml
    - --data-dir=/var/lib/etcd-from-backup
    - mountPath: /var/lib/etcd-from-backup
      path: /var/lib/etcd-from-backup

grep token /etc/kubernetes/manifests/etcd.yaml
    - --initial-cluster-token=etcd-cluster-1

mv etcd.yaml /etc/kubernetes/manifests/
mv kube-apiserver.yaml /etc/kubernetes/manifests/
```
