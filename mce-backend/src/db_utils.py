import psycopg2
from src.config import DATABASE_CONFIG
import datetime
import logging

def open_db_connexion():
    try:
        conn = psycopg2.connect(
            database = DATABASE_CONFIG["dbname"], 
            user = DATABASE_CONFIG["user"], 
            host= DATABASE_CONFIG["host"],
            password = DATABASE_CONFIG["password"],
            port = DATABASE_CONFIG["port"]
        )
        logging.info(f"succesfully established connexion with database {DATABASE_CONFIG['dbname']}")
        return conn
    except psycopg2.OperationalError as e:
        logging.error(
            f"Impossible to establish connection with database {DATABASE_CONFIG['dbname']} ({str(e)})"
        )
        return None

def verify_db_connection(conn: psycopg2.extensions.connection):
    if conn is None:
        raise ConnectionError("Database connection hasn't been created")
        return None
    return conn

def insert_api_call(conn: psycopg2.extensions.connection, timestamp: datetime.datetime, client_ip: str):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO api_calls (timestamp, ip_address) VALUES (%s, %s)",
        (timestamp, client_ip)
    )
    conn.commit()
    cur.close()