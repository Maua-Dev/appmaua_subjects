from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb as dynamodb,
)
from constructs import Construct

class AppMauaBack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        dynamo = dynamodb.Table(
            self, "MauApp-SubjectsDB",
            partition_key=dynamodb.Attribute(
                name="subjectCode",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="studentRA",
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )

        dynamo.add_global_secondary_index(
            index_name="studentRA",
            partition_key=dynamodb.Attribute(
                name="studentRA",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="subjectCode",
                type=dynamodb.AttributeType.STRING
            )
        )



        dynamo.add_local_secondary_index(
            index_name="academicYear",
            sort_key=dynamodb.Attribute(
                name="studentRA",
                type=dynamodb.AttributeType.STRING
            )
        )
        dynamo.add_local_secondary_index(
            index_name="degreeCode",
            sort_key=dynamodb.Attribute(
                name="studentRA",
                type=dynamodb.AttributeType.STRING
            )
        )

