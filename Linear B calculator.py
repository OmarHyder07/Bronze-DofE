import math
Mycenaen_Numerals = {"I": 1, "_": 10, "O": 100, "Ó": 1000, "Á": 10000, "É": 10000}

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
    line1 = line1 + "É" * math.ceil(e / 2)
    line2 = line2 + "É" * (e // 2)
    a = lbnum.count("Á")
    line1 = line1 + "Á" * math.ceil(a / 2)
    line2 = line2 + "Á" * (a // 2)
    O = lbnum.count("Ó") 
    line1 = line1 + "Ó" * math.ceil(O / 2)
    line2 = line2 + "Ó" * (O // 2)
    o = lbnum.count("O")
    line1 = line1 + "O" * math.ceil(o / 2)
    line2 = line2 + "O" * (o // 2) 
    top = math.ceil(lbnum.count("_") / 2) 
    bot = lbnum.count("_") // 2
    ast = lbnum.count("*")
    ast1 = math.ceil(ast / 2)
    p = ast1 // 2
    line1 = line1 + "=" * p
    if ast1 - (ast //2) == 1:
        line1 = line1 + "_"
    ast2 = ast // 2
    p = ast2 // 2
    line2 = line2 + "=" * p
    i = lbnum.count("I")
    line1 = line1 + "I" * math.ceil(i / 2)
    line2 = line2 + "I" * (i // 2) 
    lst = [line1, line2]
    return lst
    

def linb_to_dernary(linb_number):
    dernary_no = 0
    for letter in str(linb_number):
        if letter in Mycenaen_Numerals:
            dernary_no = dernary_no + Mycenaen_Numerals[letter]
    for x in range(linb_number.count("*")-1):
        dernary_no = dernary_no + 10
    return dernary_no

print("1 = I   5 = IIIII   10 = _   32 = ***_II   100 = O   1,000 = Ó   100,000 = <Ó>") 
number = input("Input Dernary number (up to the hundred thousands) to be translated: ")
split = dernary_split(number)
Linear_B_Number = translate(split)
lb = pretty(Linear_B_Number) 
for l in lb:
    print(l)
    
lbno1 = input("First linear B number: ")
lbno2 = input("Second linear B number: ")
no1 = linb_to_dernary(lbno1)
no2 = linb_to_dernary(lbno2)
op = input("What operator? ")
if op == "+":
    print(str(lbno1), " + ", str(lbno2), " = ", str(no1 + no2))
if op == "-":
    print(str(lbno1), " - ", str(lbno2), " = ", str(no1 - no2))
if op == "/":
    print(str(lbno1), " / ", str(lbno2), " = ", str(no1 / no2))
if op == "*":
    print(str(lbno1), " * ", str(lbno2), " = ", str(no1 * no2))
if op == "%":
    print(str(lbno1), " % ", str(lbno2), " = ", str(no1 % no2))





          
