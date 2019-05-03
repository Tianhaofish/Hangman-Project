#HangmanLogic

class Game:

  #Class Variables------------------------------------------------------------

  MAX_WRONG = 7

  #Constructors---------------------------------------------------------------
  
  def __init__(self):

    self.__num_wrong_guesses = 0
    self.__correct_letter_list = []
    self.__guess_list = []

  #Accessors------------------------------------------------------------------

  def get_guess_list(self):
    return self.__guess_list

  def get_num_wrong_guesses(self):
    return self.__num_wrong_guesses

  #Mutators-------------------------------------------------------------------

  def set_correct_letter_list(self, letter_list):
    self.__correct_letter_list = letter_list

  def __add_guess_to_guess_list(self, guess):
    self.__guess_list.append(guess)

  def __remove_correct_guess(self, guess):
    self.__correct_letter_list.remove(guess)

  def __increment_wrong_guesses(self):
    self.__num_wrong_guesses += 1

  def guess_letter(self, letter):
    return
    

  #Predicates-----------------------------------------------------------------

  def is_game_lost(self):
    return self.__num_wrong_guesses == self.MAX_WRONG

  def is_game_won(self):
    return len(self.__correct_letter_list) == 0

  def is_correct_guess(self, guess):
    return guess in self.__letter_list_no_repeats

  def is_game_over(self):
    return self.is_game_lost() or self.is_game_won()


  
