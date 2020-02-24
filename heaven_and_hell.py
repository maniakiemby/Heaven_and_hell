"""
Tego lata w Warszawie otwiera się szkoła lotnicza Heaven and Hell Sp. z.o.o.
Przez pierwsze dwa lata istnienia szkoły można będzie nauczyć się w niej latać małym samolotem oraz
śmigłowcem.
Niestety zarząd był na tyle zajęty poszukiwaniem instruktorów, że zapomniał o tym, że jest potrzebny system
informatyczny do prowadzenia szkoły. Na szczęście do projektowania bazy danych zgłosiła się firma SDA.
Od H&H SDA otrzymała następującą informację o tym, jakie dane są niezbędne do prowadzenia szkoły.
1. Informacje o kursie: cena, nazwa oraz ilość punktów ECTS, data startu oraz data końca. Kurs może być
online albo onsite.
2. Informacje o departamencie: nazwa, budżet, adres, kierownik.
3. Informacje o pracownikach: imię, nazwisko, data rozpoczęcia pracy, PESEL, telefon, adres zamieszkania.
4. Oceny kursantów.
5. Informacje o studentach: imię, nazwisko, adres zamieszkania, PESEL, telefon.
Zadaniem jest zaprojektować schemat bazy danych oraz napisać zapytania SQL, które taką bazę stworzą.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship


create = create_engine("sqlite:///C:/Users/Marcin/PycharmProjects/Średniozaawansowany-lokalny/SQL/")
Base = declarative_base()


class Course(Base):
    __tablename__ = 'course'
    course_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    credits = Column(Integer)
    department_id = Column(Integer, nullable=False)
    start_date = Column(String)
    end_date = Column(String)
    price = Column(Float)

    def __repr__(self):
        return f"Course({self.course_id}{self.title}, {self.credits}, {self.department_id}, {self.start_date}, " \
               f"{self.end_date}, {self.price})"


class OnlineCourse(Base):
    __tablename__ = 'online_course'
    course_id = Column(Integer, ForeignKey('course.course_id'), primary_key=True, nullable=False)
    url = Column(String)

    def __repr__(self):
        return f"OnlineCourse({self.course_id}, {self.url})"


class OnSiteCourse(Base):
    __tablename__ = 'onsite_course'
    course_id = Column(Integer, ForeignKey('course.course_id'), primary_key=True, nullable=False)
    address = Column(String)
    days = Column(Integer)
    time = Column(String)

    def __repr__(self):
        return f"OnsiteCourse({self.course_id}, {self.address}, {self.days}, {self.time})"


class CourseInstructor(Base):
    __tablename__ = 'instructor'
    course_id = Column(Integer, ForeignKey('course.course_id'))
    # staff_id = Column(Integer, ForeignKey('staff.staff_id'))

    staff_id = relationship('Staff', back_populates='staff_id')

    enrollment_date = Column(String)

    def __repr__(self):
        return f"CourseInstructor({self.course_id}, {self.staff_id}, {self.enrollment_date})"


class Staff(Base):  # personel
    __tablename__ = 'staff'
    staff_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    enrollment_date = Column(String)
    PESEL = Column(Integer)
    phone = Column(Integer)
    address = Column(String)

    def __repr__(self):
        return f"Staff({self.staff_id}, {self.first_name}, {self.last_name}, {self.enrollment_date}, {self.PESEL}, " \
               f"{self.phone}, {self.address})"


class Administrator(Base):
    __tablename__ = 'administrator'
    staff_id = Column(Integer, primary_key=True)
    department_id = Column(Integer)
    enrollment_date = Column(String)

    def __repr__(self):
        return f"Administrator({self.staff_id}, {self.department_id}, {self.enrollment_date})"


class Department(Base):
    __tablename__ = 'department'
    department_id = Column(Integer, primary_key=True)
    name = Column(String)
    budget = Column(Float)
    address = Column(String)

    def __repr__(self):
        return f"Department({self.department_id}, {self.name}, {self.budget}, {self.address})"


class StudentsGrade(Base):  # klasa uczniów
    __tablename__ = 'students_grade'
    course_id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    enrollment_date = Column(Integer)
    grade = Column(String)

    def __repr__(self):
        return f"StudentsGrade({self.enrollment_id}, {self.student_id}, {self.course_id}, {self.grade})"


class Student(Base):
    __tablename__ = 'student'
    student_id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    PESEL = Column(Integer)
    phone = Column(Integer)
    address = Column(String)

    def __repr__(self):
        return f"Student({self.student_id}, {self.first_name}, {self.last_name}, {self.PESEL}, {self.phone}, " \
               f"{self.address})"


Base.metadata.create_all(engine)
Session = sessionmaker(blind=engine)
session = Session()
