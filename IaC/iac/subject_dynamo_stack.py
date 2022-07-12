from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb as dynamodb,
    NestedStack
)

from constructs import Construct


class SubjectDynamoStack(NestedStack):
    def __init__(self, scope: Construct) -> None:
        super().__init__(scope, "DynamoStack")

        # Subjects database
        self.dynamo = dynamodb.Table(
            self, "SubjectsDB",
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
            index_name="studentRA-index",
            partition_key=dynamodb.Attribute(
                name="studentRA",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="subjectCode",
                type=dynamodb.AttributeType.STRING
            )
        )






