"""crud"""
from fastapi import FastAPI
from sqlalchemy.orm import Session
from models import User, Post
from schemas import UserCreate, PostCreate, UserUpdate, PostUpdate

# Users
def create_user(db: Session, user: UserCreate):
    """create_user"""
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    """get_user"""
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """get_users"""
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user: UserUpdate):
    """update_user"""
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.username = user.username
        db_user.email = user.email
        db_user.password = user.password
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"message": f"User {user_id} and their posts have been deleted"}
    else:
        return {"error": "User not found"}


# Posts
def create_post(db: Session, post: PostCreate):
    """create_post"""
    db_post = Post(title=post.title, content=post.content, user_id=post.user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post(db: Session, post_id: int):
    """get_post"""
    return db.query(Post).filter(Post.id == post_id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    """get_posts"""
    return db.query(Post).offset(skip).limit(limit).all()


def update_post(db: Session, post_id: int, post: PostUpdate):
    """update_post"""
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db_post.title = post.title
        db_post.content = post.content
        db.commit()
        db.refresh(db_post)
    return db_post


def delete_post(db: Session, post_id: int):
    """delete_post"""
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
