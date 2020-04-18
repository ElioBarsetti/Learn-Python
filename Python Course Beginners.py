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
#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("Hello " + name + "! You are " + age )


#----- Building a basic Calculator -----
#num1 = input("Enter a number: ")
#num2 = input("Enter a number: ")
#result = float(num1) + float(num2) # int, float
#print(result)



#----- Mab Libs Game -----

#color = input("Enter a color: ")
#plural_noun = input("Enter a plural noun: ")
#celebrity = input("Enter a celebrity: ")

#print("Roses are " + color)
#print(plural_noun + " are blue")
#print("I love " + celebrity)


#----- Working with Lists -----
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)
print(friends[0] + " " +  friends[2])
print(friends[-1])
print(friends[1:])
print(friends[1:4]) # Ne se rend pas jusqu'à l'index 4, il s'arrête avant

friends[1] = "Mike"
print(friends)

#----- Lists  (1h 10min 46sec) -----
lucky_number = [42, 4, 8, 15, 16, 23]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_number)
print(friends)
friends.append("Creed")
print(friends)
friends.insert(1, "Kelly") # Rajoute un élément dans la lsite et pousse les autres
print(friends)
friends.remove("Jim")
print(friends)
#friends.clear() # Vide la liste
#print
friends.pop()  # Enlève le dernier élément de la liste
print(friends)
print(friends.index("Kevin"))
print(friends.index("Toby"))

friends = ["Jim", "Kevin", "Karen", "Jim", "Oscar", "Toby", "Jim"]
print(friends.count("Jim"))
friends.sort()
print(friends)
lucky_number.sort()
print(lucky_number)
lucky_number.reverse()
print(lucky_number)

friends2 = friends.copy()
print(friends2)
print("\n")


#----- Tuples (1h 18min 59sec)  -----
coordinates = (4, 5)   # Un tuple ne peut pas être modifier
print(coordinates[0])
print(coordinates[1])

coordinates = [(4, 5), (6, 7), (80, 34)] # Une liste de tuples
print(coordinates)
print("\n")


#----- Functions (1h 24min 17sec)  -----
def say_hi():                # Définition de la fonction
    print("Hello User!")    # Tout ce qui est "tab" sera dans la fonction
    # Fin de la fonction
print("Top")
say_hi() # Appel de la fonction
print("Bottom")
print("\n")

def say_hi(name):
    print("Hello " + name + "!")
say_hi("Mike")
say_hi("Steve")
print("\n")

def say_hi(name, age):
    print("Hello " + name + "!" + " You are " + age + "!") # On utilise juste des strings
say_hi("Mike", "15")
say_hi("Steve", "47")
print("\n")

def say_hi(name, age):
    print("Hello " + name + "!" + " You are " + str(age) + "!") # On passe les int and strings
say_hi("Mike", 15)
say_hi("Steve", 47)
print("\n")


#----- Return Statement (1h 34min 11sec)  -----
def cube(num):            # Fonction qui met au cube (exposant à la 3)
    return num*num*num
result = cube(4)
print(result)
print("\n")


#----- If Statement (1h 40min 06sec)  -----
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are not a male and not tall")

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male and tall")
else:
    print("You are not a male or not tall or both")

if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are not a male and not tall")
print("\n")


#----- If Statement and Comparisons (1h 54min 07sec)  -----
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:        # On peut comparer des string, int, booleans,...
        return num1                          # >=  <=  ==  !=
    elif num2 >= num2 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(5,40,23))
print("\n")


#----- Building a better calculator (2h 00min 39sec)  -----
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op =="+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")


#----- Dictionaries (2h 07min 17sec)  -----







