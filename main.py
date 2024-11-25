from flask import Flask
from app.controllers.user_controller import register_step1_controller, register_step2_controller, login_user_controller, update_profile_controller
from app.controllers.post_controller import create_post_controller, like_post_controller, create_comment_controller
from app.firebase_config import initialize_firebase

app = Flask(__name__)

# Инициализация Firebase SDK
initialize_firebase()

@app.route("/")
def home():
    return "It's home page"

# Конечная точка для первого этапа регистрации (логин и пароль)
app.add_url_rule('/register_step1', 'register_step1', register_step1_controller, methods=['POST'])

# Конечная точка для второго этапа регистрации (никнейм, описание, аватарка)
app.add_url_rule('/register_step2/<user_id>', 'register_step2', register_step2_controller, methods=['PUT'])

# Конечная точка для входа в учетную запись
app.add_url_rule('/login', 'login_user', login_user_controller, methods=['POST'])

# Конечная точка для обновления настроек профиля пользователя
app.add_url_rule('/update_profile/<user_id>', 'update_profile', update_profile_controller, methods=['PUT'])

# Конечная точка для создания поста
app.add_url_rule('/create_post', 'create_post', create_post_controller, methods=['POST'])

# Конечная точка для лайка поста
app.add_url_rule('/like_post/<user_id>/<post_id>', 'like_post', like_post_controller, methods=['POST'])

# Конечная точка для создания комментария
app.add_url_rule('/create_comment/<user_id>/<post_id>', 'create_comment', create_comment_controller, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)