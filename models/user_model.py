class User:
    def __init__(self, user_id, email, password, nickname="", description="", avatar=""):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.nickname = nickname
        self.description = description
        self.avatar = avatar

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "email": self.email,
            "password": self.password,
            "nickname": self.nickname,
            "description": self.description,
            "avatar": self.avatar
        }