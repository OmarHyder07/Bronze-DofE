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

print("1 = I   5 = IIIII   10 = _   32 = ***_II   100 = O   1,000 = Ó   100,000 = <Ó>") 
number = input("Input Dernary number (up to the hundred thousands) to be translated: ")
split = dernary_split(number)
Linear_B_Number = translate(split)
print(Linear_B_Number) 
