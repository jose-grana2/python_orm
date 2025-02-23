from setup import session, User

try:
    new_user = User(name='Juan', age=580)
    session.add(new_user)
    session.commit()
except Exception as e:
    print(f"ERROR al crear el usuario: {e}")