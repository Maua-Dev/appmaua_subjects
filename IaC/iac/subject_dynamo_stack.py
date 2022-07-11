from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb as dynamodb,
    NestedStack
)

from constructs import Construct


class SubjectDynamoStack(NestedStack):
    def __init__(self, scope: Construct) -> None:
        super().__init__(scope, "SubjectDynamoStack")

        # Subjects database
        self.dynamo = dynamodb.Table(
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

        self.dynamo.add_global_secondary_index(
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

        self.dynamo.add_local_secondary_index(
            index_name="academicYear",
            sort_key=dynamodb.Attribute(
                name="studentRA",
                type=dynamodb.AttributeType.STRING
            )
        )
        self.dynamo.add_local_secondary_index(
            index_name="degreeCode",
            sort_key=dynamodb.Attribute(
                name="studentRA",
                type=dynamodb.AttributeType.STRING
            )
        )





