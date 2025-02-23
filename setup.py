#CRUD -> CREATE, READ, UPDATE, DELETE
from sqlalchemy import create_engine, Column, Integer, String
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
Session = sessionmaker(bind=engine)

#Abrir la sesión 
session = Session()

#Definición de un modelo
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

#Crear tabla
try:
    Base.metadata.create_all(engine)
    print("Base de datos y tabla creada exitosamente")
except Exception as e:
    print("No se puede crear la base de datos")
    print('ERROR', e)


#Manejo de excepciones ********************************************************************

try:
    new_user = User(name='Juan', age=580)
    session.add(new_user)
    session.commit()
except Exception as e:
    print(f"ERROR al crear el usuario: {e}")