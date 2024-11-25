from firebase_admin import db
from app.models.user_model import User
import uuid

def add_user(user_id, user_data):
    ref = db.reference('users')
    ref.child(user_id).set(user_data)
    print(f'Пользователь {user_id} добавлен в базу данных.')

def check_user_id_exists(user_id):
    ref = db.reference(f'users/{user_id}')
    return ref.get() is not None # проверка на существование пользователя со сгенерир. ток что айди

def register_step1(email, password):
    while True:
        user_id = str(uuid.uuid4())
        if not check_user_id_exists(user_id):
            break

    user_data = User(user_id, email, password).to_dict()
    add_user(user_id, user_data)
    print(f'Пользователь {user_id} успешно зарегистрирован на первом этапе.')
    return user_id

def register_step2(user_id, nickname, description="", avatar=""):
    user_ref = db.reference(f'users/{user_id}')
    user_data = user_ref.get()

    if not user_data:
        print(f"Ошибка: Пользователь с ID {user_id} не найден.")
        return None

    user_data['nickname'] = nickname
    user_data['description'] = description
    user_data['avatar'] = avatar

    user_ref.update(user_data)
    print(f'Профиль пользователя {user_id} успешно обновлен на втором этапе.')
    return user_data

def login_user(email, password):
    users_ref = db.reference('users')
    users = users_ref.get()

    if users:
        for user_id, user_data in users.items():
            if user_data.get('email') == email and user_data.get('password') == password:
                print(f'Пользователь {user_id} успешно вошел в систему.')
                return user_id

    print("Ошибка: Неверный email или пароль.")
    return None

def update_profile(user_id, nickname, description="", avatar=""):
    user_ref = db.reference(f'users/{user_id}')
    user_data = user_ref.get()

    if not user_data:
        print(f"Ошибка: Пользователь с ID {user_id} не найден.")
        return None

    user_data['nickname'] = nickname
    user_data['description'] = description
    user_data['avatar'] = avatar

    user_ref.update(user_data)
    print(f'Профиль пользователя {user_id} успешно обновлен.')
    return user_data