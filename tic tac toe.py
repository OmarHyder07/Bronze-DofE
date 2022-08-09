slots = {"1": {"1": "| ---", "2": " | --- | ", "3": "--- |"},
         "2": {"1": "| ---", "2": " | --- | ", "3": "--- |"},
         "3": {"1": "| ---", "2": " | --- | ", "3": "--- |"}}

def printer(slots):
    li1 = []
    li2 = []
    li3 = []
    for i in slots["1"]:
        li1.append((slots["1"][i]))
    for i in slots["2"]:
        li2.append((slots["2"][i]))
    for i in slots["3"]:
        li3.append((slots["3"][i]))
    print(*li1)
    print(*li2)
    print(*li3)

def changer(slot, user):
    if user == "X":
        slot = slot.replace("---","-X-")
        return slot
    elif user == "O":
        slot = slot.replace("---", "-O-")
        return slot

def checker(slots, user):
    if user in slots["1"]["1"] and user in slots["1"]["2"] and user in slots["1"]["3"]:
        return True
    elif user in slots["2"]["1"] and user in slots["2"]["2"] and user in slots["2"]["3"]:
        return True
    elif user in slots["3"]["1"] and user in slots["3"]["2"] and user in slots["3"]["3"]:
        return True
    elif user in slots["1"]["1"] and user in slots["1"]["2"] and user in slots["1"]["3"]:
        return True
    elif user in slots["1"]["1"] and user in slots["2"]["1"] and user in slots["3"]["1"]:
        return True
    elif user in slots["1"]["2"] and user in slots["2"]["2"] and user in slots["3"]["2"]:
        return True
    elif user in slots["1"]["3"] and user in slots["2"]["3"] and user in slots["3"]["3"]:
        return True
    elif user in slots["1"]["1"] and user in slots["2"]["2"] and user in slots["3"]["3"]:
        return True
    elif user in slots["1"]["3"] and user in slots["2"]["2"] and user in slots["3"]["1"]:
        return True
    else:
        return False
    
win_condition = False

user = input("X or O first? ")
if user == "X":
    x = 1
    o = 0
else:
    x = 0
    o = 1

while win_condition == False:
    printer(slots)
    valid = False
    while valid == False:
        row = input("which row? ")
        column = input("which column? ")
        if "O" in slots[row][column] or "X" in slots[row][column]:
            valid = False
            print("This slot has already been chosen.")
        else:
            valid = True
    if x == 1:
        slot = changer(slots[row][column], "X")
        slots[row][column] = slot
        win_condition = checker(slots, "X") 
    if o == 1:
        slot = changer(slots[row][column], "O")
        slots[row][column] = slot
        win_condition = checker(slots, "O") 
    if x == 1:
        x = 0
        o = 1
    else:
        x = 1
        o = 0
printer(slots)
if x == 0:
    print("Player X has won the game!")
else:
    print("Player O has won the game!") 

