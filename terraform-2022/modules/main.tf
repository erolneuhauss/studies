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

module "ec2module" {
  source = "./ec2"
  ec2name = "Name From Module"
}

output "module_output" {
  value = module.ec2module.ec2id
}
