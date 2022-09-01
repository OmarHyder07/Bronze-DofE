alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", \
            "v", "w", "x", "y", "z", " ", ",", "."] 

def split(word): #function to split string into each different character
    return [char for char in word]
     
word = input("please type in a phrase! ")
characters = split(word)

def char_freq(freq):
    x = 0
    y = 29
    while y >0:
        if alphabet[x] in freq :
            count = freq.count(alphabet[x])
            print(alphabet[x]+": "+str(count))
        y = y - 1
        x = x + 1
        
freq = char_freq(characters)
