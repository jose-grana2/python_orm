from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()
#URL DE LA BASE DE DATOS 
DB_PASSWORD = os.getenv("SQL_PASSWORD")
DATABASE_URL = f"mysql+pymysql://root:{DB_PASSWORD}@localhost:3306/clase1"


#Crear el motor de la base de datos 
engine = create_engine(DATABASE_URL, echo=True)

#Clase base para definir los modelos
Base= declarative_base()

#Configuracion de la sesion
SessionLocal = sessionmaker(autoflush=False, bind=engine)