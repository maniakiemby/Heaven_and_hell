from sqlalchemy import create_engine


def create_db(engine):
    queries = [
        """
        CREATE TABLE IF NOT EXISTS Department (
        id INTEGER NOT NULL PRIMARY KEY,
        name VARCHAR,
        budget(PLN) MONEY,
        address VARCHAR(60));
        """,

        """
        CREATE TABLE IF NOT EXISTS Course (
        id INTEGER NOT NULL PRIMARY KEY,
        title VARCHAR NOT NULL,
        credits INTEGER,
        department_id INTEGER NOT NULL,
        start_date DATETIME,
        end_date DATETIME,
        price FLOAT);
        """,

        """
        CREATE TABLE IF NOT EXISTS Online_course (
        course_id INTEGER PRIMARY KEY,
        url VARCHAR,
        
        FOREIGN KEY (course_id) REFERENCES Course(id));
        """,

        """
        CREATE TABLE IF NOT EXISTS On_site_course (
        course_id INTEGER PRIMARY KEY,
        address VARCHAR,
        days INTEGER,
        time VARCHAR,
        
        FOREIGN KEY (course_id) REFERENCES Course(id));
        """,

        """
        CREATE TABLE IF NOT EXISTS Staff (
        id INTEGER NOT NULL PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        enrollment_date DATETIME,
        pesel INTEGER(11),
        phone VARCHAR(12),
        address VARCHAR);
        """,

        """
        CREATE TABLE IF NOT EXISTS Administrator (
        staff_id INTEGER PRIMARY KEY,
        department_id INTEGER,
        enrollment_date DATETIME,
        
        FOREIGN KEY (staff_id) REFERENCES Staff(id),
        FOREIGN KEY (department_id) REFERENCES Department(id));
        """,

        """
        CREATE TABLE IF NOT EXISTS Students_grade (
        course_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        enrollment_date DATETIME,
        grade VARCHAR,
        
        FOREIGN KEY (course_id) REFERENCES Course(id),
        FOREIGN KEY (student_id) REFERENCES Student(id));
        """,

        """
        CREATE TABLE IF NOT EXISTS Student (
        id INTEGER NOT NULL PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        pesel INTEGER(11),
        phone VARCHAR(14),
        address VARCHAR(60));
        """,

        """
        CREATE TABLE IF NOT EXISTS Instructor (
        course_id INTEGER NOT NULL PRIMARY KEY,
        staff_id INTEGER NOT NULL,
        enrollment_date DATETIME,
        
        FOREIGN KEY (course_id) REFERENCES Course(id),
        FOREIGN KEY (staff_id) REFERENCES Staff(id));
        """,
    ]

    for query in queries:
        execute_query(engine, query)


def execute_query(engine, query):
    return engine.execute(query)


if __name__ == '__main__':
    url = 'sqlite:///heaven_and_hell.sqlite'
    engine = create_engine(url)

    create_db(engine)
    print('DB has been created')
    print('Available Levels')
