import sqlite3

def get_connection():
    return sqlite3.connect("studybuddy.db")

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER,
            topic TEXT,
            status TEXT,
            FOREIGN KEY(subject_id) REFERENCES subjects(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT,
            test_name TEXT,
            marks_obtained REAL,
            total_marks REAL
        )
    ''')

    conn.commit()
    conn.close()
