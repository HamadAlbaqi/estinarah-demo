from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    host = os.getenv("host")
    database = os.getenv("database")
    user = os.getenv("user")
    password = os.getenv("password")
    port = int(os.getenv("port"))
    api_key = os.getenv("api_key")
    model_name = 'estinarah_model'