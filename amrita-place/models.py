from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm  import relationship, Mapped, mapped_column
from amrita_place.database import Base
from sqlalchemy.sql import func

# Example Classes for creating tables, and PK, FK relations

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

# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     username = Column(Text, nullable=False, unique=True)
#     password_hash = Column(Text)

#     def __init__(self, username, password_hash):
#         self.username = username
#         self.password_hash = password_hash
    
#     def __repr__(self):
#         return f"<User {self.username}>"

class Student(Base):
    __tablename__ = 'student'
    rollNumber = Column(String(50), primary_key=True)
    emailId = Column(String(100))
    name = Column(String(100))
    linkedInProfile = Column(String(500))
    salary = Column(Integer)
    cgpa = Column(Integer)
    companyId = Column(Integer, ForeignKey('company.companyId'))
    adminId = Column(Integer, ForeignKey('administrator.adminId'))

    def __init__(self, rollNumber, emailId, name, linkedInProfile, salary, cgpa, companyId, adminId):
        self.rollNumber = rollNumber
        self.emailId = emailId
        self.name = name
        self.linkedInProfile = linkedInProfile
        self.salary = salary
        self.cgpa = cgpa
        self.companyId = companyId
        self.adminId = adminId

class PhoneNumber(Base):
    __tablename__ = 'phoneNumber'
    rollNumber = Column(String(50), ForeignKey('student.rollNumber'), primary_key=True)
    phoneNumber = Column(String(15))

    def __init__(self, rollNumber, phoneNumber):
        self.rollNumber = rollNumber
        self.phoneNumber = phoneNumber

class Company(Base):
    __tablename__ = 'company'
    logo = Column(String(500))
    name = Column(String(100))
    companyId = Column(Integer, primary_key=True)

    def __init__(self, logo, name):
        self.logo = logo
        self.name = name

class Degree(Base):
    __tablename__ = 'degree'
    programmeId = Column(String(50), primary_key=True)
    name = Column(String(100))
    branch = Column(String(100))

    def __init__(self, programmeId, name, branch):
        self.programmeId = programmeId
        self.name = name
        self.branch = branch

class InterviewExperience(Base):
    __tablename__ = 'interviewExperience'
    interviewId = Column(Integer, primary_key=True)
    positivePoints = Column(String(500))
    isJobSecured = Column(String(10))
    improvements = Column(String(500))
    rollNumber = Column(String(50), ForeignKey('student.rollNumber'))
    companyId = Column(Integer, ForeignKey('company.companyId'))

    def __init__(self, interviewId, positivePoints, isJobSecured, improvements, rollNumber, companyId):
        self.interviewId = interviewId
        self.positivePoints = positivePoints
        self.isJobSecured = isJobSecured
        self.improvements = improvements
        self.rollNumber = rollNumber
        self.companyId = companyId

class Administrator(Base):
    __tablename__ = 'administrator'
    username = Column(String(50))
    adminId = Column(Integer, primary_key=True)
    passwordHash = Column(String(256))
    name = Column(String(100))

    def __init__(self, username, passwordHash, name):
        self.username = username
        self.passwordHash = passwordHash
        self.name = name

class StudentDegreeHolder(Base):
    __tablename__ = 'studentDegreeHolder'
    rollNumber = Column(String(50), ForeignKey('student.rollNumber'), primary_key=True)
    programmeId = Column(String(50), ForeignKey('degree.programmeId'))

    def __init__(self, rollNumber, programmeId):
        self.rollNumber = rollNumber
        self.programmeId = programmeId
        

    
