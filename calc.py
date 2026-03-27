def addition():
    print("Kalkylator för att addera två tal")
    try:
        tal1 = int(input("Skriv det första talet: "))
        tal2 = int(input("Skriv det andra talet: "))

        resultat = tal1 + tal2 

        print(tal1, "+", tal2, "=", resultat)

    except ValueError:
        print("skriv en siffra inte nåt annat")
    except Exception as e:
        print("fel:", e)
