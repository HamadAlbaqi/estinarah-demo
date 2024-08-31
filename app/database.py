import mysql.connector
from mysql.connector import Error
from .config import Settings

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=Settings.host,
            database=Settings.database,
            user=Settings.user,
            password=Settings.password,
            port=int(Settings.port)
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
        return connection
    except Error as e:
        print("Error while connecting to MySQL")
        print(e)
        return None

connection = get_connection()