class Dictionary:
    def __init__(self):
        self.dictionary = {}

    def addWord(self, word, meanings: list):
        self.dictionary[word] = meanings

    def translate(self, word: str):
        if word not in self.dictionary.keys():
            raise ValueError(f"Parola {word} non esistente nel dizionario!!")
        return self.dictionary[word]

    def translateWordWildCard(self):
        pass