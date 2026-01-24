import sqlite3

def create_table():
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER,
            deleted INTEGER DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books_archive (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)

    connection.commit()
    connection.close()

def insert_books():
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM books")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute(
            "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES ('Преступление и наказание', 'Фёдор Достоевский', 1866, 'Классика', 600, 5)")
        cursor.execute(
            "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES ('Мастер и Маргарита', 'Михаил Булгаков', 1967, 'Фантастика', 480, 3)")
        cursor.execute(
            "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES ('1984', 'Джордж Оруэлл', 1949, 'Антиутопия', 328, 10)")
        cursor.execute(
            "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES ('Герой нашего времени', 'Михаил Лермонтов', 1840, 'Классика', 224, 4)")
        cursor.execute(
            "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES ('Маленький принц', 'Антуан де Сент-Экзюпери', 1943, 'Сказка', 112, 7)")
        cursor.execute(
            "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES ('Алхимик', 'Пауло Коэльо', 1988, 'Приключения', 208, 12)")
        cursor.execute(
            "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES ('Портрет Дориана Грея', 'Оскар Уайльд', 1890, 'Роман', 320, 2)")
        cursor.execute(
            "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES ('Три товарища', 'Эрих Мария Ремарк', 1936, 'Драма', 480, 6)")
        cursor.execute(
            "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES ('Унесенные ветром', 'Маргарет Митчелл', 1936, 'Роман', 1000, 3)")
        cursor.execute(
            "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES ('Ведьмак', 'Анджей Сапковский', 1993, 'Фэнтези', 320, 8)")

        connection.commit()
        print("Книги успешно добавлены!")

    connection.close()

def soft_delete(book_id):
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()

    cursor.execute(
        "SELECT name, author, publication_year, genre, number_of_pages, number_of_copies FROM books WHERE id = ?",
        (book_id,))
    book = cursor.fetchone()

    if book != None:
        cursor.execute("UPDATE books SET deleted = 1 WHERE id = ?", (book_id,))

        cursor.execute("""
            INSERT INTO books_archive (name, author, publication_year, genre, number_of_pages, number_of_copies) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (book[0], book[1], book[2], book[3], book[4], book[5]))

        connection.commit()
        print(f"Книга с ID {book_id} перемещена в архив.")

    connection.close()

def hard_delete(book_id):
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()

    cursor.execute("DELETE FROM books WHERE id = ? AND deleted = 1", (book_id,))

    connection.commit()
    connection.close()
    print(f"Попытка полного удаления книги с ID {book_id} завершена.")
if __name__ == "__main__":
    create_table()
    insert_books()
    soft_delete(2)
    hard_delete(2)