terraform {
  required_version = ">= 1.0"
}

terraform {
  required_providers {
    aws = "~> 2.7"
  }
}

provider "aws" {
  region = "eu-central-1"
}

resource "aws_iam_user" "myUser" {
  name = "ENE"
}

resource "aws_iam_policy" "customPolicy" {
  name = "GlacierEFSEC2"
  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:DeleteVpcEndpointServiceConfigurations",
                "ec2:ModifyAvailabilityZoneGroup",
                "ec2:CreateCapacityReservationFleet",
                "elasticfilesystem:DescribeFileSystemPolicy",
                "ec2:CreateStoreImageTask",
                "elasticfilesystem:DescribeFileSystems",
                "ec2:ModifyTransitGatewayVpcAttachment",
                "ec2:DeletePlacementGroup",
                "ec2:TerminateInstances",
                "ec2:ResetAddressAttribute",
                "ec2:DisassociateTransitGatewayMulticastDomain",
                "ec2:DisassociateClientVpnTargetNetwork",
                "ec2:DeleteRoute",
                "ec2:ModifyCapacityReservationFleet",
                "ec2:CreateTrafficMirrorSession",
                "ec2:AllocateAddress",
                "ec2:CreateManagedPrefixList",
                "ec2:EnableFastLaunch",
                "ec2:CreateVpcEndpoint",
                "ec2:DisableEbsEncryptionByDefault",
                "ec2:CreateInstanceEventWindow",
                "glacier:ListProvisionedCapacity",
                "ec2:ResetFpgaImageAttribute"
            ],
            "Resource": "*"
        }
    ]
}
EOF
}

resource "aws_iam_policy_attachment" "policyBind" {
  name = "attachment"
  users = [aws_iam_user.myUser.name]
  policy_arn = aws_iam_policy.customPolicy.arn
}
