from setup import session, User

users_to_delete = session.query(User).filter_by(age=30).all()

if users_to_delete:
    for user in users_to_delete:
        print('El usuario ', user.name, 'va a ser eliminado')
        session.delete(user)

        
    session.commit()
    print('Usuarios con edad de 30 han sido eliminados')
