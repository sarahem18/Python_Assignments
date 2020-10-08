hello = "hello world"
print(hello.upper())
print(hello.lower())

def hasVowels(word):
  word = word.lower()
  if "a" in word:
    return True
  if "e" in word:
    return True
  if "i" in word:
    return True
  if "o" in word:
    return True
  if "u" in word:
    return True
  else:
    return False

while True:
  user_input = input('enter a word that contains a vowel:')
  if hasVowels(user_input) == False:
    user_input = input('enter a word that contains a vowel:')
  else:
    break

def countVowels(word):
  count = 0
  word = word.lower()
  for letter in word:
    if hasVowels(letter) == True:
      count += 1
  return count

word_list = []
user_word = input("Enter a word, or type stop to stop:")
user_word = user_word.lower()
while not user_word == 'stop':
  word_list.append(user_word)
  user_word = input("Enter a word, or type stop to stop:")
print(word_list)

total_vowels = 0
for user_word in word_list:
  if countVowels(user_word) != 0:
    total_vowels = total_vowels + countVowels(user_word)
  continue
print(total_vowels)
