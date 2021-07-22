# Link
[Basic operation explained here](../first-deployment-on-aws/README.md)

## Error
This did not work the way it should and resulted in 
```terraform plan
╷
│ Error: Error describing SSM parameter (/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2): AccessDeniedException: User: arn:aws:iam::765940042124:user/xxx is not authorized to perform: ssm:GetParameter on resource: arn:aws:ssm:eu-central-1::parameter/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
│ 	status code: 400, request id: d8b6aeed-819c-49d0-b5c4-3523ffc724cc
```
