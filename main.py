import translator as tr

def crea_stringa(trans: list):
    string = ""
    for x in range(len(trans)):
        if x != len(trans) - 1:
            string += trans[x] + ", "
        else:
            string += trans[x]
    return string

t = tr.Translator()

txtIn = "-1"

while txtIn.strip() != "4":

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!
    input_cases = {"1", "2", "3", "4"}

    if txtIn.strip() not in input_cases:
        print("Attenzione, inserisci un numero valido!!")
    else:
        if int(txtIn.strip()) == 1:
            print(
                "Scrivi la nuova parola da inserire nel dizionario con i relativi significati separati da uno spazio, ad esempio: <parola> <traduzione1 traduzione2 ...>: ")
            txtIn = input()
            check = False
            try:
                check = t.handleAdd(txtIn)
            except ValueError as ve:
                print(ve)
            if check:
                print(f"Traduzione ({txtIn}) aggiunta correttamente!")
            else:
                print(f"Traduzione {txtIn} non aggiunta!")
        elif int(txtIn.strip()) == 2:
            print("Scrivi la parola da tradurre: ")
            txtIn = input()
            traduzione = None
            try:
                traduzione = t.handleTranslate(txtIn)
            except ValueError as ve:
                print(ve)
            if traduzione is None:
                print("La parola non è stata trovata nel dizionario!")
            else:
                if len(traduzione) > 1:
                    stringa = ""
                    for i in range(len(traduzione)):
                        if i != len(traduzione) - 1:
                            stringa += traduzione[i] + ", "
                        else:
                            stringa += traduzione[i]
                    print(f"{txtIn} -> {stringa}")
                else:
                    print(f"{txtIn.lower()} -> {traduzione[0]}")
        elif int(txtIn.strip()) == 3:
            print("Scrivi la parola da tradurre con wildcard. Inserisci '?' al posto della lettera sconosciuta: ")
            txtIn = input()
            if '?' not in txtIn:
                print("Attenzione, inserisci correttamente il carattere '?'")
            if txtIn.count('?') > 1:
                print("Attenzione, puoi inserire una sola volta il carattere '?'")
            else:
                translations = t.handleWildCard(txtIn.strip())
                if len(translations) == 1:
                    key = None
                    for keys in translations.keys():
                        key = keys
                    print(f"Trovata una parola sola: {key} -> {translations.get(key)[0]}")
                elif len(translations) > 1:
                    print("Trovate più parole: ")
                    for key in translations.keys():
                        if len(translations.get(key)) > 1:
                            stringa = crea_stringa(translations.get(key))
                            print(f"{key} -> {stringa}")
                        else:
                            print(f"{key} -> {translations.get(key)[0]}")
        elif int(txtIn.strip()) == 4:
            break