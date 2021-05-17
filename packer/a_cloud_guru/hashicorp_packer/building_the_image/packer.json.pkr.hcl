packer {
  required_plugins {
    amazon = {
      version = ">= 0.0.1"
      source  = "github.com/hashicorp/amazon"
    }
  }
}

data "amazon-ami" "ubuntu" {
  filters = {
    name                = "ubuntu/images/*ubuntu-focal-20.04-amd64-server-*"
    root-device-type    = "ebs"
    virtualization-type = "hvm"
  }
  most_recent = true
  owners      = ["099720109477"]
}

locals { timestamp = regex_replace(timestamp(), "[- TZ:]", "") }

source "amazon-ebs" "ubuntu" {
  ami_name      = "packer-base-ami-${local.timestamp}"
  instance_type = "t2.micro"
  source_ami    = "${data.amazon-ami.ubuntu.id}"
  ssh_username  = "ubuntu"
}

build {
  sources = ["source.amazon-ebs.ubuntu"]
    provisioner "shell" {
        inline = ["sudo apt update -y && sudo apt upgrade -y"]
    }
    provisioner "file" {
        source = "files/"
        destination = "/tmp"
    }
    provisioner "shell" {
        scripts = [
            "app-init.sh",
            "scripts/metrics.sh"
        ]
    }
}

