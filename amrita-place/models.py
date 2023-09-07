from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm  import relationship, Mapped, mapped_column
from database import Base
from sqlalchemy.sql import func

# Example Classes for creating tables, and PK, FK relations

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    age = Column(Integer)
    created_at = Column(DateTime(timezone=True),
                           server_default=func.now())
    bio = Column(Text)
    course_id = mapped_column(ForeignKey("courses.course_id")) # Child table 

    def __init__(self, firstname, lastname): # constructor. Defines what to do when you do stu = Student("Bob", "Morly", ...)
        self.firstname = firstname


    def __repr__(self): # this tells python what to print if you do print(student) where student is a Student object.
        return f'<Student {self.firstname}>'
    
class Courses(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(100), nullable=False)
    children = relationship() # Parent table
  # add __init__ and __repr__ definitions to all classes

    
