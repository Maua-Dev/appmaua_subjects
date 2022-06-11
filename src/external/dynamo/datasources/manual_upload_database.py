import os
import asyncio
import pprint

from src.external.dynamo.datasources.dynamo_datasource import DynamoDatasource
from src.external.dynamo.datasources.mock_db import SUBJECTS # arquivo temporario com lista das subjects

# access_key = os.environ["access_key"]
# secret_key = os.environ["secret_key"]
# endpoint_url = os.environ["endpoint_url"]
# dynamo_table_name = os.environ["dynamo_table_name"]


access_key = None
secret_key = None
endpoint_url = None
dynamo_table_name = "IaCStack-MauAppSubjectsDB1BBD4F9F-1KES1YD4D4CXE"


def getDuplicates(data, partition_key, sort_key):
    keys = []
    duplicates = []
    duplicates_keys = []
    for item in data:
        if (item[partition_key], item[sort_key]) in keys:
            duplicates.append(item)
            duplicates_keys.append((item[partition_key], item[sort_key]))
        else:
            keys.append((item[partition_key], item[sort_key]))

    return duplicates, duplicates_keys


if __name__ == '__main__':
    dynamo = DynamoDatasource(access_key, secret_key, endpoint_url, dynamo_table_name)
    data = SUBJECTS

    asyncio.run(dynamo.batchWriteItems(data))
    # duplicates, keys = getDuplicates(data, "subjectCode", "studentRA")
    # pprint.pprint(duplicates)
    # print("\n\n", keys)

    # print(len(keys))

    # asyncio.run(dynamo.putItem(data))
