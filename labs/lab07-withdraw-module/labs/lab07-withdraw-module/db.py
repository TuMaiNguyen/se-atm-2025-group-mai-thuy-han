# labs/lab07-withdraw-module/db.py
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()  # đọc .env nếu có (copy .env.example -> .env và sửa)

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "atm_user"),
        password=os.getenv("DB_PASSWORD", "atm_pass_123"),
        database=os.getenv("DB_NAME", "atm_demo"),
        autocommit=False,
    )
