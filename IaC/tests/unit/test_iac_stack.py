import aws_cdk as core
import aws_cdk.assertions as assertions
from IaC.iac.iac_stack import AppMauaBack


# example tests. To run these tests, uncomment this file along with the example
# resource in iac/iac_stack.py



# def test_dynamo_table_created():
#     app = core.App()
#     stack = AppMauaBack(app, "iac")
#     template = assertions.Template.from_stack(stack)
#
#     template.has_resource_properties("AWS::DYNAMODB::Table", {
#         "BillingMode": "PAY_PER_REQUEST",
#         "PartitionKey": {
#             "AttributeName": "subjectCode",
#             "AttributeType": "S"
#         },
#         "SortKey": {
#             "AttributeName": "studentRA",
#             "AttributeType": "S"
#         }
#     })
#
#
# #     template.has_resource_properties("AWS::SQS::Queue", {
# #         "VisibilityTimeout": 300
# #     })
