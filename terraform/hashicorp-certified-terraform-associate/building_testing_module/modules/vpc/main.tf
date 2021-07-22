provider "aws" {
  region = var.region
}

resource "aws_vpc" "this" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "this" {
  vpc_id     = aws_vpc.this.id
  cidr_block = "10.0.1.0/24"
}

# this results in 
# Error describing SSM parameter (/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2): AccessDeniedException: User: arn:aws:iam::xxx:user/xxx is not authorized to perform: ssm:GetParameter on resource: arn:aws:ssm:eu-central-1::parameter/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
# data "aws_ssm_parameter" "this" {
  # name = "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2"
# }
