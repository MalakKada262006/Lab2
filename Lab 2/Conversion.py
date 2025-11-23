
print("Conversion de température : ")
try:
    C=float(input("Entrer une valeur en Celsius : "))
except ValueError:
    print("Erreur : veuillez entre un nombre valide : ")
    exit()
F = (C * 9/5) + 32
K = C + 273.15
print(f"{C}°C ={F:.2f}°F")
print(f"{C}°C ={F:.2f}K")
print("\nVoulez-vous faire une conversion inverse?")
print("1 - Fahrenheit --> Celsius")
print("2 - Kelvin --> Celsius")
print("3 - non")
choix = input("Votre choix : ")
if choix =="1":
    F2 = float(input("Entrer °F : "))
    C2 = (F2 - 32) * 5/9
    print(f"{F2}°F = {C2:.2f}°C")
elif choix == "2":
    K2 = float(input("Entrer K :")) 
    C2 = K2 - 273.15
    print(f"{K2}K = {C2:.2f}°C")
else:
    print("Fin du programme.")       
