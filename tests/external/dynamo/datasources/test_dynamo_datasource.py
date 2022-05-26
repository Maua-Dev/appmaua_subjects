import pytest
from boto3.dynamodb.conditions import Key

from src.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class Test_DynamoDatasource:

    @pytest.mark.asyncio
    async def test_dynamo_connection(self):
        dynamoDatasource = DynamoDatasource()
        assert dynamoDatasource.dynamoTable is not None
        with dynamoDatasource.dynamoTable as table:
            assert table.table_status == 'ACTIVE'

    @pytest.mark.asyncio
    async def test_put_item(self):
        dynamoDatasource = DynamoDatasource()
        item = {
            "subjectCode": "CSCI",
            "studentRA": "123456789",
            "studentName": "John Doe"
        }
        resp = await dynamoDatasource.putItem(item)
        assert resp['ResponseMetadata']['HTTPStatusCode'] == 200

    @pytest.mark.asyncio
    async def test_get_item(self):
        dynamoDatasource = DynamoDatasource()

        resp = await dynamoDatasource.getItem(
            {
                "subjectCode": "CSCI",
                "studentRA": "123456789"
            }
        )
        assert resp['Item']['studentName'] == 'John Doe'

    @pytest.mark.asyncio
    async def test_hard_update_item(self):
        dynamoDatasource = DynamoDatasource()

        item = {
            "subjectCode": "CSCI",
            "studentRA": "123456789",
            "studentName": "John Doe",
            "data": "test"
        }
        resp = await dynamoDatasource.putItem(item)
        assert resp['ResponseMetadata']['HTTPStatusCode'] == 200

        resp2 = await dynamoDatasource.getItem(
            {
                "subjectCode": item['subjectCode'],
                "studentRA": item['studentRA']
            }
        )
        assert resp2['Item']['data'] == 'test'
        assert resp2['Item']['studentName'] == 'John Doe'


    @pytest.mark.asyncio
    async def test_delete_item(self):
        dynamoDatasource = DynamoDatasource()

        item = {
            "subjectCode": "SUBJ123",
            "studentRA": "1234542",
            "studentName": "John",
            "data": "test"
        }
        resp = await dynamoDatasource.putItem(item)
        assert resp['ResponseMetadata']['HTTPStatusCode'] == 200

        resp2 = await dynamoDatasource.getItem(
            {
                "subjectCode": item['subjectCode'],
                "studentRA": item['studentRA']
            }
        )
        assert resp2['Item']['data'] == 'test'
        assert resp2['Item']['studentName'] == 'John'

        resp3 = await dynamoDatasource.deleteItem(
            {
                "subjectCode": item['subjectCode'],
                "studentRA": item['studentRA']
            }
        )
        assert resp3['ResponseMetadata']['HTTPStatusCode'] == 200

        resp4 = await dynamoDatasource.getItem(
            {
                "subjectCode": item['subjectCode'],
                "studentRA": item['studentRA']
            }
        )
        assert resp4.get('Item') is None

    @pytest.mark.asyncio
    async def test_query_items(self):
        dynamoDatasource = DynamoDatasource()
        items = [
            {
                "subjectCode": "ECM257",
                "studentRA": "123456789",
                "studentName": "John Doe"
            },
            {
                "subjectCode": "ECM255",
                "studentRA": "123456789",
                "studentName": "John Doe",
                "data": "test"
            },
            {
                "subjectCode": "ECM257",
                "studentRA": "123456755",
                "studentName": "Mark Doe"
            },

        ]

        for i in items:
            await dynamoDatasource.putItem(i)

        resp = await dynamoDatasource.query(
            keyConditionExpression=Key('subjectCode').eq('ECM257')
        )

        assert len(resp['Items']) == 2
        assert items[0] in resp['Items']
        assert items[2] in resp['Items']
        assert items[1] not in resp['Items']

        resp2 = await dynamoDatasource.query(
            keyConditionExpression=Key('subjectCode').eq('ECM257') & Key('studentRA').eq('123456789')
        )

        assert len(resp2['Items']) == 1
        assert items[0] in resp2['Items']


    @pytest.mark.asyncio
    async def test_scan_items(self):
        dynamoDatasource = DynamoDatasource()
        items = [
            {
                "subjectCode": "ECM257",
                "studentRA": "123456789",
                "studentName": "John Doe"
            },
            {
                "subjectCode": "ECM255",
                "studentRA": "123456789",
                "studentName": "John Doe",
                "data": "test"
            },
            {
                "subjectCode": "ECM257",
                "studentRA": "123456755",
                "studentName": "Mark Doe"
            }
        ]

        for i in items:
            await dynamoDatasource.putItem(i)

        resp = await dynamoDatasource.getAllItems()
        assert len(resp['Items']) >= 3
        assert items[0] in resp['Items']
        assert items[1] in resp['Items']
        assert items[2] in resp['Items']



    @pytest.mark.asyncio
    async def test_batch_write(self):
        dynamoDatasource = DynamoDatasource()
        items = [
            {
                "subjectCode": "ECM222",
                "studentRA": "1234567892",
                "studentName": "John Doe"
            },
            {
                "subjectCode": "ECM222",
                "studentRA": "1234567822",
                "studentName": "Johny Doe",
                "data": "test"
            },
            {
                "subjectCode": "ECM222",
                "studentRA": "1234567525",
                "studentName": "Mark Doe"
            }
        ]


        await dynamoDatasource.batchWriteItems(items)


        res = await dynamoDatasource.query(keyConditionExpression=Key('subjectCode').eq('ECM222') )
        assert items[0] in res['Items']
        assert items[1] in res['Items']
        assert items[2] in res['Items']

    @pytest.mark.asyncio
    async def test_batch_delete(self):
        dynamoDatasource = DynamoDatasource()

        items = [
            {
                "subjectCode": "ECM222",
                "studentRA": "1234567892",
                "studentName": "John Doe"
            },
            {
                "subjectCode": "ECM222",
                "studentRA": "1234567822",
                "studentName": "Johny Doe",
                "data": "test"
            },
            {
                "subjectCode": "ECM222",
                "studentRA": "1234567525",
                "studentName": "Mark Doe"
            }
        ]
        keys = [
            {
                "subjectCode": "ECM222",
                "studentRA": "1234567892",
            },
            {
                "subjectCode": "ECM222",
                "studentRA": "1234567822",
            },
            {
                "subjectCode": "ECM222",
                "studentRA": "1234567525",
            }
        ]

        await dynamoDatasource.batchWriteItems(items)
        curr = await dynamoDatasource.query(Key('subjectCode').eq('ECM222'))

        await dynamoDatasource.batchDeleteItems(keys)
        act = await dynamoDatasource.query(Key('subjectCode').eq('ECM222'))

        assert curr["Count"] == act["Count"] + 3

