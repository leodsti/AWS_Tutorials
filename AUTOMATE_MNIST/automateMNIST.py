import boto3
session = boto3.Session(profile_name='user1Admin')

ec2 = session.resource('ec2')

user_data_script = """#!/bin/bash
sudo yum update -y
sudo yum -y install httpd
sudo service httpd start"""

#THERE IS A SMALL THING YOU NEED TO CONFIGURE AT THE SUBNET LEVEL
response = ec2.create_instances(ImageId='ami-01f3682deed220c2a',MinCount=1,MaxCount=1, InstanceType="t2.micro",UserData=user_data_script,SecurityGroupIds=["sg-06a3af9085a0087ff"],SubnetId="subnet-fbba26b3")
instance_id = response[0].instance_id

print(response)
print(instance_id)

ids = [instance_id]
#ec2.instances.filter(InstanceIds=ids).terminate()