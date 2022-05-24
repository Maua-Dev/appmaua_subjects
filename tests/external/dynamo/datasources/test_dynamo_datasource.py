import pytest

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

        resp = await dynamoDatasource.getItem("CSCI","123456789")
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

        resp2 = await dynamoDatasource.getItem(subjectCode=item["subjectCode"], studentCode=item["studentRA"])
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

        resp2 = await dynamoDatasource.getItem(subjectCode=item["subjectCode"], studentCode=item["studentRA"])
        assert resp2['Item']['data'] == 'test'
        assert resp2['Item']['studentName'] == 'John'

        resp3 = await dynamoDatasource.deleteItem(subjectCode=item["subjectCode"], studentCode=item["studentRA"])
        assert resp3['ResponseMetadata']['HTTPStatusCode'] == 200

        resp4 = await dynamoDatasource.getItem(subjectCode=item["subjectCode"], studentCode=item["studentRA"])
        assert resp4.get('Item') is None
