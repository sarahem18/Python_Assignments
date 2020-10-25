import urllib.request
import random

def chooseWord():
  file_name = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/coolWords.txt"
  my_file = urllib.request.urlopen(file_name)
  long_string = my_file.read()
  long_string = long_string.decode("utf-8")
  word_list = long_string.split("\n")
  word = random.choice(word_list)
  word = word.lower()
  return word

def body_parts(wrongGuess):
  if wrongGuess == 1:
    print("  (_)  ")
  if wrongGuess == 2:
    print("  (_)  ")
    print("   |   ")
    print("   |   ")
  if wrongGuess == 3:
    print("  (_)  ")
    print("  /|   ")
    print(" / |   ")
  if wrongGuess == 4:
    print("  (_)  ")
    print("  /|\  ")
    print(" / | \ ")
  if wrongGuess == 5:
    print("  (_)  ")
    print("  /|\  ")
    print(" / | \ ")
    print("  /    ")
    print(" /     ")
  if wrongGuess == 6:
    print("  (_)  ")
    print("  /|\  ")
    print(" / | \ ")
    print("  / \  ")
    print(" /   \ ")

def hangman(word):
  complete_word = '_' * len(word)
  guessed = False
  guess_letter = []
  guess_word = []
  tries = 6
  wrong_count = 0
  while not guessed and tries > 0:
    guess = input("choose a letter:").lower()
    if guess not in word:
      print(guess," is not in the word.")
      tries -= 1
      wrong_count += 1
      guess_letter.append(guess)
      body_parts(wrong_count)
    else:
      print(guess," is in the word!")
      guess_letter.append(guess)
      list_of_char = list(complete_word)
      indices = [i for i, letter in enumerate(word) if letter == guess]
      for index in indices:
        list_of_char[index] = guess
      complete_word = ''.join(list_of_char)
      print(complete_word)
      if not '_' in complete_word:
        guessed == True
  if guessed:
    print("Congrats, you won!")
  else:
    print("You lose. The word was", word)

def play_hangman():
  word = chooseWord()
  hangman(word)

if __name__ == "__main__":
    play_hangman()
