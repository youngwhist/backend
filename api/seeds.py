from .models import User, Emoji, Category, Post

def seed():
    user = User.objects.create_user(username="test1", password="pass123", role="user")
    admin = User.objects.create_user(username="admin1", password="admin123", role="admin")

    emojis = ['😀', '😂', '🔥', '👍']
    for e in emojis:
        Emoji.objects.create(name=f"{e} emoji", symbol=e)

    cat1 = Category.objects.create(name="Tech")
    cat2 = Category.objects.create(name="Life")

    Post.objects.create(title="Hello World", content="My first post", author=user, category=cat1)
    Post.objects.create(title="Admin Post", content="By admin", author=admin, category=cat2)
