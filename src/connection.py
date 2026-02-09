import os
import pyodbc
from dotenv import load_dotenv


def connect_database():

    load_dotenv()

    conn_str = (
        f"DRIVER={os.getenv('DRIVER')};"
        f"UID={os.getenv('UID')};"
        f"PWD={os.getenv('PWD')};"
        f"ENG={os.getenv('ENG')};"
        f"DBN={os.getenv('DBN')};"
        f"LINKS={os.getenv('LINKS')};"       
    )

    try:
        conn = pyodbc.connect(conn_str)
        print("\rConnecting to database... Done!", flush=True)
        return conn
    except Exception as error:
        print(f"\rConnecting to database... Failed!", flush=True)
        print(f"Error connecting to the database: {str(error)}")
        return None