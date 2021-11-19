#Como importar librerias
#Programa para imprimir elementos de una lista
#Uso de la libreria random

import random

list = [12, 0.3, True, 'hello']
print(f"Imprimiendo un elemento de la lista: {list[0]}")
print(f"Imprimiendo un elemento random de la lista: {random.choice(list)}")
print(f"Imprimiendo toda la lista: {list}")

var = random.randint(1, 100)
print(f"Numero aleatorio entre 1 y 100: {var}")

coin = ["head", "tails"]
if random.choice(coin) == "head":
    print("head")
elif random.choice(coin) == "tails":
    print("tails")