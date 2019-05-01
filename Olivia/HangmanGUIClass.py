#HangmanGUI

from tkinter import *

class HangmanGUI:

  def __init__(self):

    self.__win = Tk()

    self.__left_frame = Frame(self.__win)
    self.__left_frame.pack(side='left')

    self.__right_frame = Frame(self.__win)
    self.__right_frame.pack(side='left')

    self.__bot_frame = Frame(self.__win)
    self.__bot_frame.pack()

    self.canvas = Canvas(self.__left_frame, height=400, width=510, \
                         bg='lightblue')
HangmanGUI()
