'''
Olivia Klett
Tianhao Dai
olett1@binghamton.edu
tdai2@binghamton.edu
Lab Section A52
Elizabeth Vorshylo
Final project
'''
'''
ANALYSIS

RESTATEMENT: This class encapsulates the game logic used in the Hangman
game, and the methods related to it.

CONSTANTS:
  MAX_WORNG - 6

IN IT:
  self.__num_wrong_guesses - initialized to 0
  self.__correct_letter_list - initialized to empty list
  self.__correct_letter_list_copy - initialized to empty list
  self.__guess_list - initialized to empty list

METHODS:
  Accessors -
    get_guess_list()
    get_correct_letter_list_copy()
    get_num_wrong_guesses()
    
  Mutators -
    set_correct_letter_list()
    __add_guess_to_guess_list()
    __remove_correct_guess()
    __increment_wrong_guesses()
    process_guess()
    
  Predicates -
    is_game_lost()
    is_game_won()
    is_correct_guess()
'''

class Game:

  #Class Variables------------------------------------------------------------

  MAX_WRONG = 6

  #Constructors---------------------------------------------------------------

  #collaborative
  def __init__(self):

    self.__num_wrong_guesses = 0
    self.__correct_letter_list = []
    self.__correct_letter_list_copy = []
    self.__guess_list = []

  #Accessors------------------------------------------------------------------

  #returns self.__guess_list
  #collaborative
  def get_guess_list(self):
    return self.__guess_list

  #returns self.__correct_letter_list
  #collaborative
  def get_correct_letter_list_copy(self):
    return self.__correct_letter_list_copy

  #returns self.__num_wrong_guesses
  #collaborative
  def get_num_wrong_guesses(self):
    return self.__num_wrong_guesses

  #Mutators-------------------------------------------------------------------

  #sets self.__correct_guess_list and self.__correct_guess_list_copy
  #  to list argument
  #coded by Tianhao
  def set_correct_letter_list(self, letter_list):
    self.__correct_letter_list = letter_list
    self.__correct_letter_list_copy = letter_list + letter_list

  #appends guess argument to self.__guess_list
  #coded by Tianhao
  def __add_guess_to_guess_list(self, guess):
    self.__guess_list.append(guess)

  #removes guess argument from self.__correct_guess_list
  #coded by Tianhao
  def __remove_correct_guess(self, guess):
    self.__correct_letter_list.remove(guess)

  #increases incorrect guesses by 1
  #coded by Tianhao
  def __increment_wrong_guesses(self):
    self.__num_wrong_guesses += 1

  #determines if guess argument is correct, and invokes
  #  self.__remove_correct_guess if it is, otherwise
  #  invokes self.__increment_wrong_guesses
  #coded by Olivia
  def process_guess(self, guess):
    self.__add_guess_to_guess_list(guess)
    if self.is_correct_guess(guess):
       self.__remove_correct_guess(guess)
    else:
      self.__increment_wrong_guesses()
    

  #Predicates-----------------------------------------------------------------

  #determines if person has guesses the maximum number
  # of wrong guesses
  #coded by Olivia
  def is_game_lost(self):
    return self.__num_wrong_guesses == self.MAX_WRONG

  #determines if the perosn has guessed all of the letters in the word
  #coded by Olivia
  def is_game_won(self):
    return len(self.__correct_letter_list) == 0

  #determines if guess is correct
  #coded by Tianhao
  def is_correct_guess(self, guess):
    return guess in self.__correct_letter_list_copy
