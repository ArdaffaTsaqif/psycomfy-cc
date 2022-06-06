from dotenv import load_dotenv

import os

load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")
SECRET_KEY = os.getenv('SECRET_KEY')
MYSQL_UNIX_SOCKET = os.getenv('MYSQL_UNIX_SOCKET')
BASE_URL = os.getenv('BASE_URL')

