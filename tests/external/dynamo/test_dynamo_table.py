import pytest

from src.external.dynamo.dynamo_table import DynamoTable


class Test_DynamoTable:

    @pytest.mark.asyncio
    async def test_find_tables(self):
        table = DynamoTable()
        with table as t:
            assert t.table_status == 'ACTIVE'

