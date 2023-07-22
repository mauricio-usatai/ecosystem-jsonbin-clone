import json

from services import BinService

from settings import Settings
from utils import is_json_valid
from src.logger import get_logger
from src.exceptions import ServiceNotAvailableException


settings = Settings()
logger = get_logger()


def build_response(body, status_code):
    return {
        "isBase64Encoded": False,
        "statusCode": status_code,
        "body": (json.dumps(body) if isinstance(body, dict) else body),
    }


def lambda_handler(event, _context) -> dict:
    logger.info(event)
    logger.info(_context)
    method = (
        event["method"]
        if settings.DEPLOYMENT == "local"
        else event["httpMethod"]
    )

    # Parse body if present
    if "body" in event and event["body"] is not None:
        body = json.loads(event["body"])
    else:
        body = event

    if method == "POST":
        content = body["content"]
        # Try load json to check if it is valid
        if not is_json_valid(content):
            return build_response(
                {"message": "invalid json"},
                400,
            )

        try:
            item_id = BinService().save(content=content)
        except ServiceNotAvailableException as err:
            return build_response(
                {"message": str(err)},
                503,
            )

        return build_response(
            {"id": item_id},
            201,
        )

    if method == "GET":
        _id = event["pathParameters"]["id"]

        try:
            item = BinService.get(_id=_id)
        except ServiceNotAvailableException as err:
            return build_response(
                {"message": str(err)},
                503,
            )

        if item:
            return build_response(
                {
                    "id": _id,
                    "item": item,
                },
                200,
            )

        return build_response(
            {"message": "item not found"},
            404,
        )
