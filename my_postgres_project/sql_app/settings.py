import os

DB_USER_NAME = os.getenv('TEST_DB_USER_NAME', '')
DB_PASSWORD = os.getenv('TEST_DB_PASSWORD', '')
DB_HOST = os.getenv('TEST_DB_HOST', '')
DB_PORT = os.getenv('TEST_DB_PORT', '')