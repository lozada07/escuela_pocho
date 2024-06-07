from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError
from .base import Base
from dotenv import load_dotenv
import os

# Carga las variables de entorno del archivo .env en el directorio raíz
load_dotenv()

# Ahora puedes obtener tu variable de entorno
DB_NOMBRE = os.getenv('DB_NOMBRE')



class ConectarDb:

    def __init__(self):
        self.engine = create_engine(DB_NOMBRE)

    def conectar_db(self):
        try:
            Base.metadata.create_all(self.engine)
            print("Conexión a la base de datos exitosa!")
        except OperationalError:
            print("No se pudo conectar a la base de datos.")
