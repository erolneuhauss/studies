provider "aws" {
  region = "eu-central-1"

}

resource "aws_instance" "vm" {
  # ubuntu-minimal/images/hvm-ssd/ubuntu-focal-20.04-amd64-minimal-20210511
  ami = "ami-012e962955fb5a689"
  instance_type = "t3.micro"
  tags = {
    Name = "my-first-tf-node"
  }
}
