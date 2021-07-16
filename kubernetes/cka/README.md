# Kubernetes
# a kubeconfig is produced
```
export KUBECONFIG=kubeconfig_<your_name>
```

## check connectability with wget
```
k run --labels=name=internal --rm --restart Never -it busybox --image=busybox \
-- wget --spider --timeout=1 payroll-service.default.svc.cluster.local:8080
```

## check connectability with nc
```
k run --labels=name=internal --rm --restart Never -it busybox --image=busybox \
-- nc -z -v -w1 db-service 3306
```

## checkout aliases
```
zprezto-contrib/kubectl/alias.zsh
```

## custom aliases
```
kcnc is an alias for kubectl run --rm --restart Never --stdin --tty busybox --image arm64v8/busybox -- nc -z -v -w1 
kcwget is an alias for kubectl run --rm --restart Never --stdin --tty busybox --image arm64v8/busybox -- wget --spider --timeout=1
```

### side note to https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests
In order to open an connectivity window start the webcolor deployment and use the web browser on exposed NodePort e.g. 30082 add +1 to the subdomain
when quiz: https://2886795279-8080-kitek06h.environments.katacoda.com/#!/viewExam
than webcolor app on : https://2886795280-30082-kitek06h.environments.katacoda.com

## Create Wordpress Site on AWS
### Create wordpress backend
```
k -n ene create deploy mysql --image=mysql --dry-run=client -o yaml > mysql_deploy.yaml
```

Edit environment variables:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: backend
  name: mysql
  namespace: ene
spec:
  replicas: 1
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
        - name: mysql
          image: mysql
          ports:
          - containerPort: 3306
          env:
            - name : MYSQL_ROOT_PASSWORD
              value: my-secret-pw
            - name : MYSQL_DATABASE
              value: wordpress
            - name: MYSQL_USER
              value: wordpress
            - name: MYSQL_PASSWORD
              value: password
```

Apply:
```
k -n ene apply -f mysql_deploy.yaml
```

### Create wordpress frontend
```
k -n ene create deploy wordpress --image=wordpress --dry-run=client -o yaml > wordpress_deploy.yaml
```

Edit environment variables:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: frontend
  name: wordpress
  namespace: ene
spec:
  replicas: 1
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
        - name: wordpress
          image: wordpress
          ports:
          - containerPort: 80
          env:
            - name : WORDPRESS_DB_HOST
              value: mysql
            - name: WORDPRESS_DB_USER
              value: wordpress
            - name: WORDPRESS_DB_PASSWORD
              value: password
            - name : WORDPRESS_DB_NAME
              value: wordpress
```

Apply:
```
k -n ene apply -f wordpress_deploy.yaml
```

### create wordpress service
```
k -n ene expose deployment.apps/mysql --dry-run=client -o yaml > mysql_service.yaml
```
Check yaml and apply as usual

### Expose wordpress frontend
```
k -n ene expose deployment.apps/wordpress --dry-run=client -o yaml > wordpress_service.yaml
```

Change type to loadbalancer
```
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: null
  labels:
    app: frontend
  name: wordpress
  namespace: ene
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: frontend
  type: LoadBalancer
```
Apply as usual

Login to your site, after you know your URL by
```
k -n ene get all -o wide
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

# creates a corresponding service
k expose deployment --dry-run=client --output yaml --image nginx nginx


# LoadBalancer
service-nginx.yaml:
apiVersion: v1
kind: Service
metadata:
  labels:
    app: nginx
  name: nginx
spec:
  selector:
    app: nginx
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  type: LoadBalancer

k -n ene describe service/nginx
# provides an external IP. Browse via Webbrowser after a while (DNS takes a couple of minutes)

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
