provider "aws" {
  region = "eu-central-1"
}

resource "aws_key_pair" "ubuntu" {
  key_name   = "ubuntu"
  public_key = file("key.pub")
}

resource "aws_security_group" "ubuntu" {
  name        = "ubuntu-security-group"
  description = "SSH traffic"

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["2.244.58.194/32"]
  }

  tags = {
    Name = "my-first-tf-node"
  }
}

resource "aws_instance" "ubuntu" {
  key_name      = aws_key_pair.ubuntu.key_name

  # ubuntu-minimal/images/hvm-ssd/ubuntu-focal-20.04-amd64-minimal-20210511
  ami = "ami-012e962955fb5a689"

  instance_type = "t3.micro"
  vpc_security_group_ids = [
    aws_security_group.ubuntu.id
  ]

  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file("key")
    host        = self.public_ip
  }

  tags = {
    Name = "my-first-tf-node"
  }
}

resource "aws_eip" "ubuntu" {
  vpc      = true
  instance = aws_instance.ubuntu.id
}

