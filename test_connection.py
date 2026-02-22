from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("DATABASE_URL")
engine = create_engine(url)
with engine.connect() as connection:
    connection.execute(text("SELECT 1"))
    print('Conexion exitosa')
