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

RESTATEMENT:

INPUT from keyboard:
  self.__guess_entry_box (str)
  self.__set_word_entry_box (str)
  self.__set_category_entry_box (str)
  self.__random_word_button (event)
  self.__set_word_button (event)

OUTPUT to monitor:
  self.__win (TK window)
  self.__canvas (TK canvas widget)
  self.__category_label (label)
  self.__category_val (str var)
  self.__guess_list_label (label)
  self.__guess_list_var (str var)
  self.__guess_letter_label (label)
  self.__guess_entry_box (entry box)
  self.__start_game_label (label)
  self.__random_word_button (button)
  self.__or_label (label)
  self.__set_word_label (label)
  self.__word_label (label)
  self.__set_word_entry_box (entry box)
  self.__category_label (label)
  self.__set_category_entry_box (entry box)
  self.__set_word_button (button)

CONSTANTS:
  CANVAS_FONT - ('Calibri', 20)
  GUI_FONT - ('Calibri', 12)
  FRAME_PADX - 5
  CANVAS_COLOR - 'alice blue'
  BG_COLOR - 'lightblue3'
  BUTTON_COLOR - 'sky blue'
  LETTER_INDEX_POSITIONS - {0:(35, 335), 1:(75, 335), 2:(115, 335), \
                            3:(155, 335), 4:(195, 335), 5:(235, 335), \
                            6:(275, 335), 7:(315, 335), 8:(355, 335), \
                            9:(395, 335), 10:(435, 335), 11:(475, 335)}

IN IT:
  self.__game - initialized to None
  self.__word - initialized to None

METHODS:
  Event Handlers -
    __guess_letter()
    __set_word()
    __set_random_word()
    
  Mutators -
    __draw_lines()
    __draw_gallow()
    __draw_head()
    __draw_body()
    __draw_leg1()
    __draw_leg2()
    __draw_arm1()
    __draw_arm2()
    __write_correct_guess()
    __win_game()
    __lose_game()
    __reset_game()
     
  Predicates -
    __is_valid_letter()
    __is_valid_word()

