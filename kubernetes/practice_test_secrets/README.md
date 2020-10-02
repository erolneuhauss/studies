# Practice Test Secrets

```
k create secret generic db-secret --dry-run=client -o yaml --from-literal=DB_Host=sql01 --from-literal=DB_User=root --from-literal=DB_Password=password123 > db-secret--from-literal.yaml
```

or

```
cat db-secret.env
DB_Host=sql01
DB_Password=password123
DB_User=root

k create secret generic db-secret --dry-run=client -o yaml --from-env-file=db-secret.env > db-secret--from-env-file.yaml
```
or
```
mkdir db-secret

# use printf instead of echo (printf omits newline)
printf sql01 > db-secret/DB_Host
printf root > db-secret/DB_User
printf password123 > db-secret/DB_Password
k create secret generic db-secret --dry-run=client -o yaml --from-file=db-secret
```

use within a pod
```
cat webapp-run-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    name: webapp-pod
  name: webapp-pod
spec:
  containers:
  - name: webapp
    image: kodekloud/simple-webapp-mysql
    envFrom:
    - secretRef:
        name: db-secret
```
