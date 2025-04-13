import json
import os
from typing import Union

config_path = "config.json"

# Load config file
if os.path.exists(config_path):
    with open(config_path, "r") as f:
        config_data = json.load(f)
else:
    config_data = {}


def get_config_value(key, default):
    """Returns the value from config.json with the expected type."""
    value = config_data.get(key, default[1])
    expected_type = default[0]

    # Ensure the type matches the expected type
    if not isinstance(value, expected_type):
        print(
            f"Warning: Type mismatch for {key}. Expected {expected_type}, got {type(value)}. Using default."
        )
        return default[1]
    return value


class Config:
    DATABASE_URL = [str, get_config_value("DATABASE_URL", [str, "mongodb+srv://newuser:<newuser>@cluster0.0fs6z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"])]
    API_HASH = [str, get_config_value("API_HASH", [str, "b0402db44bb51470d0c50d3be950781b"])]
    API_ID = [int, get_config_value("API_ID", [int, 29696002])]
    BOT_TOKEN = [str, get_config_value("BOT_TOKEN", [str, "7529913637:AAFr-E6m5HRQLwhCRGUZBhT9pUfzcwRnG4Q"])]
    COMPLETED_STR = [str, get_config_value("COMPLETED_STR", [str, "▰"])]
    REMAINING_STR = [str, get_config_value("REMAINING_STR", [str, "▱"])]
    MAX_QUEUE_SIZE = [int, get_config_value("MAX_QUEUE_SIZE", [int, 5])]
    SLEEP_SECS = [int, get_config_value("SLEEP_SECS", [int, 10])]
    IS_MONGO = [bool, get_config_value("IS_MONGO", [bool, False])]
    DEFAULT_LOCALE = [str, get_config_value("DEFAULT_LOCALE", [str, "en"])]

    # Access Restriction
    IS_PRIVATE = [bool, get_config_value("IS_PRIVATE", [bool, False])]
    AUTH_USERS = [list, get_config_value("AUTH_USERS", [list, [123456789]])]
    OWNER_ID = [int, get_config_value("OWNER_ID", [int, 2040287721])]

    # Public username url or invite link of private chat
    FORCEJOIN = [str, get_config_value("FORCEJOIN", [str, "https://t.me/+QigegfxQjZEwYTI1"])]
    FORCEJOIN_ID = [int, get_config_value("FORCEJOIN_ID", [int, -1002596945084])]

    TRACE_CHANNEL = [int, get_config_value("TRACE_CHANNEL", [int, 0])]
    SAVE_FILE_TO_TRACE_CHANNEL = [
        bool,
        get_config_value("SAVE_FILE_TO_TRACE_CHANNEL", [bool, False]),
    ]


class Commands:
    command_defaults = {
        "START": "/start",
        "RENAME": "/rename",
        "FILTERS": "/filters",
        "SET_THUMB": "/setthumb",
        "GET_THUMB": "/getthumb",
        "CLR_THUMB": "/clrthumb",
        "SET_CAPTION": "/setcaption",
        "QUEUE": "/queue",
        "MODE": "/mode",
        "HELP": "/help",
        "SET_CAPTION": "/setcaption",
        "SET_LANG": "/setlanguage",
    }

    COMMANDS: dict = config_data.get("COMMANDS", command_defaults)

    START = COMMANDS.get("START", "/start")
    RENAME = COMMANDS.get("RENAME", "/rename")
    FILTERS = COMMANDS.get("FILTERS", "/filters")
    SET_THUMB = COMMANDS.get("SET_THUMB", "/setthumb")
    GET_THUMB = COMMANDS.get("GET_THUMB", "/getthumb")
    CLR_THUMB = COMMANDS.get("CLR_THUMB", "/clrthumb")
    QUEUE = COMMANDS.get("QUEUE", "/queue")
    MODE = COMMANDS.get("MODE", "/mode")
    HELP = COMMANDS.get("HELP", "/help")
    SET_CAPTION = COMMANDS.get("SET_CAPTION", "/setcaption")
    SET_LANG = COMMANDS.get("SET_LANG", "/setlanguage")
