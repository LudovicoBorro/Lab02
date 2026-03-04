from dictionary import Dictionary

class Translator:
    def __init__(self):
        self.dizionario = Dictionary()
        self.dicts = None

    @classmethod
    def printMenu(cls):
        print("----------------------------------")
        print(f"   Translator Alien-Italian")
        print("----------------------------------")
        # 1. Aggiungi nuova parola
        print("1. Aggiungi una nuova parola")
        # 2. Cerca una traduzione
        print("2. Cerca una traduzione")
        # 3. Cerca con wildcard
        print("3. Cerca con wildcard")
        # 4. Exit
        print("4. Exit")
        print("----------------------------------")

    def loadDictionary(self, dicts):
        # dicts is a string with the filename of the dictionary
        try:
            file = open(dicts, 'r')
            for riga in file.readlines():
                meanings = []
                campi = riga.split(" ")
                word = campi[0].lower().strip()
                meaning = campi[1].lower().strip()
                meanings.append(meaning)
                if len(campi) > 2:
                    for i in range(2,len(campi)):
                        meanings.append(campi[i].lower().strip())
                self.dizionario.addWord(word, meanings)
            file.close()
        except FileNotFoundError:
            raise FileNotFoundError(f"File {dict} non trovato!!")
        self.dicts = dicts

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        entry = entry.split(" ", 1)
        parola_aliena = entry[0].lower().strip()
        if not parola_aliena.isalpha():
            raise ValueError(f"Parola {parola_aliena} non valida!!")
        meanings = []
        for meaning in entry[1].split(" "):
            if not meaning.lower().strip().isalpha():
                raise ValueError(f"Meaning {meaning.lower().strip().isalpha()} non valida!!")
            meanings.append(meaning.lower().strip())

        if self.dizionario.check_parola(parola_aliena):
            raise ValueError(f"Parola {parola_aliena} già inserita!!")

        self.dizionario.addWord(parola_aliena, meanings)

        # Aggiunta parola al file di testo
        with open(self.dicts, 'a') as file:
            stringa = ""
            for i in range(0,len(meanings)):
                if i == len(meanings)-1:
                    stringa += meanings[i]
                else:
                    stringa += meanings[i] + " "
            file.write("\n" + parola_aliena + " " + stringa)
        return True

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        if not query.isalpha():
            raise ValueError(f"La parola {query} non è valida!!")
        return self.dizionario.translate(query.lower().strip())

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        parti = query.lower().split("?")
        return self.dizionario.translateWordWildCard(parti[0].strip(), parti[1].strip())