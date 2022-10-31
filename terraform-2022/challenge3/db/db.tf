resource "aws_instance" "ec2DB" {
  ami = "ami-070b208e993b59cea"
  instance_type = "t3.nano"

  tags = {
    Name = "DB Server"
  }
}

output "PrivateIP" {
  value = aws_instance.ec2DB.private_ip
}
