variable "main_region" {
  type    = string
  default = "eu-central-1"
}

provider "aws" {
  region = var.main_region
}

module "vpc" {
  source = "./modules/vpc"
  region = var.main_region
}

resource "aws_instance" "my-instance" {
  ami           = "ami-012e962955fb5a689"
  subnet_id     = module.vpc.subnet_id
  instance_type = "t2.micro"
}
