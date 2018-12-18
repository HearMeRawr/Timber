from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True)
  email = Column(String(256))
  password = Column(String(256))

'''class Post(db.Model):
  __tablename__ = "posts"
  
  id = Column(Integer, primary_key=True)
  authorID = Column(Integer, ForeignKey('users.id'))
  title = Column(String)
  content = Column(String)
  postTime = Column()
  editTime = Column()
  
  author = relationship("User", back_populates="posts")'''
  