# Prerequisits
## Store AWS config and credentials (non-production)
```
~/.aws/config
~/.aws/credentials
```

# Workflow
Create `main.tf` and SSH-Key-pair and run
```
terraform init
terraform validate
terraform fmt
terraform plan
terraform apply -auto-approve
```
