import math
import sys
Mycenaen_Numerals = {"I": 1, "-": 10, "O": 100, "Ó": 1000, "Á": 10000, "É": 10000}

def dernary_split(number):
    split = [int(x) for x in str(number)]
    split.reverse()
    return split

def translate(s):
    lbnum = ""
    times = len(s)
    if times == 6:
        lbnum = lbnum + "É" * s[5] + " "
    if times >=5:
        lbnum = lbnum + "Á" * s[4] + " "
    if times >= 4:
        lbnum = lbnum + "Ó" * s[3] + " "
    if times >= 3:
            lbnum = lbnum + "O" * s[2] + " "
    if times >= 2:
            tens = "*" * s[1]
            if s[1] > 0:
                tens = tens + "_"
            lbnum = lbnum + tens
    if times >= 1:
        lbnum = lbnum + "I" * s[0]
    return lbnum

def pretty(lbnum):
    line1 = ""
    line2 = ""
    e = lbnum.count("É")
    line1 = line1 + "É" * math.ceil(e / 2) + " "
    line2 = line2 + "É" * (e // 2) + " "
    if line1.count("É") == (line2.count("É") + 1):
        line2 = line2 + " "
    a = lbnum.count("Á")
    line1 = line1 + "Á" * math.ceil(a / 2) + " "
    line2 = line2 + "Á" * (a // 2) + " "
    if line1.count("Á") == (line2.count("Á") + 1):
        line2 = line2 + " "
    O = lbnum.count("Ó") 
    line1 = line1 + "Ó" * math.ceil(O / 2) + " "
    line2 = line2 + "Ó" * (O // 2) + " "
    if line1.count("Ó") == (line2.count("Ó") + 1):
        line2 = line2 + " "
    o = lbnum.count("O")
    line1 = line1 + "O" * math.ceil(o / 2) + " "
    line2 = line2 + "O" * (o // 2) + " "
    if line1.count("O") == (line2.count("O") + 1):
        line2 = line2 + " "
    ast = lbnum.count("*")
    if ast == 1:
        line1 = line1 + "- "
        line2 = line2 + "  "
    elif ast == 2:
        line1 = line1 + "= "
        line2 = line2 + "  " 
    elif ast == 3:
        line1 = line1 + "= "
        line2 = line2 + "- "
    elif ast == 4:
        line1 = line1 + "= "
        line2 = line2 + "= "
    elif ast == 5:
        line1 = line1 + "=- "
        line2 = line2 + "=  "
    elif ast == 6:
        line1 = line1 + "== "
        line2 = line2 + "=  "
    elif ast == 7:
        line1 = line1 + "== "
        line2 = line2 + "=- "
    elif ast == 8:
        line1 = line1 + "== "
        line2 = line2 + "== "
    elif ast == 9:
        line1 = line1 + "==- "
        line2 = line2 + "==  "
    i = lbnum.count("I")
    line1 = line1 + "I" * math.ceil(i / 2) + " "
    line2 = line2 + "I" * (i // 2) + " "
    if line1.count("I") == (line2.count("I") + 1):
        line2 = line2 + " "
    lst = [line1, line2]
    return lst

def linear_b(number):
    if int(number) < 0:
        print("Error. This only works with positive numbers.")
        sys.exit() 
    else:
        split = dernary_split(number)
        Linear_B_Number = translate(split)
        lb = pretty(Linear_B_Number)
        return lb

def calc():
    lbno1 = int(input("First number: "))
    lbno2 = int(input("Second number: "))
    operator = input("What operator? ") 
    lb1 = linear_b(lbno1)  
    lb2 = linear_b(lbno2)
    answer = maths(lbno1, lbno2, operator)
    calculation(lb1, lb2, operator, answer)
    
def maths(no1, no2, operator):
    if operator == "+":
        answer = linear_b(int(no1+no2))
    elif operator == "-":
        answer = linear_b(int(no1-no2))
    elif operator == "/":
        answer = linear_b(int(no1/no2))
    elif operator == "*":
        answer = linear_b(int(no1*no2))
    elif operator == "%":
        answer = linear_b(int(no1%no2)) 
    return answer

def calculation(no1, no2, operator, answer):
    for l in no1:
        print(l)
    print(operator)
    for l in no2:
        print(l)
    print("=")
    for l in answer:
        print(l)
        
print("1 = I   5 = IIIII   10 = _   32 = ***_II   100 = O   1,000 = Ó   100,000 = <Ó>") 
number = input("Input Dernary number (up to the hundred thousands) to be translated: ")
lb = linear_b(number)  
for l in lb:
    print(l)

calc() 
 




          

