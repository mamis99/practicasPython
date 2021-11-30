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

word_list = ['hangman', 'computer', 'travel', 'airplane']
chosen_word = random.choice(word_list)
lenght_word = len(chosen_word)

display = []
for char in chosen_word:
    display.append("_")
print(display)

"""for _ in range(chosen_lenght):
    display.append("_")"""

lives = 6
end_of_game = True

while end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(lenght_word):
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