#!/usr/bin/env python3
import os
import aws_cdk as cdk

from awscdk.ec2_deployer.ec2_deployer_stack import Ec2DeployerStack

app = cdk.App()

Ec2DeployerStack(
    app,
    "Ec2DeployerStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
        region=os.getenv("CDK_DEFAULT_REGION"),
    ),
)

app.synth()
