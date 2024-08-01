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

variable "ingressrules" {
  type = list(number)
  default = [80,443]
}

variable "egressrules" {
  type = list(number)
  default = [80,443,25,3306,53,8080]
}

resource "aws_instance" "ec2" {
  ami = "ami-070b208e993b59cea"
  instance_type = "t3.nano"
  security_groups = [aws_security_group.webtraffic.name]
}

resource "aws_eip" "elasticip" {
  instance = aws_instance.ec2.id
}

resource "aws_security_group" "webtraffic" {
  name = "Allow https"

  dynamic "ingress" {
    iterator = port
    for_each = var.ingressrules
    content {
    from_port = port.value
    to_port = port.value
    protocol = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
    }
  }

  dynamic "egress" {
    iterator = port
    for_each = var.egressrules
    content {
    from_port = port.value
    to_port = port.value
    protocol = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
    }
  }

}
output "ec2id" {
  value = aws_instance.ec2.id
}

output "EIP" {
  value = aws_eip.elasticip.public_ip
}