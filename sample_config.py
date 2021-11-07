# By @TroJanzHEX


import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 12345))

    API_HASH = os.environ.get("API_HASH", "")

    # Get this api from https://www.remove.bg/b/background-removal-api
    RemoveBG_API = os.environ.get("RemoveBG_API", "")
    
        # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600

    # Sql Database url
    DB_URI = os.environ.get("DATABASE_URL", "")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "teleroidzee5bot")

    BOT_OWNER = os.environ.get("BOT_OWNER", 1287407305) 

    # watermark file
    DEF_WATER_MARK_FILE = ""

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))

    MONGODB_URI = os.environ.get("MONGODB_URI", "")

    DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", "./downloads")

    # Generate screenshots for file after uploading
    # Defaults to True
    SCREENSHOTS = os.environ.get("SCREENSHOTS", "True")

    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    
    OWNER_ID = os.environ.get("OWNER_ID", 1287407305) 
