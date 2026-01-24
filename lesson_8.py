import sqlite3


def create_tables(connection):
    connection.execute('''DROP TABLE IF EXISTS students''')
    connection.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT,
        age INTEGER,
        city TEXT 
    )
    ''')


def add_student(connection, student_name, age, city):
    connection.execute('''
    INSERT INTO students
    (student_name, age, city) VALUES 
    (?, ?, ?)
    ''', (student_name, age, city))
    connection.commit()


def delete_student(connection, student_id):
    connection.execute(
        '''
    DELETE FROM students WHERE student_id = ? ''',
        (student_id,)
    )
    connection.commit()


def delet_student_by_name(connection, sdtudent_name):


if __name__ == '__main__':
    conn = sqlite3.connect("database.db")
    create_tables(conn)

    add_student(conn, "Данил", 18, "Бишкек")
    add_student(conn, "Данил", 18, "Кара-Балта")
    add_student(conn, "Аян", 20, "Бишкек")
    add_student(conn, "Игорь", 18, "Каракол")
    delete_student(conn, 1)
    for st in get_all_students(conn):
        print(st)

    print(get_all_students(conn))
