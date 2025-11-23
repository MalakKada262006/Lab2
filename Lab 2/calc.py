
print("Bienvenue dans la calculatrice!")
try:
    x=float(input("Entrer le premier nombre:"))
    y=float(input("Entrer le deuxième nombre:"))
except ValueError:
    print("Erreur: veuillez entrer des nombres valides")
    exit()
print("Choisir l'opération:")
print("+: Addition")
print("-: Soustraction")
print("*: Addition")
print("/: Division")
choix = input("Votre choix est : ")
try:
    if choix == "+":
        resultat = x + y
    elif choix == "-":
        resultat = x - y
    elif choix == "*":
        resultat = x * y 
    elif choix == "/":
        resultat = x / y
    else:
        print("Erreur : opérateur invalide.")
        exit()
    print(f"Résultat : {x} {choix} {y} = {resultat}")
except ZeroDivisionError:
    print("Erreur : division par zéro impossible !")       



