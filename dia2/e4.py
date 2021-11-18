#Año bisiesto con banderas
year = int(input("Escribe el año: "))

year_bi = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            year_bi = True
    else:
        year_bi = True

if year_bi:
    print(f"{year} es bisiesto")
elif not year_bi:
    print(f"{year} no es bisiesto")