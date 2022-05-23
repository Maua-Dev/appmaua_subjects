#!/usr/bin/env python3
import os

import aws_cdk as cdk

from iac.iac_stack import IaCStack

env_TEMP = cdk.Environment(account="171487071332", region="us-east-1")



app = cdk.App()
IaCStack(app, "IaCStack", env=env_TEMP)

app.synth()
