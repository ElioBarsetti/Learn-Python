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
print(phrase.islower()) #V érifie si toute la phrase est en minuscule (retourne True ou False)
print(phrase.upper().isupper())