#Hangman game with functions
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def random_choice_word():
    word_list = ['hangman', 'computer', 'travel', 'airplane']
    return random.choice(word_list)

def create_display(chosen_word):
    display = []
    for char in chosen_word:
        display.append("_")
    return display

"""for _ in range(chosen_lenght):
    display.append("_")"""

def check_character(chosen_word, display, stages):
    lives = 6
    end_of_game = True

    while end_of_game:
        guess = input("Guess a letter: ").lower()
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        
        if guess not in chosen_word:
            lives -= 1
            print(stages[lives])
            if lives == 0:
                end_of_game = False
                print('You lose')
        print(display)
        
        if '_' not in display:
            end_of_game = False
            final_word = ''
            for element in display:
                final_word += element
            print('You win')
            print(f'The secret word is {final_word}')

chosen_word = random_choice_word()
print(chosen_word)
display_out_function = create_display(chosen_word)
print(display_out_function)
check_character(chosen_word, display_out_function, stages)