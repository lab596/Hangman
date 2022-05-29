from tkinter import *

root = Tk()
root.geometry("500x500")
intro = Label(root,text="Hangman")
rules = Label(root,text="Simply try to guess the sentence or the word!")
intro.grid(row=0,column=4)
rules.grid(row=1, column=4)
def wordClick():
  wordr = Label(root,text="Welcome to word mode.\nYour goal is to guess the word within 6 guesses.")
  wordr.grid(row=3,column=4)
def senClick():
  wordr = Label(root,text="Welcome to sentance mode.\nYour goal is to guess the word within 3 guesses.")
  wordr.grid(row=3,column=4)
word = Button(root,text="Word Mode",command=wordClick)
sen=Button(root,text="Sentence Mode",command=senClick)
word.grid(row=2,column=3)
sen.grid(row=2,column=5)
root.mainloop()
