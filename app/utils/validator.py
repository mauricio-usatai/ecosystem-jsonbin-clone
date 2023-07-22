import json


def is_json_valid(json_str: str) -> bool:
    try:
        json.loads(json_str)
    except json.JSONDecodeError:
        return False
    return True
