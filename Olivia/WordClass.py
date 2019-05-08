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

RESTATEMENT: This class encapsulates the word used in the Hangman
game, and the methods related to it.

IN IT:
  self.__word - initialized to argument word
  self.__category - initialized to argument category
  self.__letter_list_no_repeats - initialized as empty list,
                             is the list of uniques letters in the word
  self.__random_word_dict - initialized to dictionary of word, with the
                        category as the key and the value a list of word
  self.__random_word_categories - initialized as list of category keys
                             from self.__random_word_dict

METHODS:
  Accessors -
    get_word()
    get_category()
    get_letter_position()
    get_letter_list_no_repeats()
  Mutators -
    set_random_word_and_category()
    __create_letter_list()
'''

import random

class Word:

  #collaborative
  def __init__(self, word, category):

    self.__word = word
    self.__category = category
    self.__letter_list_no_repeats = []
    self.__random_word_dict = {'animal':['zebra', 'buffalo', 'porcupine', \
                                         'alligator', 'pelican', 'polar bear'],
                               'sport':['baseball', 'basketball', 'tennis',\
                                        'rowing', 'badminton', 'pickleball'], \
                               'country':['Austria', 'Argentina', 'Greece', \
                                          'Canada', 'Croatia', 'Germany'], \
                               'movie':['Endgame', 'Avatar', 'Lion King', \
                                        'Iron Man', 'Toy Story', \
                                        'Interstellar'],
                               'fruit':['banana','watermellon','apple','peach',\
                                        'cucumber', 'grapes']}
    self.__random_word_categories = ['animal', 'sport', 'country', 'movie', \
                                     'fruit']

  #Accessors------------------------------------------------------------------

  #returns self.__word
  #collaborative
  def get_word(self):
    return self.__word

  #returns self.__category
  #collaborative
  def get_category(self):
    return self.__category

  #returns list of indexes of the letter in the word
  #coded by Olivia
  def get_letter_position(self, letter):
    index_list = []
    let_list = self.__create_letter_list(self.__word)
    while letter in let_list:
      index = let_list.index(letter)
      index_list.append(index)
      let_list.remove(letter)
      let_list.insert(index, '0')
    return index_list

  #returns list of unique letters in the word, except spaces
  #coded by Tianhao
  def get_letter_list_no_repeats(self):
    for i in self.__word:
      if i.lower() not in self.__letter_list_no_repeats and i != ' ':
        self.__letter_list_no_repeats.append(i.lower())
    return self.__letter_list_no_repeats
  

  #Mutators-------------------------------------------------------------------

  #selects a random integer and uses this integer as an index
  #  to access a category from self.__random _word_categories.
  #  Then accesses the list of words of that category from
  #  self.__random_word_dict. Select another random integer
  #  to use as an index for the word in the list
  #  set self.__word and self.__category
  #  coded by Olivia
  def set_random_word_and_category(self):
    index = random.randint(0, (len(self.__random_word_categories) - 1))
    self.__category = self.__random_word_categories[index]
    word_list = self.__random_word_dict[self.__category]
    word_index = random.randint(0, (len(word_list) - 1))
    self.__word = word_list.pop(word_index)
    if len(word_list) == 0:
      random_word_categories.remove(category)

  #creates a list of letters in the word (repeats and spaces allowed)
  #  and makes them all lower case. Used for finding index of letters
  #coded by Olivia
  def __create_letter_list(self, word):
    letter_list = []
    for letter in word:
      letter_list.append(letter.lower())
    return letter_list
