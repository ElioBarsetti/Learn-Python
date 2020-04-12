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
print(str(my_num)) # Conversion en string
print(str(my_num) + " mon numéro préféré")












