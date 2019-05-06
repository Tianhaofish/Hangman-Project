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
                                        'Iron Man', 'Toy Story', 'Interstellar'],\
                               'fruit':['banana','water mellon','apple','peach','cucumber']}
    self.__random_word_categories = ['animal', 'sport', 'country', 'movie','fruit']

  #Accessors------------------------------------------------------------------
    
  def get_word(self):
    return self.__word
  
  def get_word_length(self):
    self.__length = len(self.__word)
    return self.__length

  def get_category(self):
    return self.__category

  def get_letter_position(self,letter):
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
    return self.__letter_positions[letter]

  def get_letter_coordinates(self,letter):
    letter_coordinates={}
    for i in self.__letter_positions[letter]:
        letter_coordinates[letter]=35+i*40
    return letter_coordinates


  def get_letter_list_no_repeats(self):
    for i in self.__word:
      if i not in self.__letter_list_no_repeats:
        self.__letter_list_no_repeats.append(i)
    return self.__letter_list_no_repeats
  

  #Mutators-------------------------------------------------------------------

  def set_random_word_and_category(self):
    index = random.randint(0, (len(self.__random_word_categories) - 1))
    self.__category = self.__random_word_categories[index]
    word_list = self.__random_word_dict[self.__category]
    word_index = random.randint(0, (len(word_list) - 1))
    self.__word = word_list.pop(word_index)
    if len(word_list) == 0:
      random_word_categories.remove(category)



    
