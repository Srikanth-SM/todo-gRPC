import datetime
from sqlalchemy import Column, String, Integer, Boolean, create_engine,DateTime
from sqlalchemy.orm import sessionmaker, relationship, validates
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://root@localhost/todo", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Todo(Base):
    
    __tablename__ = "todos"
    id = Column('id',Integer, primary_key=True)
    todo_text = Column('todo_text',String(100), nullable=False)
    # created_at = Column('created_at',DateTime,default=datetime.datetime.now())
    status = Column(Integer, nullable=False,default=0)


    def asdict(self):
        row_dict = {}
        for col in self.__table__.columns.keys():
            row_dict[col] = getattr(self, col)

        return row_dict
        