from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb as dynamodb,
)
from constructs import Construct

from IaC.iac.subject_dynamo_stack import SubjectDynamoStack


class AppMauaBack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        dynamoStack = SubjectDynamoStack(self)



