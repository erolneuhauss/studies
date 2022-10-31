terraform {
  required_version = ">= 1.0"
}

terraform {
  required_providers {
    aws = "~> 2.7"
  }
}

provider "aws" {
  region = "eu-central-1"
}

module "db" {
  source = "./db"
}

module "web" {
  source = "./web"
}

output "PublicIP" {
  value = module.web.pub_ip
}
 
output "PrivateIP" {
  value = module.db.PrivateIP
}
