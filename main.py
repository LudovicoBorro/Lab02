import translator as tr

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
            pass
        elif int(txtIn.strip()) == 4:
            break