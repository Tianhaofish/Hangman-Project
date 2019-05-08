#WordClass

import random

class Word:

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
                                        'cucumber']}
    self.__random_word_categories = ['animal', 'sport', 'country', 'movie', \
                                     'fruit']

  #Accessors------------------------------------------------------------------
    
  def get_word(self):
    return self.__word

  def get_category(self):
    return self.__category

  def get_letter_position(self, letter):
    index_list = []
    let_list = self.__create_letter_list(self.__word)
    while letter in let_list:
      index = let_list.index(letter)
      index_list.append(index)
      let_list.remove(letter)
      let_list.insert(index, '0')
    return index_list

  def get_letter_list_no_repeats(self):
    for i in self.__word:
      if i.lower() not in self.__letter_list_no_repeats and i != ' ':
        self.__letter_list_no_repeats.append(i.lower())
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

  def __create_letter_list(self, word):
    letter_list = []
    for letter in word:
      letter_list.append(letter.lower())
    return letter_list
