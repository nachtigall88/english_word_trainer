import sqlite3 as sq

class DataBase:
    def __init__(self):
        self.make_data_base()

    def make_data_base(self):
        with sq.connect('eng_word.db') as con:
            cur = con.cursor()
            cur.execute("""
            """)

    def add_data(self):
        pass

if __name__ == '__main__':
    db = DataBase()