import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

computer = random.randint(0, len(game) - 1)
print("0.- Rock\n1.- Paper\n2.- Scissors")
choice = int(input("Make a choice: "))

if choice == 0 and computer == 2:
    print("User wins!")
elif choice == 2 and computer == 0:
    print("Computer wins!")
elif choice == computer:
    print("It's a tie :/")
elif choice > computer:
    print("User wins!")
elif computer > choice:
    print("Computer wins!")

#Enseñar el juego
print("User's choice: ")
print(game[choice])    #Se muestra el elemento de la lista game de acuerdo a la posicion seleccionada por el usuario
print("Computer's choice: ", computer)
print(game[computer])  #Se muestra el elemento de la lista game de acuerdo a la posicion seleccionada por la computadora