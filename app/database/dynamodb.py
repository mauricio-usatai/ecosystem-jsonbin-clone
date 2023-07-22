import boto3

from settings import Settings
from src.logger import get_logger


settings = Settings()
logger = get_logger()


class DynamoDB:
    def __init__(self):
        if settings.DEPLOYMENT == "local":
            self.client = boto3.client(
                "dynamodb",
                endpoint_url="http://dynamodb:8000",
                region_name="us-east-1",
                aws_access_key_id="dummy-key-id",
                aws_secret_access_key="dummy-key",
            )
        else:
            self.client = boto3.client(
                "dynamodb",
                region_name="sa-east-1",
            )

    def put_item(self, table_name: str, item_id: str, item_content: dict) -> None:
        try:
            self.client.put_item(
                TableName=table_name,
                Item={
                    "id": {"S": item_id},
                    "content": {"S": item_content},
                },
            )
        except Exception as err:
            raise err

    def get_item_by_id(self, table_name: str, item_id: str) -> dict:
        try:
            item = self.client.get_item(
                TableName=table_name, Key={"id": {"S": item_id}}
            )
        except Exception as err:
            raise err

        logger.info(item)

        if not item:
            return None

        return item
