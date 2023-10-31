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


#to be edited by me(adi) n vatsu n praneeth
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    age = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    bio = Column(Text)
    course_id = Column(Integer, ForeignKey("courses.course_id")) # Child table 

    def __init__(self, firstname, lastname): # constructor. Defines what to do when you do stu = Student("Bob", "Morly", ...)
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self): # this tells python what to print if you do print(student) where student is a Student object.
        return f'<Student {self.firstname}>'

class Courses(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(100), nullable=False)
    students = relationship("Student", backref="courses") # Parent table

class PhoneNumber(Base):
    __tablename__ = "phone_number"
    roll_number = Column(Integer, ForeignKey("students.id"), primary_key=True)
    phone_number = Column(String(20), primary_key=True)

class Company(Base):
    __tablename__ = "company"
    company_id = Column(Integer, primary_key=True)
    logo = Column(String(255))
    name = Column(String(100), nullable=False)

class Degree(Base):
    __tablename__ = "degree"
    program_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    branch = Column(String(100))

class InterviewExperience(Base):
    __tablename__ = "interview_experience"
    interview_id = Column(Integer, primary_key=True)
    positive_points = Column(Text)
    is_job_secured = Column(Boolean)
    improvements = Column(Text)
    roll_number = Column(Integer, ForeignKey("students.id"))
    company_id = Column(Integer, ForeignKey("company.company_id"))

class Administrator(Base):
    __tablename__ = "administrator"
    admin_id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(100), nullable=False)

class StudentDegreeHolder(Base):
    __tablename__ = "student_degree_holder"
    roll_number = Column(Integer, ForeignKey("students.id"), primary_key=True)
    program_id = Column(Integer, ForeignKey("degree.program_id"), primary_key=True)



    
