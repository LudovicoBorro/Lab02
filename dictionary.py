class Dictionary:
    def __init__(self):
        self.dictionary = {}

    def addWord(self, word, meanings: list):
        self.dictionary[word] = meanings

    def translate(self, word: str):
        if word not in self.dictionary.keys():
            raise ValueError(f"Parola {word} non esistente nel dizionario!!")
        return self.dictionary[word]

    def translateWordWildCard(self, part1: str, part2: str):
        translations = []
        for word in self.dictionary.keys():
            if len(part1) == 0:
                check = word.find(part2, 1, len(word))
                if check != -1:
                    translations.append(word)
            elif len(part2) == 0:
                check = word.find(part1, 0, len(word)-1)
                if check != -1:
                    translations.append(word)
            else:
                check1 = word.find(part1, 0, len(part1))
                check2 = word.find(part2, len(part1), len(word))
                if check1 != -1 and check2 != -1 and len(part1) + len(part2) == len(word) - 1:
                    translations.append(word)
        trad = {}
        for parola in translations:
            traduzioni = self.translate(parola)
            trad[parola] = traduzioni
        return trad

    def check_parola(self, parola):
        if parola.lower().strip() in self.dictionary.keys():
            return True
        return False