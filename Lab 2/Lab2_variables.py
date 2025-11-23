
entier = 42              
flottant = 3.14          
texte = "Python"         
vrai_ou_faux = True   
print(entier, "→", type(entier))
print(flottant, "→", type(flottant))
print(texte, "→", type(texte))
print(vrai_ou_faux, "→", type(vrai_ou_faux))
try:
    age = int(input("Quel âge as-tu ? "))
    print(f"Dans 5 ans tu auras {age + 5} ans.")
except ValueError:
    print("Saisie invalide, merci d'entrer un entier.")