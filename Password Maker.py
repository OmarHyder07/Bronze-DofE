import random
import time

p = int(input("How many characters do you want the password to be? "))
print("Answer these questions with Y or N")
z = 0
symbols = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+",
           "{", "[", "}", "]", "|", "\\", ":", ";",
           "'", "<", ",", ">", ".", "?", "/"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
while z == 0:
    if_ch = input("Letters? ")
    if_nu = input("Numbers? ")
    if_sy = input("Symbols? ")
    if if_sy == "Y":
        print("Which symbols should be removed from this list of usable symbols? (SET INPUT = X TO STOP)")
        print(symbols)
        b = 0
        while b == 0: 
            to_remove = input("input: ")
            if to_remove == "X":
                b = 1
            else:
                symbols.remove(to_remove) 
    if if_ch == "N" and if_nu == "N" and if_sy == "N":
        z = 0
    else:
        z = z + 1

d = {"char": 0, "num": 0, "sym": 0}

if if_ch == "N":
    d.pop("char")
if if_nu == "N":
    d.pop("num")
if if_sy == "N":
    d.pop("sym")
    
m = []
for key in d:
    m.append(key)
for x in range(p):
    pick = m[random.randint(0, len(m)-1)]
    d[pick] = d[pick] + 1
        
#random addition of letters, and random capitalisation of such letters. 
word = ""

if "char" in d:
    for x in range(d["char"]):
        y = random.randint(1,2)
        if y == 1:
            word = word + alphabet[random.randint(0, 25)]
        if y == 2:
            word = word + alphabet[random.randint(0, 25)].upper()

#random addition of numbers.
if "num" in d:
    for x in range(d["num"]):
        word = word + str(random.randint(0,9))

#random addition of symbols.

if "sym" in d:
    for x in range(d["sym"]):
        word = word + symbols[random.randint(0, len(symbols)-1)]

#makes password
password = "" 
n_list = list(word)
random.shuffle(n_list)
length = len(n_list) 
for x in range(length):
    password = password + n_list[x] 

print(password) 
