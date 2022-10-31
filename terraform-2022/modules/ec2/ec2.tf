variable "ec2name" {
  type = string
}

resource "aws_instance" "ec2" {
  ami = "ami-070b208e993b59cea"
  instance_type = "t3.nano"
  tags = {
    Name = var.ec2name
  }
}

output "ec2id" {
  value = aws_instance.ec2.id
}

