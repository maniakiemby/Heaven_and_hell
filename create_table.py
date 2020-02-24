from sqlalchemy import create_engine


def create_db(engine):
    queries = [
        'CREATE TABLE IF NOT EXISTS Languages (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR);',
        'CREATE TABLE IF NOT EXISTS Categories (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR);',
        'CREATE TABLE IF NOT EXISTS Levels (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, description VARCHAR);',

        """
        CREATE TABLE IF NOT EXISTS Cources (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            lessons INTEGER NOT NULL,
            description VARCHAR,
            language_id INTEGER,
            level_id INTEGER,
            category_id INTEGER,
            price FLOAT,
            start_date DATETIME,
            end_date DATETIME,

            FOREIGN KEY (category_id) REFERENCES Categories(id),
            FOREIGN KEY (language_id) REFERENCES Languages(id),
            FOREIGN KEY (level_id) REFERENCES Levels(id)
        );
        """,

        "INSERT INTO Languages(name) VALUES('English');",
        "INSERT INTO Languages (name) VALUES ('German');",
        "INSERT INTO Languages(name) VALUES('French');",
        "INSERT INTO Languages(name) VALUES('Italian');",

        "INSERT INTO Categories(name) VALUES('Conversation course');",
        "INSERT INTO Categories(name) VALUES('Business');",
        "INSERT INTO Categories(name) VALUES('Kids');",
        "INSERT INTO Categories(name) VALUES('Exam preparation');",
        "INSERT INTO Categories(name) VALUES('Adults');",

        "INSERT INTO Levels(name, description) VALUES('A0', 'Beginners');",
        "INSERT INTO Levels(name, description) VALUES('A1', 'Beginners');",
        "INSERT INTO Levels(name, description) VALUES('A2', 'Beginner');",
        "INSERT INTO Levels(name, description) VALUES('B1', 'Pre-intermediate');",
        "INSERT INTO Levels(name, description) VALUES('B2', 'Intermediate');",
        "INSERT INTO Levels(name, description) VALUES('C1', 'Advanced');",
        "INSERT INTO Levels(name, description) VALUES('C2', 'Fluent');"
    ]

    for query in queries:
        execute_query(engine, query)


def execute_query(engine, query):
    return engine.execute(query)


def select_all(engine, table):
    return engine.execute(f'select * from {table}').fetchall()


if __name__ == '__main__':
    # url = 'sqlite:///:memory:'  # in RAM
    url = 'sqlite:///speaknfly.sqlite'
    engine = create_engine(url)

    create_db(engine)
    print('DB has been created')
    print('Available Levels')

    for item in select_all(engine, 'Levels'):
        print(item)
