variable "wide_open" {
  type    = list(any)
  default = ["0.0.0.0/0"]
}

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
    cidr_blocks = var.wide_open
  }

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.my_pub_ip
  }

  ingress {
    description = "allow traffic from TCP/80"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = var.wide_open
  }

  tags = {
    Name = "my-first-tf-node"
  }
}

resource "aws_instance" "ubuntu" {
  key_name = aws_key_pair.ubuntu.key_name

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

  provisioner "remote-exec" {
    inline = [
      "sudo apt update && sudo apt upgrade -y",
      "sudo apt install -y apache2 && sudo systemctl enable --now apache2",
      "echo '<h1><center>My Test Website With Help From Terraform Provisioner</center></h1>' | sudo tee /var/www/html/index.html"
    ]
  }

  tags = {
    Name = "my-first-tf-node"
  }
}

resource "aws_eip" "ubuntu" {
  vpc      = true
  instance = aws_instance.ubuntu.id
}

output "instance_ip" {
  description = "VM's public_ip"
  value       = aws_instance.ubuntu.public_ip
}
