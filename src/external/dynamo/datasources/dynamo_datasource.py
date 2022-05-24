from src.external.dynamo.dynamo_table import DynamoTable


class DynamoDatasource:
    def __init__(self):
        self.dynamoTable = DynamoTable()

    async def putItem(self, item):
        with self.dynamoTable as table:
            return table.put_item(Item=item)

    async def getItem(self, subjectCode: str, studentCode: str):
        with self.dynamoTable as table:
            resp = table.get_item(
                Key={
                    "subjectCode": subjectCode,
                    "studentRA": studentCode
                }
            )
            return resp

    async def hardUpdateItem(self, item):
        with self.dynamoTable as table:
            resp = table.put_item(Item=item)
            return resp

    async def updateItem(self, subjectCode: str, studentCode: str, updateAttributes):
        with self.dynamoTable as table:
            resp = table.update_item(
                Key={
                    "subjectCode": subjectCode,
                    "studentRA": studentCode
                },
                AttributeUpdates=updateAttributes
            )
            return resp

    async def deleteItem(self, subjectCode: str, studentCode: str):
        with self.dynamoTable as table:
            resp = table.delete_item(
                Key={
                    "subjectCode": subjectCode,
                    "studentRA": studentCode
                }
            )
            return resp
