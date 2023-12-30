import os

import dotenv

dotenv.load_dotenv()

USERNAME_REGEX = r"^[\w.@+-]+$"
USERNAME_MIN_LENGTH = 5
USERNAME_MAX_LENGTH = 32
NAME_REGEX = r"^[а-яА-ЯёЁ]+$"
NAME_MIN_LENGTH = 1
NAME_MAX_LENGTH = 64
SURNAME_MAX_LENGTH = 64
SURNAME_MIN_LENGHT = 1
PHONE_NUMBER_REGEX = r"^[0-9]"
PHONE_NUMBER_LENGTH = 11
FAQ_MAX_LENGTH = 1024
CHAT_ID_MIN_LENGTH = 6
CHAT_ID_MAX_LENGTH = 15
PROD_URL = os.getenv("PROD_URL")
DATETIME_FORMAT = "%Y%m%d"
CHAT_ID_REGEX = r"\d"
TELEGRAM_USERNAME_REGEX = r"([a-z]|\d|[_])"
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
