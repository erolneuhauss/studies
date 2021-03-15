# Add another worker node
## Retrieve discovery token ca cert hash
```
kubectl config view --minify --raw --output 'jsonpath={..cluster.certificate-authority-data}' \\
  | base64 -d \\
  | openssl x509 -out - \\
  | openssl rsa -pubin -outform der 2>/dev/null \\
  | openssl dgst -sha256 -hex | sed 's/^.* //'
```

## Create join token
`kubeadm create token`

## Run on worker node
`kubeadm join 192.168.178.51:6443 --token $TOKEN --discovery-token-ca-cert-hash sha256:$DISCOVERY_HASH`

