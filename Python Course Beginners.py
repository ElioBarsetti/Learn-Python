#----- Print function -----

print("   /|\ ")
print("  / | \ ")
print(" /  |  \ ")
print("/___|___\ ")
print("   |_|   ")
print("\n")

#----- Variables-----
# Data type string
character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old.")
character_name = "Mike"
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + " years old.")
print("\n")

# True or false values
is_male = True
is_Female = False

# Data type number
character_age = 50.567

#----- Working with strings -----
print("Giraffe\nAcademy")
print("Giraffe\"Academy")  #Add a cotation mark
print("\n")
phrase = "J'ecris Une Phrase"
print(phrase + " et je rajoute du stock")
print(phrase.lower()) # Met tout en minuscule
print(phrase.upper()) # Met tout en MASJUSCULE
print(phrase.isupper()) # Vérifie si toute la phrase est en masjucule (retourne True ou False)
print(phrase.islower()) # Vérifie si toute la phrase est en minuscule (retourne True ou False)
print(phrase.upper().isupper())
print(len(phrase)) # Le nombre de caractères du string
print(phrase[0]) # Retourne le premier caractère du string Python commence avec 0 (et non 1)
print(phrase[8])
print(phrase.index("P")) # Retourne l'index du P
print(phrase.index("cris")) # Cherche un string et retourne l'index du premier caractère
print(phrase.replace("e", "Z")) # Rempalce e par Z partout dans la phrase
print("\n")

#----- Working with numbers -----
print(2.583491)
print(-2.583491)
print(3 + 4.5)     # Addition
print(3 - 4.5)     # Soustraction
print(3 * 4.5)     # Multiplication
print(3 / 4.5)     # Division
print(3 * 4 + 5)   # Priorité des opérations
print(3 * (4 + 5)) # Priorité des opérations
print(10 % 3)      # Mod (modulo) donne le reste de 10 divisé par 3  (11 % 3 = 2 , 12 % 3 = 0)

my_num = 5
print(my_num)
print(str(my_num))                          # Conversion en string
print(str(my_num) + " mon numéro préféré")  # Conversion en string plus ajout de string
print(abs(-5))                              # Donne la valeur absolue du nombre
print(pow(4, 6))                            # 4 exposant 6
print(max(4, 6))                            # Retourne le plus gros chiffre
print(min(4, 6))                            # Retourne le plus petit chiffre
print(round(3.499))                         # Approxime le nombre
print(round(3.500))                         # Approxime le nombre
print("\n")

from math import*     # Importe plusieurs fonction pour des mathémagiques, c'est un module de mathématique
print(floor(3.7))     # Approxime vers le bas
print(ceil(3.2))      # Approxime vers le haut
print(sqrt(36))       # Fait la racine carrée
print("\n")

#----- Get inputs from users -----
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age )








