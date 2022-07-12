from aws_cdk import (
    aws_lambda as lambda_,
    NestedStack,
    aws_iam as iam,
    Duration

)

from constructs import Construct


class LambdaStack(NestedStack):

    def __init__(self, scope: Construct, DYNAMO_TABLE_NAME: str) -> None:
        super().__init__(scope, "Lambda_Stack")

        self.full_access_to_dynamo_table_statement = iam.PolicyStatement(
                    actions=[
                        "dynamodb:GetItem",
                        "dynamodb:PutItem",
                        "dynamodb:UpdateItem",
                        "dynamodb:DeleteItem",
                        "dynamodb:Scan",
                        "dynamodb:Query"
                    ],
                    resources=[
                        f"arn:aws:dynamodb:{self.region}:{self.account}:table/{DYNAMO_TABLE_NAME}/*",
                        f"arn:aws:dynamodb:{self.region}:{self.account}:table/{DYNAMO_TABLE_NAME}",
                    ],
                    effect=iam.Effect.ALLOW
                )

        self.lambda_layer = lambda_.LayerVersion(self, "Lambda_Layer",
                                                 code=lambda_.Code.from_asset("./lambda_layer.zip"),
                                                 compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
                                                 )

        self.lambda_layer_requirements = lambda_.LayerVersion(self, "Lambda_Layer_Requirements",
                                                              code=lambda_.Code.from_asset(
                                                                  "./lambda_layer_requirements.zip"),
                                                              compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
                                                              )

        # MSS - Get all subjects
        self.get_all_subject = lambda_.Function(
            self, "GET_ALL_SUBJECTS",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="get_all_subjects_presenter.lambda_handler",
            code=lambda_.Code.from_asset("../src/modules/get_all_subjects"),
            environment={
                "PYTHON_ENV": "Development",
                "DYNAMO_TABLE_NAME": DYNAMO_TABLE_NAME
            },
            layers=[self.lambda_layer, self.lambda_layer_requirements],
            timeout=Duration.seconds(30)

        )
        self.get_all_subject.add_function_url(auth_type=lambda_.FunctionUrlAuthType.NONE)
        self.get_all_subject.add_to_role_policy(self.full_access_to_dynamo_table_statement)

        # MSS - Get subject
        self.get_subject = lambda_.Function(
            self, "GET_SUBJECT",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="get_subject_presenter.lambda_handler",
            code=lambda_.Code.from_asset("../src/modules/get_subject"),
            environment={
                "PYTHON_ENV": "Development",
                "DYNAMO_TABLE_NAME": DYNAMO_TABLE_NAME
            },
            layers=[self.lambda_layer, self.lambda_layer_requirements],
            timeout=Duration.seconds(30)
        )
        self.get_subject.add_function_url(auth_type=lambda_.FunctionUrlAuthType.NONE)
        self.get_subject.add_to_role_policy(self.full_access_to_dynamo_table_statement)

        # MSS - Get subjects by student
        self.get_subjects_by_student = lambda_.Function(
            self, "GET_SUBJECT_BY_STUDENT",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="get_subjects_by_student_presenter.lambda_handler",
            code=lambda_.Code.from_asset("../src/modules/get_subjects_by_student"),
            environment={
                "PYTHON_ENV": "Development",
                "DYNAMO_TABLE_NAME": DYNAMO_TABLE_NAME
            },
            layers=[self.lambda_layer, self.lambda_layer_requirements],
            timeout=Duration.seconds(30)
        )
        self.get_subjects_by_student.add_function_url(auth_type=lambda_.FunctionUrlAuthType.NONE)
        self.get_subjects_by_student.add_to_role_policy(self.full_access_to_dynamo_table_statement)
