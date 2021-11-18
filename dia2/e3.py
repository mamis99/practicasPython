num1 = int(input("Ingresa un numero: "))

par = False
ocho = False

if num1 % 2 == 0:
    par = True
    if num1 == 8:
        ocho = True
if par:
    print(f"El número {num1} es par")
    if ocho:
        print("El número que ingresaste es 8")
elif not par:
    print(f"El número {num1} es impar")