#HangmanLogic

class HangmanLogic:

  #Constructors---------------------------------------------------------------
  def __init__(self, word):

    self.__word = word
    self.__letter_positions = {}

  #Mutators-------------------------------------------------------------------

  def __set_letter_positions(self, self.__word):
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

  #Predicates-----------------------------------------------------------------
  
  def __create_letter_list(self, self.__word):
    letter_list = []
    for letter in self.__word:
      letter_list.append(letter.lower())
    return letter_list
