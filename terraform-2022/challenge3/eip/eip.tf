variable "instance_id" {
  type = string
}

resource "aws_eip" "web_ip" {
  # instance = aws_instance.ec2WEB.id
  instance = var.instance_id
}

output "PublicIP" {
  value = aws_eip.web_ip.public_ip
}
