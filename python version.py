#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random 
from nltk.corpus import wordnet
from nltk.corpus import words
english_words = words.words()
def generate():
    test=True
    while test==True:
        word=random.choice(english_words)
        synsets = wordnet.synsets(word)
        if synsets:
            test=False
            return word
def play(word):
    ch=""
    essay=6
    test=True
    i=0
    hangman=""" 
              |----|
              |
              |
              |
              |
              |
              |__________
            """
    while  essay>0 and  i<len(word) :
        letter=input("give a letter")
        l=letter_test(letter)
        cond=True
        j=0
        while cond==True and l!=word[i]:
            print(condition(essay))
            essay-=1
            print(essay,"chances are lasting")
            l=letter_test(input("the letter is unvalid, give a letter"))
            j=j+1
            
            if l==word[i]:
                cond=False
        if l==word[i]:
            print("the letter is right")
            ch=ch+l
            print(ch)
            i=i+1
    if ch==word:
        print("You Win, the word is",word)
            
    if essay==0:
        print(condition(1))
        print("You Lose,the word is ",word)
def letter_test(x):
    test=False
    if x.isalpha() :
        test=True
        return x
    else:
        while test==False:
            x=input("give a letter")
            if x.isalpha() :
                test=True
    return x
def explane(word):
    synsets = wordnet.synsets(word)
    if synsets:
        return synsets[0].definition()
    else:
        return f"No definition found for the word '{word}'"
    
    
def condition(n):
    if n==6 :
        h=(""" 
              |----|
              |    O
              |
              |
              |
              |
              |__________
            """)
    if n==5:
        h=(""" 
              |----|
              |    O
              |    |
              |    |
              |
              |
              |__________
            """)
    if n==4:
        h=(""" 
              |----|
              |    O
              |   /|
              |    |
              |
              |
              |__________
            """)
    if n==3:
        h=(""" 
              |----|
              |    O
              |   /|\\
              |    |
              |
              |
              |__________
            """)
    if n==2:
        h=(""" 
              |----|
              |    O
              |   /|\\
              |    |
              |   / 
              |
              |__________
            """)
    if n==1:
        h=(""" 
              |----|
              |    O
              |   /|\\
              |    |
              |   / \\
              |
              |__________
            """)
    return h
        
        

    

name=generate()
print(explane(name))
play(name)



# In[ ]:




