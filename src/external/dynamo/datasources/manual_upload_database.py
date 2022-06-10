import os
import asyncio

from src.external.dynamo.datasources.dynamo_datasource import DynamoDatasource
from src.external.dynamo.datasources.mock_db import SUBJECTS # arquivo temporario com lista das subjects

access_key = os.environ["access_key"]
secret_key = os.environ["secret_key"]
endpoint_url = os.environ["endpoint_url"]
dynamo_table_name = os.environ["dynamo_table_name"]


if __name__ == '__main__':
    dynamo = DynamoDatasource(access_key, secret_key, endpoint_url, dynamo_table_name)
    data = SUBJECTS

    asyncio.run(dynamo.batchWriteItems(data))

    # asyncio.run(dynamo.putItem(data))
