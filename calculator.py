print("Simpel lommeregner")

tal1 = float(input("Indtast første tal: "))
operator = input("Vælg operator (+, -, *, /): ")
tal2 = float(input("Indtast andet tal: "))

if operator == "+":
    resultat = tal1 + tal2
elif operator == "-":
    resultat = tal1 - tal2
elif operator == "*":
    resultat = tal1 * tal2
elif operator == "/":
    if tal2 == 0:
        print("Fejl: Du kan ikke dividere med 0.")
        exit()
    resultat = tal1 / tal2
else:
    print("Fejl: Ukendt operator.")
    exit()

print("Resultat:", resultat)
