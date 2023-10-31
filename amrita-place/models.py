# from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
# from sqlalchemy.orm  import relationship, Mapped, mapped_column
# from database import Base
# from sqlalchemy.sql import func

# # Example Classes for creating tables, and PK, FK relations

# class Student(Base):
#     __tablename__ = 'students'
#     id = Column(Integer, primary_key=True)
#     firstname = Column(String(100), nullable=False)
#     lastname = Column(String(100), nullable=False)
#     email = Column(String(80), unique=True, nullable=False)
#     age = Column(Integer)
#     created_at = Column(DateTime(timezone=True),
#                            server_default=func.now())
#     bio = Column(Text)
#     course_id = mapped_column(ForeignKey("courses.course_id")) # Child table 

#     def __init__(self, firstname, lastname): # constructor. Defines what to do when you do stu = Student("Bob", "Morly", ...)
#         self.firstname = firstname


#     def __repr__(self): # this tells python what to print if you do print(student) where student is a Student object.
#         return f'<Student {self.firstname}>'
    
# class Courses(Base):
#     __tablename__ = "courses"
#     course_id = Column(Integer, primary_key=True)
#     course_name = Column(String(100), nullable=False)
#     children = relationship() # Parent table
#   # add __init__ and __repr__ definitions to all classes

#Above code: patch1 - not official, only for trials and testing (Courses table doesnt exist)
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    roll_no = Column(Integer, primary_key=True)
    email_id = Column(String)
    name = Column(String)
    linkedIN_profile = Column(String)
    salary = Column(Integer)
    CGPA = Column(Integer)
    companyID = Column(Integer, ForeignKey('company.CompanyID'))
    adminID = Column(Integer, ForeignKey('administrator.AdminID'))

class PhoneNumber(Base):
    __tablename__ = 'phone_number'
    rollNumber = Column(Integer, ForeignKey('student.roll_no'), primary_key=True)
    phoneNumber = Column(String)

class Company(Base):
    __tablename__ = 'company'
    logo = Column(String)
    name = Column(String)
    CompanyID = Column(Integer, primary_key=True)

class Degree(Base):
    __tablename__ = 'degree'
    programID = Column(Integer, primary_key=True)
    name = Column(String)
    branch = Column(String)

class InterviewExperience(Base):
    __tablename__ = 'interview_experience'
    interviewID = Column(Integer, primary_key=True)
    positivePoints = Column(String)
    isJobSecured = Column(String)
    improvements = Column(String)
    rollNumber = Column(Integer, ForeignKey('student.roll_no'))
    companyID = Column(Integer, ForeignKey('company.CompanyID'))

class Administrator(Base):
    __tablename__ = 'administrator'
    username = Column(String)
    AdminID = Column(Integer, primary_key=True)
    PasswordHash = Column(String)
    Name = Column(String)

class StudentDegreeHolder(Base):
    __tablename__ = 'student_degree_holder'
    rollNumber = Column(Integer, ForeignKey('student.roll_no'), primary_key=True)
    ProgrammeID=Column(Integer, ForeignKey('degree.programID'))

