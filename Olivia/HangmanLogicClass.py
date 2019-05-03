#HangmanLogic

class HangmanLogic:

  #Class Variables------------------------------------------------------------

  MAX_WRONG = 7

  #Constructors---------------------------------------------------------------
  
  def __init__(self):

    self.__num_wrong_guesses = 0
    self.__correct_letter_list = []
    self.__guess_list = []

  #Accessors------------------------------------------------------------------

  def get_guess_list(self):

  def get_num_wrong_guesses(self):

  #Mutators-------------------------------------------------------------------

<<<<<<< HEAD
  def set_correct_letter_list(self, letter_list):
    self.__correct_letter_list = letter_list

  def __add_guess_to_guess_list(self, guess):
    self.__guess_list.append(guess)
=======
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
>>>>>>> d4a94c213ae057b447ccdf47cc3f558978655d52


  def __remove_correct_guess(self):
    self.__letter_list_no_repeats.remove(self.__guess)
  def __increment_wrong_guesses(self):
    self.__num_wrong_guesses += 1
<<<<<<< HEAD
<<<<<<< HEAD

  def guess_letter(self, letter):
    
=======
>>>>>>> d4a94c213ae057b447ccdf47cc3f558978655d52
=======
>>>>>>> cd8ef0bc13fdd3d5056a9ef3cbe5b4f9d1b6d646

  #Predicates-----------------------------------------------------------------

  def is_game_lost(self):
    return self.__num_wrong_guess == self.MAX_WRONG

<<<<<<< HEAD
  def is_game_won(self):
    return len(self.__letter_list_no_repeats) == 0

  def is_correct_guess(self):
    return self.__guess in self.__letter_list_no_repeats

  def is_game_over(self):
    return self.is_game_lost() or self.is_game_won()

<<<<<<< HEAD

=======
  def __guess_right_or_wrong(self):
     
>>>>>>> d4a94c213ae057b447ccdf47cc3f558978655d52
=======
  def __guess_right_or_wrong(self):
     
>>>>>>> cd8ef0bc13fdd3d5056a9ef3cbe5b4f9d1b6d646
  
