class Word:
    def __init__(self, word, translation):
        self.word = word
        self.translation = translation


    def __str__(self):
        return f'{self.word} {self.translation}'