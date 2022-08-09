import random
from time import sleep

playing = True
while playing == True:
    ships = [[2, 8], [3, 7], [3, 7], [4, 6], [5, 5]] #[length of ship, number of valid options ship has in positions list (-1 for index)]
    positions = [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9],
                 [6, 7, 8, 9], [7, 8, 9], [8,9]] #the valid positions a ship can be placed on, the numbers are index for the values in the board lists
    board_horiz = {}
    board_vert = {}

    for x in range(int(10)):
        board_horiz[x+1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # dictionary: key = row, value = 10 column positions 
        board_vert[x+1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # dictionary: key = column, value = 10 row positions

    def placer(board, o_board, ship): #places the ships randomly 
        obstructed = True 
        while obstructed == True: #this is to check wether or not the ships are going to overlap
            test = [] 
            o_test = []
            rpos = positions[random.randint(0, ship[1])] 
            rkey = random.randint(1,10) 
            for x in range(ship[0]):
                test.append(board[rkey][rpos[x]]) #this creates a list of the spots going to be placed on within the list of the ships orientation (horiz or vert)
                o_test.append(o_board[rpos[x]+1][rkey-1]) #this does the same, but for the other orientation's list, to make sure there are no unseen clashes.
            if "1" in test or "1" in o_test: #the "1" means a ship. 
                obstructed = True
            else:
                obstructed = False
        for x in range(ship[0]):
                board[rkey][rpos[x]] = "1" #this replaces all of the "0"s in the list with "1"s to indicate a ship's placement 
        return board

    for x in range(len(ships)):
        if random.randint(1,2) == 1: #randomly decides if a ship should be verticle or horizontal 
            board_vert = placer(board_vert, board_horiz, ships[x])
        else:
            board_horiz = placer(board_horiz, board_vert, ships[x])

    ############################
     
    board = []
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I","J"]
    score = 100

    for x in range(10):
        board.append([letters[x]] + ["O"] * 10)

    def print_board(board): #prints the board 
        print("  0 1 2 3 4 5 6 7 8 9") 
        for row in board:
            print((" ").join(row))

    def validator(guess): #checks if a guess is valid
        holder = []
        for char in guess:
            holder.append(char) 
        if len(holder) == 2 and guess[0].isalpha() == True and guess[0] in letters and guess[1].isdigit() == True and 0 <= int(guess[1]) < 10:
            row = letters.index(guess[0]) #translates the letter to an indexable
            if board[row][int(guess[1]) + 1] == "O": 
                return True
            else:
                print("You've already guessed this slot!")
                return False 
        else:
            print("Invalid Input")
            return False 
        

    def checker(guess, score): #checks if the guess hits a ship
        row = letters.index(guess[0]) #translates the letter to an indexable
        if board_horiz[row+1][int(guess[1])] == "1" or board_vert[int(guess[1]) + 1][row] == "1": #horiz's key is the row (i made keys 1-10 even though the values are 0-9), it's value is the column) 
            board_changer(row, int(guess[1]) + 1, "X")
            print("You hit a ship!") 
        else:
            board_changer(row, int(guess[1]) + 1, "*")
            print("You missed the ships.") 
            score = score - 1
        

    def board_changer(row, column, symbol): #adds guesses and hits to the board, parameters: position and symbol to add (wether it's a hit or miss) 
        board[row][column] = symbol

    def win_checker(board): #checks if you have won the game yet
        XCount = 0
        for li in board:
            for letters in li:
                XCount += letters.count("X")
        if XCount == 17:
            return True
        else:
            return False

    print("Let's play Battleships!")
    print("Inputs: letter + number. e.g. B3") 
    win_condition = False

    while win_condition == False:
        print_board(board)
        sleep(0.5)
        v = False
        while v == False:
            guess = input("Input which slot you will fire a missile at: ")
            v = validator(guess)
        checker(guess, score)
        sleep(0.5)
        win_condition = win_checker(board)
         
    print_board(board)
    print("Well done! You won!")
    sleep(0.5)
    print("Your score is " + str(score) + ".")
    sleep(1)
    again = input("Would you like to play again? Y/N ")
    if again == "N":
        playing == False 
