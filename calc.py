def operator():
    print("Kalkylator för att addera två tal\n")
    tal1 = int(input("Skriv det första talet: "))
    vald_operator = input("skriv operaton")
    tal2 = int(input("Skriv det andra talet: "))

    if vald_operator == "-":
        resultat = tal1 - tal2
    elif vald_operator == "+":
        resultat = tal1 + tal2 
    elif vald_operator == "*":
        resultat = tal1 * tal2
    elif vald_operator == "/":
        resultat = tal1 / tal2
    else:
        print("Ogiltig operator")
        return

    print(tal1, vald_operator, tal2, "=", resultat)


if __name__ == "__main__":    operator()