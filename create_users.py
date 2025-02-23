from setup import session, User
# #Crear un registro CREATE
new_user = User(name="Jose", age=25)

# #Agregamos el registro
session.add(new_user)
session.commit()

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
session.add_all(users_to_create)
session.commit()

#Verificamos los registros
created_users = session.query(User).all()
for user in created_users:
    print('Nombre', user.name, 'Edad', user.age)


