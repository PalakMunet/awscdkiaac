# ec2_deployer/ec2_deployer_stack.py
from aws_cdk import Stack, aws_ec2 as ec2
from constructs import Construct

class Ec2DeployerStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "Vpc")

        ec2.Instance(
            self,
            "MyEC2",
            instance_type=ec2.InstanceType("t3.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux2023(),
            vpc=vpc,
        )
