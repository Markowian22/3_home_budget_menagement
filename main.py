from application import Application
from repository import Repository
import sqlite3


def init_db(db_cursor):
    """
    Initializes the database.

    Parameters
    ----------
    db_cursor : sqlite3.Cursor
        Cursor to the SQLite3 database.
    """
    db_cursor.execute(
        """CREATE TABLE IF NOT EXISTS categories
                (ID INTEGER PRIMARY KEY, name TEXT)"""
    )

    db_cursor.execute(
        """CREATE TABLE IF NOT EXISTS items
                (ID INTEGER PRIMARY KEY,
                name TEXT,
                category_id INTEGER,
                amount REAL,
                date TEXT,
                FOREIGN KEY (category_id) REFERENCES categories(ID))"""
    )


if __name__ == "__main__":

    with sqlite3.connect("budget.db") as database:
        cursor = database.cursor()
        init_db(cursor)
        repository = Repository(database)
        main = Application(repository)
        main.main()
