import random
people = ["Isaac", "Ana", "Juan", "Manuel", "Priscila"]

#Escoger una posicion al azar de la lista people
lucky_person1 = people[random.randint(0, len(people))]
print("La persona escogida de la lista predeterminada es: ", lucky_person1)

#Escoger un elemento al azar de la lista people
lucky_person2 = random.choice(people)
print("La persona escogida de la lista predeterminada es: ", lucky_person2)

#Pedir los elementos de una lista (se quedan guardados como cadena)
names_string = input("Dame todos los nombres que quieras meter a una lista (separados por una 'coma'): ")

#Split (Separar la cadena "names_string" mediante la separación que es ", ")
#Esa separacion se va guardando en una lista
names_list = names_string.split(", ")
print("Esta es tu lista personalizada: ", names_list)
print("El elegido de tu lista personalizada es: ", names_list[random.randint(0, len(names_list))])