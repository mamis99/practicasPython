import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like to password?: "))
nr_numbers = int(input("How many numbers would you like to password?: "))
nr_symbols = int(input("How many symbols would you like to password?: "))


#Easy mode
password_s = ""   #se crea una cadena vacia
for _ in range(1, nr_letters + 1):
    password_s += random.choice(letters)    #Se concatena una letra al azar a la cadena password_s
for _ in range(1, nr_numbers + 1):
    password_s += random.choice(numbers)    #Se concatena un numero al azar a la cadena password_s
for _ in range(1, nr_symbols + 1):
    password_s += random.choice(symbols)    #Se concatena un simbolo al azar a la cadena password_s

print(f"Your password is: {password_s}")    #Se imprime toda la cadena ya concatenada por letras, numeros y simbolos

#Hard mode
password_list = []  #Se crea una lista vacía
for _ in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))  #Se agrega una letra al azar en la lista password_list
for _ in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))  #Se agrega un numero al azar en la lista password_list
for _ in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))  #Se agrega un simbolo al azar en la lista password_list

random.shuffle(password_list)   #Mezcla la lista password_list, reorganizando el orden de los elementos
string_list_password = ''    #se crea una cadena auxiliar para guardar la lista ya mezclada
for element in password_list:
    string_list_password += element     #se concatena cada elemento de la lista en la cadena auxiliar llamada string_list_password
print(f"Your password is: {string_list_password}")    #Se imprime toda la cadena de la contraseña ya mezclada