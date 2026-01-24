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
    connection.commit()
    connection.close()


def insert_books():
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM books")
    if cursor.fetchone()[0] == 0:
        sample_books = [
            ('1984', 'Джордж Оруэлл', 1949, 'Антиутопия', 328, 10),
            ('Алхимик', 'Пауло Коэльо', 1988, 'Приключения', 208, 12),
            ('Ведьмак', 'Анджей Сапковский', 1993, 'Фэнтези', 320, 8)
        ]
        for book in sample_books:
            cursor.execute(
                "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES (?, ?, ?, ?, ?, ?)",
                book)
        connection.commit()
    connection.close()

def select_all_books():
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    all_books = cursor.fetchall()

    print("\n--- Список всех книг в базе ---")
    for book in all_books:
        print(book)

    connection.close()

def update_book_name(book_id, new_name):
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET name = ? WHERE id = ?", (new_name, book_id))
    connection.commit()
    connection.close()
    print(f"\nНазвание книги с ID {book_id} успешно изменено на: {new_name}")

def delete_book(book_id):
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    connection.commit()
    connection.close()
    print(f"\nКнига с ID {book_id} полностью удалена из базы.")

if __name__ == "__main__":
    create_table()
    insert_books()

    print("Состояние ДО изменений:")
    select_all_books()
    update_book_name(1, "Супер-Книга 2024")

    delete_book(3)

    print("\nСостояние ПОСЛЕ изменений:")
    select_all_books()