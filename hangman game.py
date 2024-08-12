#!/usr/bin/env python
# coding: utf-8

# In[1]:


#the python version that I submitted before is edited in the play() function and there are some modifications to be convinient to th Qt interface
import random
from nltk.corpus import wordnet
from nltk.corpus import words
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox
english_words = words.words()
word = ""  
letter = ""  
essay = 6
guess = ""

def submit():
    global letter
    input = win.addletter.text().strip()
    if len(input) == 1 and input.isalpha():
        letter = input.lower()
        win.addletter.clear()
        win.test.setText("")
    else:
        letter = ""  
        win.test.setText("Please enter a valid single letter")
    return letter

def generate():
    global word, guess, essay
    enable()
    test = False
    while test==False:
        word = random.choice(english_words)
        synsets = wordnet.synsets(word)
        if synsets:
            test = True
    guess= "_" * len(word)
    essay = 6
    reset_game()
    return word 

def reset_game():
    global word, guess, essay
    win.wordedited.setText(guess)
    win.attempts.setText(str(essay))
    win.test.setText("Add a letter")
    win.hangman.setText(condition(essay))
    win.result.setText("")

def play():
    global word, letter, essay, guess
    enable()

    if not word:
        win.test.setText("Please generate a word first")
        return

    submit()

    if not letter:
        return

    if letter in word:
        guess = ''.join([letter if word[i] == letter else guess[i] for i in range(len(word))])
        win.test.setText("The letter is right")
    else:
        essay -= 1
        win.test.setText("The letter is invalid, try again")
    
    win.hangman.setText(condition(essay))
    win.attempts.setText(str(essay))
    win.wordedited.setText(guess)
    
    if "_" not in guess:
        win.result.setText("You Win, the word is " + word)
        endgame()
    elif essay == 0:
        win.result.setText("You Lose, the word was " + word)
        endgame()

def explane():
    global word
    if not word:
        win.indication.setText("Generate a word first!")
        return
    synsets = wordnet.synsets(word)
    if synsets:
        win.indication.setText(str(synsets[0].definition()))
    
def condition(n):
    stages = [
        """ 
          |----|
          |    O
          |   /|\\
          |    |
          |   / \\
          |
          |__________
        """,
        """ 
          |----|
          |    O
          |   /|\\
          |    |
          |   / 
          |
          |__________
        """,
        """ 
          |----|
          |    O
          |   /|\\
          |    |
          |
          |
          |__________
        """,
        """ 
          |----|
          |    O
          |   /|
          |    |
          |
          |
          |__________
        """,
        """ 
          |----|
          |    O
          |    |
          |    |
          |
          |
          |__________
        """,
        """ 
          |----|
          |    O
          |
          |
          |
          |
          |__________
        """,
        """ 
          |----|
          |
          |
          |
          |
          |
          |__________
        """
    ]
    return stages[n]
def endgame():
    disable()
    win.test.setText("Game over. Click 'Generate' to play again.")
def disable():
    win.addletter.setDisabled(True)
    win.play.setDisabled(True)
def enable():
    win.addletter.setDisabled(False)
    win.play.setDisabled(False)

app = QApplication([])
win = loadUi("hangman game.ui")
win.show()
win.generate.clicked.connect(generate)
win.display.clicked.connect(explane)
win.play.clicked.connect(play)

app.exec_()


# In[ ]:





# In[ ]:





# In[ ]:




