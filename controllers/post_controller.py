from flask import request, jsonify
from app.services.post_service import create_post, like_post, create_comment

def create_post_controller():
    try:
        data = request.json
        user_id = data.get('user_id')
        text = data.get('text', '')
        image_url = data.get('image_url', '')

        if not user_id:
            print("Ошибка: Недостаточно данных для создания поста.")
            return jsonify({"error": "Недостаточно данных"}), 400

        post_id = create_post(user_id, text, image_url)
        if post_id:
            return jsonify({"message": "Пост успешно создан", "post_id": post_id}), 201
        else:
            return jsonify({"error": "Ошибка при создании поста"}), 500
    except Exception as e:
        print(f"Ошибка при создании поста: {str(e)}")
        return jsonify({"error": str(e)}), 500

def like_post_controller(user_id, post_id):
    try:
        likes = like_post(user_id, post_id)
        if likes is not None:
            return jsonify({"message": "Пост лайкнут", "likes": likes}), 200
        else:
            return jsonify({"error": "Пост не найден"}), 404
    except Exception as e:
        print(f"Ошибка при лайке поста: {str(e)}")
        return jsonify({"error": str(e)}), 500

def create_comment_controller(user_id, post_id):
    try:
        data = request.json
        text = data.get('text')

        if not text:
            print("Ошибка: Недостаточно данных для создания комментария.")
            return jsonify({"error": "Недостаточно данных"}), 400

        comment_id = create_comment(user_id, post_id, text)
        if comment_id:
            return jsonify({"message": "Комментарий успешно создан", "comment_id": comment_id}), 201
        else:
            return jsonify({"error": "Ошибка при создании комментария"}), 500
    except Exception as e:
        print(f"Ошибка при создании комментария: {str(e)}")
        return jsonify({"error": str(e)}), 500