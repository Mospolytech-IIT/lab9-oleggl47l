"""db_operations"""
from models import SessionLocal, User, Post


def get_db():
    """get_db"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def add_users():
    """add_users"""
    db = next(get_db())

    users = [
        User(username="Luke", email="luke@example.com", password="mtfbwy"),
        User(username="Anakin", email="anakin@example.com", password="mtfbwy"),
        User(username="Ahsoka", email="ahsoka@example.com", password="mtfbwy")
    ]

    db.add_all(users)
    db.commit()
    print("Users added successfully.")


def add_posts():
    """add_posts"""
    db = next(get_db())

    user1 = db.query(User).filter(User.username == "Luke").first()
    user2 = db.query(User).filter(User.username == "Anakin").first()
    user3 = db.query(User).filter(User.username == "Ahsoka").first()

    posts = [
        Post(title="Luke's First Post", content="This is Luke's first post.", user_id=user1.id),
        Post(title="Anakin's First Post", content="This is Anakin's first post.", user_id=user2.id),
        Post(title="Ahsoka's First Post", content="This is Ahsoka's first post.", user_id=user3.id)
    ]

    db.add_all(posts)
    db.commit()
    print("Posts added successfully.")


def get_all_users():
    """get_all_users"""
    db = next(get_db())
    users = db.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

def get_all_posts_with_users():
    """get_all_posts_with_users"""
    db = next(get_db())
    posts = db.query(Post).join(User).all()
    for post in posts:
        print(f"Post Title: {post.title}, Content: {post.content}, Author: {post.user.username}")


def get_posts_by_user(username):
    """get_posts_by_user"""
    db = next(get_db())
    user = db.query(User).filter(User.username == username).first()
    if user:
        posts = db.query(Post).filter(Post.user_id == user.id).all()
        for post in posts:
            print(f"Post Title: {post.title}, Content: {post.content}")
    else:
        print(f"User {username} not found.")


def update_user_email(username, new_email):
    """update_user_email"""
    db = next(get_db())
    user = db.query(User).filter(User.username == username).first()
    if user:
        user.email = new_email
        db.commit()
        print(f"Email of {username} updated to {new_email}.")
    else:
        print(f"User {username} not found.")


def update_post_content(post_title, new_content):
    """update_post_content"""
    db = next(get_db())
    post = db.query(Post).filter(Post.title == post_title).first()
    if post:
        post.content = new_content
        db.commit()
        print(f"Content of post '{post_title}' updated.")
    else:
        print(f"Post '{post_title}' not found.")


def delete_post(post_title):
    """delete_post"""
    db = next(get_db())
    post = db.query(Post).filter(Post.title == post_title).first()
    if post:
        db.delete(post)
        db.commit()
        print(f"Post '{post_title}' deleted.")
    else:
        print(f"Post '{post_title}' not found.")


def delete_user_and_posts(username):
    """delete_user_and_posts"""
    db = next(get_db())
    user = db.query(User).filter(User.username == username).first()
    if user:
        db.query(Post).filter(Post.user_id == user.id).delete()
        db.delete(user)
        db.commit()
        print(f"User {username} and their posts deleted.")
    else:
        print(f"User {username} not found.")


if __name__ == "__main__":
    add_users()
    add_posts()

    print("\nAll Users:")
    get_all_users()

    print("\nAll Posts with Users:")
    get_all_posts_with_users()

    print("\nPosts by Anakin:")
    get_posts_by_user("Anakin")

    update_user_email("Anakin", "new_anakin@example.com")
    update_post_content("Anakin's First Post", "Updated content for Anakin's first post.")

    delete_post("Ahsoka's First Post")
    delete_user_and_posts("Luke")
