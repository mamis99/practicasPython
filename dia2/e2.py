year = input("Ingresa el año: ")
try:
    int(year)
    check = True
except ValueError:
    check = False
if check == True:
    if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
        print(f"{year} es un año bisiesto")
    else:
        print(f"{year} no es un año bisiesto")
else:
    print("No ingresaste un año")
