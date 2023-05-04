import random

wordlist = ['test', 'paper', 'language']
chosen_word = random.choice(wordlist)
word_length = len(chosen_word)
display = []
lives = 7

# print(chosen_word)
# word display set up
for i in range(0, word_length):
  display.append("_")

game_end = False

while not game_end:
  print(f"{' '.join(display)}")
  print(f"life: {lives}")
# letter guessing mechanic
  guess = input("guess a letter: ").lower()
  for position in range(0, word_length):
    letter = chosen_word[position]
    if guess == letter:
      display[position] = letter
  if guess not in chosen_word:
    lives -= 1 
# win/lose conditions
  if "_" not in display:
    game_end = True
    print("You win")
  elif lives == 0:
    game_end = True
    print("You lose")
