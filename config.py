import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return 6845693079

API_ID = int(environ.get("API_ID", "27215224"))
API_HASH = environ.get("API_HASH", "688ae67db37f0ae991c3ecb97d73ff0a")
BOT_TOKEN = environ.get("BOT_TOKEN", "6845693079:AAG290dcjTkuIoFDg8B4R4e7PeIAVmZ6pT0")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002142022630"))
ADMINS = int(environ.get("ADMINS", "6200605339"))
DB_URI = environ.get("DB_URI", "mongodb+srv://jeronmathew691:jeronmathew691@cluster0.2au4ued.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
