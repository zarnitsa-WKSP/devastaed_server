from firebase_admin import db
from app.models.post_model import Post, Comment
import uuid

def add_post(user_id, post_id, post_data):
    ref = db.reference(f'posts/{user_id}/{post_id}')
    ref.set(post_data)
    print(f'Пост {post_id} добавлен в базу данных для пользователя {user_id}.')

def get_user_nickname(user_id):
    user_ref = db.reference(f'users/{user_id}')
    user_data = user_ref.get()
    if user_data:
        return user_data.get('nickname', '')
    return ''  # проверка на существование пользователя, который хочет лайкнуть пост

def check_post_id_exists(user_id, post_id):
    ref = db.reference(f'posts/{user_id}/{post_id}')
    return ref.get() is not None  # проверка на существование нового айди поста

def create_post(user_id, text="", image_url=""):
    nickname = get_user_nickname(user_id)
    if not nickname:
        print(f"Ошибка: Никнейм пользователя с ID {user_id} не найден.")
        return None

    post_id = str(uuid.uuid4())
    post_data = Post(post_id, user_id, nickname, text, image_url).to_dict()
    add_post(user_id, post_id, post_data)
    print(f'Пост {post_id} успешно создан для пользователя {user_id}.')
    return post_id

def like_post(user_id, post_id):
    # Получаем все посты всех пользователей
    posts_ref = db.reference('posts')
    posts = posts_ref.get()

    if not posts:
        print("Ошибка: Посты не найдены.")
        return None

    # Ищем пост по post_id
    for user_posts in posts.values():
        if post_id in user_posts:
            post_ref = db.reference(f'posts/{user_id}/{post_id}')
            post_data = post_ref.get()

            if not post_data:
                print(f"Ошибка: Пост с ID {post_id} не найден.")
                return None

            post_data['likes'] += 1
            post_ref.update(post_data)
            print(f'Пост {post_id} лайкнут пользователем {user_id}.')
            return post_data['likes']

    print(f"Ошибка: Пост с ID {post_id} не найден.")
    return None

def check_comment_id_exists(user_id, post_id, comment_id):
    ref = db.reference(f'posts/{user_id}/{post_id}/comments/{comment_id}')
    return ref.get() is not None  # проверка на существование нового айди комментария

def add_comment(user_id, post_id, comment_id, comment_data):
    ref = db.reference(f'posts/{user_id}/{post_id}/comments')
    ref.child(comment_id).set(comment_data)
    print(f'Комментарий {comment_id} добавлен к посту {post_id} пользователя {user_id}.')

def create_comment(user_id, post_id, text):
    nickname = get_user_nickname(user_id)
    if not nickname:
        print(f"Ошибка: Никнейм пользователя с ID {user_id} не найден.")
        return None

    while True:
        comment_id = str(uuid.uuid4())
        if not check_comment_id_exists(user_id, post_id, comment_id):
            break  # сама проверочка осуществляется тут

    comment_data = Comment(comment_id, user_id, nickname, text).to_dict()
    add_comment(user_id, post_id, comment_id, comment_data)
    print(f'Комментарий {comment_id} успешно создан к посту {post_id} пользователя {user_id}.')
    return comment_id