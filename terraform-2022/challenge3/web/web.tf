resource "aws_instance" "ec2WEB" {
  ami = "ami-070b208e993b59cea"
  instance_type = "t3.nano"
  security_groups = [module.sg.sg_name]
  user_data = file("./web/server-script.sh")

  tags = {
    Name = "Web Server"
  }
}

output "pub_ip" {
  value = module.eip.PublicIP
}

module "eip" {
  source = "../eip"
  instance_id = aws_instance.ec2WEB.id
}

module "sg" {
  source = "../sg"
}
