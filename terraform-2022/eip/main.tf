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

resource "aws_instance" "ec2" {
  ami = "ami-070b208e993b59cea"
  instance_type = "t3.nano"
}

resource "aws_eip" "elasticip" {
  instance = aws_instance.ec2.id
}

output "ec2id" {
  value = aws_instance.ec2.id
}

output "EIP" {
  value = aws_eip.elasticip.public_ip
}
