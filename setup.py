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

# #Crear un registro CREATE
# new_user = User(name="Jose", age=25)

# #Agregamos el registro
# session.add(new_user)
# session.commit()

#Verificar que el usuario (registro) ha sido registrado
#Consulta de petición READ SELECT users.id AS users_id, users.name AS users_name, users.age AS users_ag
created_user=session.query(User).filter_by(name="Jose").first()
print('The name that we create is', created_user.name.upper(), 'and his age is', created_user.age)

#Agregamos múltiples usuarios
users_to_create = [
    User(name="Matilde", age=21),
    User(name="Pepe", age=55),
    User(name="Mari Camen", age=54),
    User(name="Checho", age=26),
]
# session.add_all(users_to_create)
# session.commit()

#Verificamos los registros
created_users = session.query(User).all()
for user in created_users:
    print('Nombre', user.name, 'Edad', user.age)


#Manejo de excepciones ********************************************************************

# try:
#     new_user = User(name='Juan', age=580)
#     session.add(new_user)
#     session.commit()
# except Exception as e:
#     print(f"ERROR al crear el usuario: {e}")


#LEER REGISTROS ***************************************************************************
#operacion de filtrado
users = session.query(User).filter(User.age > 25).all()
print('Usuarios mayores a 25')
for user in users:
    print(f"{user.name}, {user.age}")

#Operacion de filtrado por varios criterios
users2 = session.query(User).filter(User.age >= 20, User.age <= 30).all()
print('Usuarios mayores de 20 y menores de 30')
for user in users2:
    print(f"{user.name}, {user.age}")

#Contamos los registros
total_users = session.query(User).filter(User.age >= 20, User.age <= 30).count()
print('El número total de usuarios en la base de datos es:' , total_users)


#ACTUALIZAR REGISTROS *********************************************************************
user_to_update = session.query(User).filter_by(name='Matilde').first()
if user_to_update:
    user_to_update.age = 26
    session.commit()
    print('Usuario actualizado', user_to_update.name, 'Edad', user_to_update.age)

#Actualización múltiple
users_to_update = session.query(User).filter(User.age >= 23, User.age <= 29).all()
if users_to_update:
    users_to_update
    for user in users_to_update:
        user.age = 30
    
    session.commit()
    print('Usuarios con edad entre 23 y 29 actualizados')


updated_users = session.query(User).all()
if updated_users:
    for user in updated_users:
        print(user.name, user.age)

#ELIMINACION REGISTROS *********************************************************************

users_to_delete = session.query(User).filter_by(age=30).all()
if users_to_delete:
    for user in users_to_delete:
        print('El usuario ', user.name, 'va a ser eliminado')
        session.delete(user)

        
    session.commit()
    print('Usuarios con edad de 30 han sido eliminados')





