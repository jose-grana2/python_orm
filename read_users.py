from setup import session, User

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
total_users = session.query(User).count()
print('El número total de usuarios en la base de datos es:' , total_users)
