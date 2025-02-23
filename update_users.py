from setup import session, User

#Actualización de un registro
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