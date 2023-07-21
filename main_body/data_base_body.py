import sqlite3 as sq
from main_body import Word
from random import choice


class DataBase:
    def __init__(self):
        self.make_data_base()

    def make_data_base(self):
        with sq.connect('eng_word.db') as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS eng_words (
            word TEXT,
            translation TEXT
            )""")

    def add_data(self, word: Word):
        with sq.connect('eng_word.db') as con:
            cur = con.cursor()
            if self.check_availability(word):
                cur.execute(f"""INSERT INTO eng_words VALUES (
                '{word.word}',
                '{word.translation}'
                )""")

    def get_random_data(self):
        with sq.connect('eng_word.db') as con:
            cur = con.cursor()
            res = cur.execute("""SELECT * FROM eng_words""")
            return choice([*res])

    @staticmethod
    def check_availability(data):
        flag = True
        with sq.connect('eng_word.db') as con:
            cur = con.cursor()
            res = cur.execute("""SELECT * FROM eng_words""")
            for item in res:
                if data.word in item:
                    flag = False
        return flag



if __name__ == '__main__':
    db = DataBase()
    w = Word('hello', 'привіт')
    w1 = Word('home', 'дім')
    w2 = Word('tree', 'дерево')
    w3 = Word('sky', 'небо')
    db.add_data(w)
    db.add_data(w1)
    db.add_data(w2)
    db.add_data(w3)
    print(db.get_random_data())
