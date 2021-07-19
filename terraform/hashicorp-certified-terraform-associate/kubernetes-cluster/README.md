# Lets run a simple nginx pod via terraform
```
terraform init
terraform plan
terraform apply -auto-approve
```

## Check status
```
k get all -o wide

```

## Check connectivity
```
k run --rm --restart Never -it busybox --image busybox \
    -- nc -z -v -w1 tf-k8s-service 80
```

### Output should be
```
tf-k8s-service (10.108.189.180:80) open
pod "busybox" deleted
```

## Observe the state
```
terraform state list
terraform state show kubernetes_deployment.tf-k8s-deployment
```

## Delete everything
```
terraform destroy
```
