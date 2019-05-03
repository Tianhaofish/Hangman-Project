#HangmanGUI

from tkinter import *
from tkinter import messagebox
from WordClass import *
from HangmanLogicClass import *

class HangmanGUI:

  #Class Constants------------------------------------------------------------

  CANVAS_FONT = ('Calibri', 20)
  GUI_FONT = ('Calibri', 12)
  BG_COLOR = 'seashell3'
  BUTTON_COLOR = 'light steel blue'
  LETTER_INDEX_POSITIONS = {}

  #Constructor----------------------------------------------------------------
  
  def __init__(self):

    self.__game = None
    self.__word = None

    self.__win = Tk()

    #Main frames-------------------------------------

    self.__left_frame = Frame(self.__win)
    self.__left_frame.pack(side='left')

    self.__right_frame = Frame(self.__win, bg=self.BG_COLOR)
    self.__right_frame.pack(side='left')

    self.__bot_frame = Frame(self.__win, bg=self.BG_COLOR)
    self.__bot_frame.pack()

    #Canvas------------------------------------------

    self.__canvas = Canvas(self.__left_frame, height=400, width=510, \
                           bg='rosybrown2', highlightbackground='black')
    self.__canvas.pack()

    #Draw gallow-------------------------------------

    self.__canvas.create_line(140, 280, 330, 280, width=2.0)
    self.__canvas.create_line(235, 280, 235, 50, width=2.0)
    self.__canvas.create_line(235, 50, 330, 50, width=2.0)
    self.__canvas.create_line(330, 50, 330, 100, width=2.0)

    #frames within right frame-----------------------

    self.__top_right_frame = Frame(self.__right_frame, padx=5, pady=10, \
                                   bg=self.BG_COLOR)
    self.__top_right_frame.pack()

    self.__mid_right_frame1 = Frame(self.__right_frame, padx=5, \
                                    bg=self.BG_COLOR)
    self.__mid_right_frame1.pack()

    self.__mid_right_frame2 = Frame(self.__right_frame, padx=5, \
                                    bg=self.BG_COLOR)
    self.__mid_right_frame2.pack()

    self.__mid_right_frame3 = Frame(self.__right_frame, padx=5, \
                                    bg=self.BG_COLOR)
    self.__mid_right_frame3.pack()

    self.__mid_right_frame4 = Frame(self.__right_frame, padx=5, \
                                    bg=self.BG_COLOR)
    self.__mid_right_frame4.pack()

    self.__mid_right_frame5 = Frame(self.__right_frame, padx=5, pady=10, \
                                    bg=self.BG_COLOR)
    self.__mid_right_frame5.pack()

    self.__bot_right_frame = Frame(self.__right_frame, padx=5, \
                                   bg=self.BG_COLOR)
    self.__bot_right_frame.pack()

    #Category display--------------------------------

    self.__category_label = Label(self.__top_right_frame, text='Category: ', \
                                  font=self.GUI_FONT, bg=self.BG_COLOR)
    self.__category_label.pack(side='left')

    self.__category_val = StringVar()
    self.__category_val.set('')

    self.__category_val_label = Label(self.__top_right_frame, \
                                      textvariable = self.__category_val, \
                                      font=self.GUI_FONT, bg=self.BG_COLOR)
    self.__category_val_label.pack(side='left')

    #Word and category entry boxes, labels, and button

    self.__set_word_label = Label(self.__mid_right_frame1, text='Set word:', \
                                  font=self.GUI_FONT, bg=self.BG_COLOR)
    self.__set_word_label.pack()

    self.__word_label = Label(self.__mid_right_frame2, text='Word', padx=12, \
                              font=self.GUI_FONT, bg=self.BG_COLOR)
    self.__word_label.pack(side='left')

    self.__set_word_entry_box = Entry(self.__mid_right_frame2, width=25)
    self.__set_word_entry_box.pack(side='left')

    self.__category_label = Label(self.__mid_right_frame3, text='Category', \
                                  font=self.GUI_FONT, bg=self.BG_COLOR)
    self.__category_label.pack(side='left')

    self.__set_category_entry_box = Entry(self.__mid_right_frame3, width=25)
    self.__set_category_entry_box.pack(side='left')

    self.__set_word_button = Button(self.__mid_right_frame4, text='Set Word', \
                                    command=self.__set_word, font=self.GUI_FONT, \
                                    bg=self.BUTTON_COLOR)
    self.__set_word_button.pack()

    #Pick random word button-------------------------

    self.__random_word_button = Button(self.__mid_right_frame5, \
                                       text='Pick Random Word', \
                                       command=self.__set_random_word, \
                                       font=self.GUI_FONT, bg=self.BUTTON_COLOR)
    self.__random_word_button.pack()

    mainloop()
    


  #Event Handlers-------------------------------------------------------------

  def __guess_letter(self):
    return

  def __set_word(self):
    if self.__game == None:
      word = self.__set_word_entry_box.get()
      category = self.__set_category_entry_box.get()

      self.__word = Word(word, category)

      self.__game = Game()
      
      self.__game.set_correct_letter_list(\
        self.__word.get_letter_list_no_repeats())

      category = self.__word.get_category()
    
      self.__category_val.set(category)

      self.__draw_lines()

    else:

      answer = messagebox.askyesno('Warning!', 'You have not finished ' +\
                                      'this game! Are you sure you would ' +\
                                      'like to start a new one?')
      if answer == True:
        word = self.__set_word_entry_box.get()
        category = self.__set_category_entry_box.get()

        self.__word = Word(word, category)

        self.__game = Game()
        self.__game.set_correct_letter_list(\
          self.__word.get_letter_list_no_repeats())

        category = self.__word.get_category()
    
        self.__category_val.set(category)

        self.__draw_lines()
        
    self.__set_word_entry_box.delete(0, END)
    self.__set_category_entry_box.delete(0, END)
    return

  def __set_random_word(self):
    if self.__game == None:
      self.__word = Word('', '')
    
      self.__word.set_random_word_and_category()

      self.__game = Game()
      
      self.__game.set_correct_letter_list(\
        self.__word.get_letter_list_no_repeats())

      category = self.__word.get_category()
    
      self.__category_val.set(category)

      self.__draw_lines()

    else:

      answer = messagebox.askyesno('Warning!', 'You have not finished ' +\
                                      'this game! Are you sure you would ' +\
                                      'like to start a new one?')
      if answer == True:
        self.__word = Word('', '')

        self.__game = Game()
    
        self.__word.set_random_word_and_category()
        self.__game.set_correct_letter_list(\
          self.__word.get_letter_list_no_repeats())

        category = self.__word.get_category()
    
        self.__category_val.set(category)

        self.__draw_lines()
        
    return

  def __reset_game(self):
    return
  
  #Mutators-------------------------------------------------------------------

  def __draw_lines(self):
    i = 0
    for letter in self.__word.get_word():
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
'''
  def __draw_head(self):

  def __draw_body(self):

  def __draw_leg1(self):

  def __draw_leg2(self):

  def __draw_arm1(self):

  def __draw_arm2(self):

  def __write_correct_guess(self, guess):

  def __win_game(self):

  def __lose_game(self):
'''
  #Predicates-----------------------------------------------------------------
      

HangmanGUI()
