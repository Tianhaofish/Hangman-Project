#HangmanLogic

class HangmanLogic:

  #Constructors---------------------------------------------------------------
  
  def __init__(self, word):

    self.__word = word
    self.__letter_positions = {}
    self.__random_word = {
    self.__num_wrong_guesses = 0
    self.__letter_list_no_repeats = []
    self.__guess = ''

  #Mutators-------------------------------------------------------------------

  def __set_letter_positions(self):
    letter_positions = {}
    let_list = self.__create_letter_list(self.__word)
    let_list_copy = let_list[:]
    for letter in let_list_copy:
      if letter in let_list:
        index_list = []
        while letter in let_list:
          index = let_list.index(letter)
          index_list.append(index)
          letter_positions[letter] = index_list
          let_list.remove(letter)
          let_list.insert(index, '0')
    self.__letter_positions = letter_positions

  def __set_letter_list_no_repeats(self):
    
  def __set_guess(self, guess):


  def __remove_correct_guess(self):
    self.__letter_list_no_repeats.remove(self.__guess)
  def __increment_wrong_guesses(self):
    self.__num_wrong_guesses += 1

  #Predicates-----------------------------------------------------------------
  
  def __create_letter_list(self):
    letter_list = []
    for letter in self.__word:
      letter_list.append(letter.lower())
    return letter_list

  def __win_or_lose(self):

  def __guess_right_or_wrong(self):
     
  
