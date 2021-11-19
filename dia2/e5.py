"""De acuerdo a tu estatura puedes ingresar al juego y de acuerdo
a tu edad es lo que te cobran y ya un extra si querias fotografía"""

height = int(input("What is your height in cm?: "))
can_ride = False
if height >= 120:
    can_ride = True

if can_ride:
    age = int(input("How old are you?: "))
    bill = 0
    if age < 12:
        #bill = bill + 5
        bill += 5
    elif age <= 18:
        bill += 7
    elif age <= 45:
        bill += 9
    if input("Do you want a photo? (y/n): ").lower() == 'y':
        bill += 3
    print(f"You have to pay ${bill}")
elif not can_ride:
    print("Yo cannot ride")