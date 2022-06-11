from aws_cdk import (
    aws_lambda as lambda_,
    NestedStack,

)

from constructs import Construct




class LambdaStack(NestedStack):

    def __init__(self, scope: Construct, DYNAMO_TABLE_NAME: str) -> None:
        super().__init__(scope, "MauApp_MSS_Lambda_Stack")

        self.lambda_layer = lambda_.LayerVersion(self, "MauApp_MSS_Lambda_Layer",
            code=lambda_.Code.from_asset("../"),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
        )




        self.get_subject_by_student = lambda_.Function(
            self, "MauApp_MSS_SUBJECTS_GET_SUBJECT_BY_STUDENT",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="get_subjects_by_student_presenter.lambda_handler",
            code=lambda_.Code.from_asset("../src/modules/get_subjects_by_student"),
            environment={
                "PYTHON_ENV": "Development",
                "DYNAMO_SUBJECTS_TABLE_NAME": DYNAMO_TABLE_NAME
            },
            layers=[self.lambda_layer]
        )

        self.get_subject_by_student.add_function_url(auth_type=lambda_.FunctionUrlAuthType.NONE)


