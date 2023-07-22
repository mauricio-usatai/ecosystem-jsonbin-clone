from typing import Optional

import uuid

from database import DynamoDB

from settings import Settings
from src.logger import get_logger
from src.exceptions import ServiceNotAvailableException


settings = Settings()
logger = get_logger()


class BinService:
    @staticmethod
    def save(content: dict) -> str:
        dynamodb = DynamoDB()

        item_id = str(uuid.uuid4())
        try:
            dynamodb.put_item(
                table_name=settings.DYNAMO_TABLE_NAME,
                item_id=item_id,
                item_content=content,
            )
        except Exception as err:
            logger.error("Could not access dynamo: %s", err)
            raise ServiceNotAvailableException from err

        return item_id

    @staticmethod
    def get(_id: str) -> Optional[dict]:
        dynamodb = DynamoDB()

        try:
            response = dynamodb.get_item_by_id(
                table_name=settings.DYNAMO_TABLE_NAME,
                item_id=_id,
            )
        except Exception as err:
            logger.error("Could not access dynamo: %s", err)
            raise ServiceNotAvailableException from err

        if "Item" not in response:
            return None

        item = response["Item"]
        content = item["content"]["S"]

        return content
