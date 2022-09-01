import random
from random import shuffle

colours = ["orange", "blue", "red", "pink", "purple"]

col_pick = random.randint(0, 4) #randomly decides which word to use
c_ana = colours[col_pick] #assignes that word to a new variable

def shuffle_word(word):
       word = list(word)
       shuffle(word)
       return ''.join(word)

anagram = shuffle_word(c_ana) 

print("Colour anagram: guess the word!")
print(anagram)
guess = ""

while guess != c_ana:
    guess = input("What is the word? ")
    if guess == c_ana:
        print("Correct!")
    else:
        print("Wrong") 
