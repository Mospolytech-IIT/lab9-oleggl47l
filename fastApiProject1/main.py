from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import SessionLocal, User, Post
from crud import create_user, get_users, get_user, update_user, delete_user, create_post, get_posts, get_post, update_post, delete_post
from schemas import UserCreate, PostCreate, UserUpdate, PostUpdate, UserOut, PostOut

app = FastAPI()

app = FastAPI()

def get_db():
    """get_db"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршруты для пользователей (Users)
@app.post("/users/", response_model=UserOut)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    """create_new_user"""
    return create_user(db=db, user=user)

@app.get("/users/", response_model=list[UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """read_users"""
    return get_users(db=db, skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """read_users"""
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=UserOut)
def update_user_info(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    """update_user_info"""
    db_user = update_user(db=db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}")
def delete_user_info(user_id: int, db: Session = Depends(get_db)):
    """delete_user_info"""
    delete_user(db=db, user_id=user_id)
    return {"message": "User deleted successfully"}

# Маршруты для постов (Posts)
@app.post("/posts/", response_model=PostOut)
def create_new_post(post: PostCreate, db: Session = Depends(get_db)):
    """create_new_post"""
    return create_post(db=db, post=post)

@app.get("/posts/", response_model=list[PostOut])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """read_posts"""
    return get_posts(db=db, skip=skip, limit=limit)

@app.get("/posts/{post_id}", response_model=PostOut)
def read_post(post_id: int, db: Session = Depends(get_db)):
    """read_posts"""
    db_post = get_post(db=db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.put("/posts/{post_id}", response_model=PostOut)
def update_post_info(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    """update_post_info"""
    db_post = update_post(db=db, post_id=post_id, post=post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.delete("/posts/{post_id}")
def delete_post_info(post_id: int, db: Session = Depends(get_db)):
    """delete_post_info"""
    delete_post(db=db, post_id=post_id)
    return {"message": "Post deleted successfully"}
