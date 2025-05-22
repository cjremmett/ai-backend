import os
import json
from dotenv import load_dotenv


def reload_dotenv() -> None:
    """
    Reload the environment variables from the .env file.
    """
    load_dotenv()


def get_cjremmett_key(key: str) -> str:
    json_string = os.environ.get('CJREMMETT_KEYS_JSON')
    if not json_string:
        reload_dotenv()
        json_string = os.environ.get('CJREMMETT_KEYS_JSON')
        if not json_string:
            raise ValueError("CJREMMETT_KEYS_JSON is not set in the .env file")
    try:
        return (json.loads(json_string))[key]
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in CJREMMETT_KEYS_JSON: {e}")