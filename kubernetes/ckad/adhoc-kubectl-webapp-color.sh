#!/usr/bin/env bash

kubectl delete po webapp-color
kubectl delete svc webapp-color
kubectl delete ingress webapp-color-ingress

kubectl run webapp-color --image registry.fritz.box/my/arm64/python:3.6-alpine --env APP_COLOR=blue --labels app=webapp-color
# kubectl run webapp-color --image registry.fritz.box/my/arm64/python:3.6-alpine --labels app=webapp-color -- --color=pink
kubectl expose pod webapp-color --target-port 8080 --port 80 --selector app=webapp-color

cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: webapp-color-ingress
  namespace: default
spec:
  rules:
  - host: webapp-color.fritz.box
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service: 
            name: webapp-color
            port:
              number: 80
status:
  loadBalancer: {}
EOF
