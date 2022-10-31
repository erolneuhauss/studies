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

variable "vpcName" {
  type = string
  default = "TerraformVPC"
}

resource "aws_vpc" "myvpc" {
  cidr_block = "198.168.0.0/24"

  tags = {
    Name = var.vpcName
  }
}

output "vpcid" {
  value = aws_vpc.myvpc.id
}

