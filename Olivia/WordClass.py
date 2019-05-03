#WordClass

from HangmanModule import *
import random

class Word:

  def __init__(self, word, category):

    self.__word = word
    self.__length = 0
    self.__category = category
    self.__letter_list_no_repeats = []
    self.__letter_positions = {}
    self.__random_word_dict = {'animal':['zebra', 'buffalo', 'porcupine', \
                                         'alligator', 'pelican', 'polar bear'],
                               'sport':['baseball', 'basketball', 'tennis',\
                                        'rowing', 'badminton', 'pickleball'], \
                               'country':['Austria', 'Argentina', 'Greece', \
                                          'Canada', 'Croatia', 'Germany'], \
                               'movie':['Endgame', 'Avatar', 'Jurassic Park', \
                                        'Iron Man', 'Toy Story', 'Interstellar']}
    self.__random_word_categories = ['animal', 'sport', 'country', 'movie']

  #Accessors------------------------------------------------------------------
    
  def get_word(self):
    return self.__word
  
  def get_word_length(self):
    return self.__length

  def get_category(self):
    return self.__category

  def get_letter_position(self, letter):
    return self.__letter_positions[letter]

  def get_letter_list_no_repeats(self):
  

  #Mutators-------------------------------------------------------------------

  def __set_word_length(self):
    self.__length = len(self.__word)

  def __set_letter_positions(self):
    letter_positions = {}
    let_list = create_letter_list(self.__word)
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

  def __set_random_word_and_category(self):
    index = random.randint(0, (len(self.__random_word_categories) - 1))
    self.__category = self.__random_word_categories[index]
    word_list = self.__random_word_dict[self.__category]
    word_index = random.randint(0, (len(word_list) - 1))
    self.__word = word_list.pop(word_index)
    if len(word_list) == 0:
      random_word_categories.remove(category)
    self.__set_word_length()

  #iterate over letters in self.__word and add each unique letter
  ##(no repeated letters) to a list, where each letter is its own
  ## element. set list to self.__letter_list_no_repeats
  def __set_letter_list_no_repeats(self):


    
