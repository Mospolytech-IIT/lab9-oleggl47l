"""Create db"""
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Post

DATABASE_URL = "postgresql://postgres:123Qq123@localhost"


def create_database():
    """create_database"""
    connection = psycopg2.connect(DATABASE_URL)
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'db_lab9'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute('CREATE DATABASE db_lab9')
        print("Database 'db_lab9' created successfully.")
    cursor.close()
    connection.close()


create_database()

DATABASE_URL = "postgresql://postgres:123Qq123@localhost/db_lab9"

engine = create_engine(DATABASE_URL)


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()


def create_sample_data():
    """create_sample_data"""
    user = User(username="olegg", email="oleg@example.com", password="123123123123")
    session.add(user)
    session.commit()

    post = Post(title="The First Post", content="The first content of the first post.", user_id=user.id)
    session.add(post)
    session.commit()


create_sample_data()

session.close()

print("Tables created and sample data inserted successfully.")
