from flask import request, jsonify
from app.services.user_service import register_step1, register_step2, login_user, update_profile

def register_step1_controller():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            print("Ошибка: Недостаточно данных для первого этапа регистрации.")
            return jsonify({"error": "Недостаточно данных"}), 400

        user_id = register_step1(email, password)
        return jsonify({"message": "Пользователь успешно зарегистрирован на первом этапе", "user_id": user_id}), 201
    except Exception as e:
        print(f"Ошибка при регистрации пользователя на первом этапе: {str(e)}")
        return jsonify({"error": str(e)}), 500

def register_step2_controller(user_id):
    try:
        data = request.json
        nickname = data.get('nickname')
        description = data.get('description', '')  # Описание опционально
        avatar = data.get('avatar', '')  # Аватарка опциональна

        if not nickname:
            print("Ошибка: Никнейм обязателен для заполнения.")
            return jsonify({"error": "Никнейм обязателен для заполнения"}), 400

        user_data = register_step2(user_id, nickname, description, avatar)
        if user_data:
            return jsonify({"message": "Профиль успешно обновлен на втором этапе"}), 200
        else:
            return jsonify({"error": "Пользователь не найден"}), 404
    except Exception as e:
        print(f"Ошибка при обновлении профиля пользователя на втором этапе: {str(e)}")
        return jsonify({"error": str(e)}), 500

def login_user_controller():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            print("Ошибка: Недостаточно данных для входа.")
            return jsonify({"error": "Недостаточно данных"}), 400

        user_id = login_user(email, password)
        if user_id:
            return jsonify({"message": "Успешный вход", "user_id": user_id}), 200
        else:
            return jsonify({"error": "Неверный email или пароль"}), 401
    except Exception as e:
        print(f"Ошибка при входе пользователя: {str(e)}")
        return jsonify({"error": str(e)}), 500

def update_profile_controller(user_id):
    try:
        data = request.json
        nickname = data.get('nickname')
        description = data.get('description', '')  # Описание опционально
        avatar = data.get('avatar', '')  # Аватарка опциональна

        if not nickname:
            print("Ошибка: Никнейм обязателен для заполнения.")
            return jsonify({"error": "Никнейм обязателен для заполнения"}), 400

        user_data = update_profile(user_id, nickname, description, avatar)
        if user_data:
            return jsonify({"message": "Профиль успешно обновлен"}), 200
        else:
            return jsonify({"error": "Пользователь не найден"}), 404
    except Exception as e:
        print(f"Ошибка при обновлении профиля пользователя: {str(e)}")
        return jsonify({"error": str(e)}), 500