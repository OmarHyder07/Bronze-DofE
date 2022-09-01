nato_alphabet = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf',\
                 'H':'Hotel', 'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November',\
                 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo',\
                 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor',\
                 'W':'Whiskey', 'X':'X-ray', 'Y':'Yankee', 'Z':'Zulu'}

name = input("what is your last name (please type this in FULL CAPS!)? ")
n_of_letters = len(name)
letter = 0

surname = []

# putting each letter in name in an array
while n_of_letters > 0:
    array_addition = name[letter]
    letter = letter +1
    n_of_letters = n_of_letters - 1
    surname.append(array_addition)
    #print(surname[letter-1])

n_to_get = len(surname)

nato_finder = 0
printed_name = ""
x = 0

while x < n_to_get:
    nletter_to_get = nato_alphabet[surname[x]]
    #print(nletter_to_get)
    #nato_finder = nato_finder - 1
    x = x + 1
    printed_name = printed_name + " " + nletter_to_get
   # print(str(x) + " " + printed_name)

#print(printed_name)

#print("####################################")


printed_name = ""
for x in name:
    nletter_to_get = nato_alphabet[x]
    printed_name = printed_name + " " + nletter_to_get
   # print(str(x) + " " + printed_name)


print(printed_name)    
