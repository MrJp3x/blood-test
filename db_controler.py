import sqlite3

from base_vars import present_date


class DatabaseController:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                test_type TEXT NOT NULL,
                result TEXT NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_test(self, test_type, result, date):
        try:
            self.cursor.execute('''
                INSERT INTO tests (test_type, result, date)
                VALUES (?, ?, ?)
            ''', (test_type, result, date))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def fetch_tests(self):
        try:
            self.cursor.execute('SELECT * FROM tests')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []

    def update_test(self, test_id, test_type, result, date):
        try:
            self.cursor.execute('''
                UPDATE tests
                SET test_type = ?, result = ?, date = ?
                WHERE id = ?
            ''', (test_type, result, date, test_id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def delete_test(self, test_id):
        try:
            self.cursor.execute('''
                DELETE FROM tests
                WHERE id = ?
            ''', (test_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def search_tests(self, search_query):
        try:
            self.cursor.execute('''
                SELECT * FROM tests
                WHERE test_type LIKE ? OR result LIKE ? OR date LIKE ?
            ''', ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []

    def close(self):
        self.connection.close()
