# Prerequisits
## Store AWS config and credentials (non-production)
```
~/.aws/config
~/.aws/credentials
```

## Get your own public IP (for SSH onto aws instance)
```
dig +short myip.opendns.com @resolver1.opendns.com
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

## Check instance and retrieve public dns
```
terraform state list
terraform state show aws_eip.ubuntu
```

## curl
```
curl ec2-xx-xx-xx-xx.eu-central-1.compute.amazonaws.com
```
