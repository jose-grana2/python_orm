from database import engine, Base
from models import User
from sqlalchemy.orm import sessionmaker

#Crear las tablas en la base de datos -> Introducir usuarios

if __name__ == "__main__":
    print("Insertando usuario en la abase de datos ...")
    Base.metadata.create_all(bind=engine)
    print("Base de datos lista")
    try: 
        print("Insertando datos ...")

        #Configuracion de la sesion
        SessionLocal = sessionmaker(autoflush=False, bind=engine)
        db = SessionLocal()

        new_user = User(name='Juan', age=40)
        db.add(new_user)
        db.commit()
        print('Usuario insertado con éxito')
    except Exception as e:
        db.rollback
        print('El usuario no pudo ser insertado')