from datetime import datetime

class Post:
    def __init__(self, post_id, user_id, nickname, text="", image_url="", timestamp=None, likes=0, comments=None):
        self.post_id = post_id
        self.user_id = user_id
        self.nickname = nickname
        self.text = text
        self.image_url = image_url
        self.timestamp = timestamp if timestamp else datetime.utcnow().isoformat()
        self.likes = likes
        self.comments = comments if comments else []

    def to_dict(self):
        return {
            "post_id": self.post_id,
            "user_id": self.user_id,
            "nickname": self.nickname,
            "text": self.text,
            "image_url": self.image_url,
            "timestamp": self.timestamp,
            "likes": self.likes,
            "comments": self.comments
        }

class Comment(Post):
    def __init__(self, comment_id, user_id, nickname, text, timestamp=None):
        super().__init__(comment_id, user_id, nickname, text, image_url="", timestamp=timestamp)
        self.comment_id = comment_id

    def to_dict(self):
        return {
            "comment_id": self.comment_id,
            "user_id": self.user_id,
            "nickname": self.nickname,
            "text": self.text,
            "timestamp": self.timestamp
        }