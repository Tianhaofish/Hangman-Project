#HangmanModule

def create_letter_list(word):
  letter_list = []
  for letter in word:
    letter_list.append(letter.lower())
  return letter_list
