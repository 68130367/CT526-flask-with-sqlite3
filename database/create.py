import sqlite3
import os
from datetime import date, timedelta
import random

DB_NAME = "ct526.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS movies (
        mid INTEGER PRIMARY KEY AUTOINCREMENT,
        m_name TEXT NOT NULL,
        release_date DATE NOT NULL,
        genre TEXT NOT NULL,
        country TEXT NOT NULL
    );
    """
    try:
        with get_db_connection() as conn:
            conn.execute(sql_create_table)
        print(f"'{DB_NAME}'")
    except sqlite3.Error as e:
        print(f"{e}")


def insert_data(m_name, release_date, genre, country):
    sql_insert = (
        "INSERT INTO movies (m_name, release_date, genre, country) VALUES (?, ?, ?, ?);"
    )

    try:
        with get_db_connection() as conn:
            conn.execute(sql_insert, (m_name, release_date, genre, country))
        print(f"เพิ่มข้อมูลสำเร็จ")
        return True
    except sqlite3.IntegrityError:
        return False
    except sqlite3.Error as e:
        print(f"{e}")
        return False


def view_all_data():
    sql_select = "SELECT * FROM movies ORDER BY mid;"

    try:
        with get_db_connection() as conn:
            cursor = conn.execute(sql_select)
            rows = cursor.fetchall()

            if not rows:
                return []
            results = [dict(row) for row in rows]

            return results

    except sqlite3.Error as e:
        print(f"เกิดข้อผิดพลาด ao: {e}")
        return []


days_offset = random.randint(0, 365 * 2)
random_date = date.today() - timedelta(days=days_offset)

create_table()
insert_data("Terminal", random_date, "Drama", "USA")
insert_data("Terminator", random_date, "Sci-Fi", "England")
insert_data("Determinator", random_date, "Horror", "Finland")
insert_data("Harry Potter", random_date, "Fantasy", "England")
insert_data("Love Next Door", random_date, "Comedy", "Thailand")
all_items = view_all_data()
