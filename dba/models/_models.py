from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, UniqueConstraint, SMALLINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    username = Column(VARCHAR(50), nullable=True)
    password = Column(VARCHAR(50), nullable=True)
    email = Column(VARCHAR(50))

    UniqueConstraint(username, name='username')
    UniqueConstraint(email, name='email')


class Track(Base):

    __tablename__ = 'musical_compositions'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  
    usr = Column(VARCHAR(60), nullable=True)    
    user = relationship('User', backref='musical_composition') 
