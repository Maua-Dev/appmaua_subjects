#!/usr/bin/env python3
import os
import aws_cdk as cdk
from iac.iac_stack import AppMauaBack
from dotenv import load_dotenv
from load_layer_output import load_lambda_layer_output

load_dotenv()

env = cdk.Environment(account=os.environ['CDK_DEFAULT_ACCOUNT'], region=os.environ['CDK_DEFAULT_REGION'])

load_lambda_layer_output()

app = cdk.App()

AppMauaBack(app, "IaCStack", env=env)

app.synth()
