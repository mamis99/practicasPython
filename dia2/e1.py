#secuencia if
num = input("Ingresa un numero entero: ")
try:
    int(num)
    check = True
except ValueError:
    check = False
if check == True:
    if int(num) % 2 == 0:
        print(f"El numero {num} es par")
        if int(num) >= 100 & int(num) < 1000:
            print(f"El número {num} es mayor o igual que 100")
        elif int(num) >= 1000:
            print(f"El numero {num} es mayor o igual que 1000")
        else:
            print(f"El numero {num} es menor que 100")
    elif int(num) % 2 != 0:
        print("El numero es impar")
else:
    print("No ingresaste un número entero")