'''

from tkinter import *
from tkinter import messagebox
from WordClass import *
from GameClass import *

class HangmanGUI:

  #Class Constants------------------------------------------------------------

  CANVAS_FONT = ('Calibri', 20)
  GUI_FONT = ('Calibri', 12)
  FRAME_PADX = 5
  CANVAS_COLOR = 'alice blue'
  BG_COLOR = 'lightblue3'
  BUTTON_COLOR = 'sky blue'
  LETTER_INDEX_POSITIONS = {0:(35, 335), 1:(75, 335), 2:(115, 335), \
                            3:(155, 335), 4:(195, 335), 5:(235, 335), \
                            6:(275, 335), 7:(315, 335), 8:(355, 335), \
                            9:(395, 335), 10:(435, 335), 11:(475, 335)}

  #Constructor----------------------------------------------------------------

  #collaborative
  def __init__(self):

    self.__game = None
    self.__word = None

    self.__win = Tk()

    #Main frames-------------------------------------

    self.__left_frame = Frame(self.__win)
    self.__left_frame.pack(side='left')

    self.__right_frame = Frame(self.__win, bg=self.BG_COLOR)
    self.__right_frame.pack(side='left')

    #Canvas------------------------------------------

    self.__canvas = Canvas(self.__left_frame, height=401, width=510, \
                           bg=self.CANVAS_COLOR, highlightbackground='black')
    self.__canvas.pack()

    #Draw gallow-------------------------------------

    self.__canvas.create_line(140, 280, 330, 280, width=2.0)
    self.__canvas.create_line(235, 280, 235, 50, width=2.0)
    self.__canvas.create_line(235, 50, 330, 50, width=2.0)
    self.__canvas.create_line(330, 50, 330, 100, width=2.0)

    #frames within right frame-----------------------

    self.__top_right_frame1 = Frame(self.__right_frame, padx=self.FRAME_PADX, \
                                    pady=15, bg=self.BG_COLOR)
    self.__top_right_frame1.pack()

    self.__top_right_frame2 = Frame(self.__right_frame, padx=self.FRAME_PADX, \
                                   bg=self.BG_COLOR)
    self.__top_right_frame2.pack()

    self.__mid_right_frame1 = Frame(self.__right_frame, padx=self.FRAME_PADX, \
                                    pady=25, bg=self.BG_COLOR)
    self.__mid_right_frame1.pack()

    self.__mid_right_frame2 = Frame(self.__right_frame, padx=self.FRAME_PADX, \
                                    pady=10, bg=self.BG_COLOR)
    self.__mid_right_frame2.pack()

    self.__mid_right_frame3 = Frame(self.__right_frame, padx=self.FRAME_PADX,\
                                    bg=self.BG_COLOR)
    self.__mid_right_frame3.pack()

    self.__mid_right_frame4 = Frame(self.__right_frame, padx=self.FRAME_PADX, \
                                    pady=7, bg=self.BG_COLOR)
    self.__mid_right_frame4.pack()

    self.__mid_right_frame5 = Frame(self.__right_frame, padx=self.FRAME_PADX, \
                                    bg=self.BG_COLOR)
    self.__mid_right_frame5.pack()

    self.__mid_right_frame6 = Frame(self.__right_frame, padx=self.FRAME_PADX, \
                                    bg=self.BG_COLOR)
    self.__mid_right_frame6.pack()

    self.__mid_right_frame7 = Frame(self.__right_frame, padx=self.FRAME_PADX, \
                                    bg=self.BG_COLOR)
    self.__mid_right_frame7.pack()

    self.__bot_right_frame = Frame(self.__right_frame, padx=self.FRAME_PADX, \
                                   bg=self.BG_COLOR)
    self.__bot_right_frame.pack()

    #Category display--------------------------------

    self.__category_label = Label(self.__top_right_frame1, text='Category: ', \
                                  font=self.GUI_FONT, bg=self.BG_COLOR)
    self.__category_label.pack(side='left')

    self.__category_val = StringVar()
    self.__category_val.set('')

    self.__category_val_label = Label(self.__top_right_frame1, \
                                      textvariable = self.__category_val, \
                                      font=self.GUI_FONT, bg=self.BG_COLOR)
    self.__category_val_label.pack(side='left')

    #Display guesses---------------------------------

    self.__guess_list_label = Label(self.__top_right_frame2, \
                                    text='Guesses: ', font=self.GUI_FONT, \
                                    bg=self.BG_COLOR)
    self.__guess_list_label.pack()

    self.__guess_list_var = StringVar()
    self.__guess_list_var.set('')

    self.__guess_list_var_label = Label(self.__top_right_frame2, \
                                        textvariable=self.__guess_list_var, \
                                        font=self.GUI_FONT, bg=self.BG_COLOR)
    self.__guess_list_var_label.pack()

    #Guess letter------------------------------------

    self.__guess_letter_label = Label(self.__mid_right_frame1, \
                                      text='Guess Letter:', \
                                      font=self.GUI_FONT, bg=self.BG_COLOR)
    self.__guess_letter_label.pack(side='left')

    self.__guess_entry_box = Entry(self.__mid_right_frame1, width=10)
    self.__guess_entry_box.pack(side='left')
    self.__guess_entry_box.bind('<Return>', self.__guess_letter)

    #Start game label--------------------------------

    self.__start_game_label = Label(self.__mid_right_frame2, text=\
                                    'To start game: ', font=self.GUI_FONT, \
                                    bg=self.BG_COLOR)
    self.__start_game_label.pack()

    #Pick random word button-------------------------

    self.__random_word_button = Button(self.__mid_right_frame3, \
                                       text='Pick Random Word', \
                                       command=self.__set_random_word, \
                                       font=self.GUI_FONT, bg=self.BUTTON_COLOR)
    self.__random_word_button.pack()

    #Or label----------------------------------------

    self.__or_label = Label(self.__mid_right_frame4, text='Or', \
                            font=self.GUI_FONT, bg=self.BG_COLOR)
    self.__or_label.pack()

    #Word and category entry boxes, labels, and button

    self.__set_word_label = Label(self.__mid_right_frame5, text='Set word:', \
                                  font=self.GUI_FONT, bg=self.BG_COLOR)
    self.__set_word_label.pack()

    self.__word_label = Label(self.__mid_right_frame6, text='Word', padx=12, \
                              font=self.GUI_FONT, bg=self.BG_COLOR)
    self.__word_label.pack(side='left')

    self.__set_word_entry_box = Entry(self.__mid_right_frame6, width=25)
    self.__set_word_entry_box.pack(side='left')

    self.__category_label = Label(self.__mid_right_frame7, text='Category', \
                                  font=self.GUI_FONT, bg=self.BG_COLOR)
    self.__category_label.pack(side='left')

    self.__set_category_entry_box = Entry(self.__mid_right_frame7, width=25)
    self.__set_category_entry_box.pack(side='left')

    self.__set_word_button = Button(self.__bot_right_frame, text='Set Word', \
                                    command=self.__set_word, font=self.GUI_FONT, \
                                    bg=self.BUTTON_COLOR)
    self.__set_word_button.pack()


    mainloop()
    


 #Event Handlers-------------------------------------------------------------
# Examine the input of the entry box.If input is valid, pass the 
# entry to instance in the Game class to process the information
# then examine if the letter is a correct guess, if it is, makes it
# show up on the canvass, if it isnn't,increment the number of wrong guesses.
# at last, examine if users have used up all guessing chances or have guesses
# all the letters in the word. Delete the input in the entry box at the end.
# coded by Olivia.

  def __guess_letter(self, event):
    
    letter = self.__guess_entry_box.get().lower()

    if not self.__is_valid_letter(letter):

      messagebox.showwarning('Warning!', 'That is not a valid guess!')

    elif self.__word == None:
      
      messagebox.showwarning('Warning!', 'You need to start a game first!')
      
    elif letter in self.__game.get_guess_list():
      
      messagebox.showwarning('Warning!', \
                             'You have already guessed this letter!')
      
    else:

      self.__game.process_guess(letter)

      guess_list = self.__game.get_guess_list()

      self.__guess_list_var.set(guess_list)

      if self.__game.is_correct_guess(letter):
      
        position_list = self.__word.get_letter_position(letter)
        self.__write_correct_guess(position_list, letter)
      
      else:
        
        num_wrong = self.__game.get_num_wrong_guesses()

        if num_wrong == 1:
          self.__draw_head()
        elif num_wrong == 2:
          self.__draw_body()
        elif num_wrong == 3:
          self.__draw_leg1()
        elif num_wrong == 4:
          self.__draw_leg2()
        elif num_wrong == 5:
          self.__draw_arm1()
        elif num_wrong == 6:
          self.__draw_arm2()
      
      if self.__game.is_game_lost():
        
        self.__lose_game()
      
      elif self.__game.is_game_won():
        
        self.__win_game()

    self.__guess_entry_box.delete(0, END)
    return
  
# call back function that's written for multi player mode: set up the word and category 
# that's put by user in the instance of Game class. Display error message if
# the game doesn't have a result yet (win or lose) delete all the input of
# entries at the end.
#collaborative
  def __set_word(self):

    word = self.__set_word_entry_box.get()
    category = self.__set_category_entry_box.get()

    if self.__is_valid_word(word) == False:

      messagebox.showwarning('Warning!', 'That is not a valid word! ' +\
                             'Please be sure your word only contains ' +\
                             'letters and spaces. And is 12 characters ' +\
                             'or less')

    elif self.__game == None:

      self.__word = Word(word, category)

      self.__game = Game()
      
      self.__game.set_correct_letter_list(self.__word.get_letter_list_no_repeats())
    
      self.__category_val.set(category)

      self.__draw_lines()

    else:

      answer = messagebox.askyesno('Warning!', 'You have not finished ' +\
                                      'this game! Are you sure you would ' +\
                                      'like to start a new one?')
      if answer == True:
        self.__reset_game()

        self.__word = Word(word, category)

        self.__game = Game()
        self.__game.set_correct_letter_list(self.__word.get_letter_list_no_repeats())
    
        self.__category_val.set(category)

        self.__draw_lines()
        
    self.__set_word_entry_box.delete(0, END)
    self.__set_category_entry_box.delete(0, END)
    return
# fcall back function that's written for single player mode: pick a random word in the
# pre-made dictionary for the user to guess. Displaying error message if the
# game isn't finished yet.
#coded by Olivia
  def __set_random_word(self):
    if self.__game == None:
      self.__word = Word('', '')
    
      self.__word.set_random_word_and_category()

      self.__game = Game()
      
      self.__game.set_correct_letter_list(self.__word.get_letter_list_no_repeats())

      category = self.__word.get_category()
    
      self.__category_val.set(category)

      self.__draw_lines()

    else:

      answer = messagebox.askyesno('Warning!', 'You have not finished ' +\
                                      'this game! Are you sure you would ' +\
                                      'like to start a new one?')
      if answer == True:
        self.__reset_game()
        
        self.__word = Word('', '')

        self.__game = Game()
    
        self.__word.set_random_word_and_category()
        self.__game.set_correct_letter_list(self.__word.get_letter_list_no_repeats())

        category = self.__word.get_category()
    
        self.__category_val.set(category)

        self.__draw_lines()
        
    return
  
  #Mutators-------------------------------------------------------------------
# Functions that will Draw a body part of the hangman each time 
# the user guesses wrong, the drawing will happen in the Canvass
# Class, coded by Tianhao
  def __draw_lines(self):
    i = 0
    word = self.__word.get_word()
    for letter in word:
      if letter != ' ':
        self.__canvas.create_line((20 + i), 350, (50 + i), 350, width=2.0)
        i += 40
      else:
        i += 40
    return

  def __draw_gallow(self):
    self.__canvas.create_line(140, 280, 330, 280, width=2.0)
    self.__canvas.create_line(235, 280, 235, 50, width=2.0)
    self.__canvas.create_line(235, 50, 330, 50, width=2.0)
    self.__canvas.create_line(330, 50, 330, 100, width=2.0)
    return

  def __draw_head(self):
    self.__canvas.create_oval(310, 100, 350, 140, width=2.0)

  def __draw_body(self):
    self.__canvas.create_line(330, 140, 330, 200, width=2.0)

  def __draw_leg1(self):
    self.__canvas.create_line(330,200,300,230,width=2.0)

  def __draw_leg2(self):
    self.__canvas.create_line(330, 200, 360, 230, width=2.0)

  def __draw_arm1(self):
    self.__canvas.create_line(330,170,300,150, width=2.0)

  def __draw_arm2(self):
    self.__canvas.create_line(330, 170, 360, 150, width=2.0)
    
  def __write_correct_guess(self, position_list,letter):
    for position in position_list:
       coordinates=self.LETTER_INDEX_POSITIONS[position]
       self.__canvas.create_text(coordinates, text=letter, \

                                 font=self.CANVAS_FONT)
  #Display Winning message when the game is won, and reset the game when the
  # user wants to play the game again, coded by Tianhao
  def __win_game(self):
    answer = messagebox.askyesno("Question",\
      "Congratulation! Do you want to try this Game again?")
    if answer==True:
      self.__reset_game()
      
  #Display Losing message
  def __lose_game(self):

    message = 'Sad! You have used up all chances. The correct word was: \n' +\
              self.__word.get_word() + '\n' + \
              "Do you want to try this game again?"
                        
    
    answer = messagebox.askretrycancel("Question", message)
    
    if answer == True:
     
      self.__reset_game()
 # reset the game by clearing instances and values of canvass,
 # Coded by Olivia
  def __reset_game(self):
    self.__game = None
    self.__word = None
    self.__guess_list_var.set('')
    self.__category_val.set('')
    self.__canvas.delete(ALL)
    self.__draw_gallow()
    return

  #Predicates-----------------------------------------------------------------
#Examine if the input is a letter.
#coded by Olivia
  def __is_valid_letter(self, letter):
    return letter.isalpha() and len(letter)==1
  
#Examine if the word set in Multiplayer mode is valid (all made of letters,
# word lenth shouldn't exceed 12) Coded by Olivia
  def __is_valid_word(self, set_word):
    word_list = set_word.split(' ')
    for word in word_list:
      if not word.isalpha():
        return False
    if len(set_word) > 12:
      return False
      
HangmanGUI()

