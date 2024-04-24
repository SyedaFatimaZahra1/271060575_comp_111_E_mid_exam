import random
print("!!!LUDO GAME!!!")
# tol roll dice 
def roll_dice():
    return random.randint(1, 6)

# to move token
def move_token(cur_pos, dice_roll):
    i, j = cur_pos 
#to move token on board
    j = j + dice_roll
    if j >= 4:  # when j get out of range it gets reset and i chnages from [0] to [1]
        i = i + 1
        j = j % 4
# to not get Indexerror
    if i >= 4:
        i = 3   # sets i and j back to [3]
    if j >= 4:
        j = 3
    return i, j

# making board and other things
board = [[" "," "," "," "],  # making a 2d array used as game_board
         [" "," "," "," "],
         [" "," "," "," "],
         [" "," "," "," "]]
PL1_array = ["1","2","3"]   # separate arrays for both players containing their tokens
PL2_array = ["4","5","6"]
token = ""

player = input("which player are you (e.g 1 / 2): ") # enter 1 or 2
# player 1 conditions
if player == "1": 
    dice_roll = roll_dice()
    if dice_roll == 6:
        token = PL1_array[0] # when dice is 6 token is selected and romoved from array
        del PL1_array[0]
        if len(PL1_array) < 3: # to get the [2] token
            token = PL1_array[1]
            del PL1_array[1]
        elif len(PL1_array) < 2: # to get the [3] token 
            token = PL1_array[2]
            del PL1_array[2]
           
# player 2 conditions            
elif player == "2":
    dice_roll = roll_dice()
    if dice_roll == 6:
        token = PL2_array[0]   #same condition as PL_1 with different names 
        del PL2_array[0]
        if len(PL2_array) < 3:
            token = PL2_array[1]    
            del PL2_array[1]
        elif len(PL2_array) < 2 :
            token = PL2_array[2]
            del PL2_array[2]   

token = "1"
board[0][0] = token
# Initial position of the token
cur_pos = (0, 0) # i=0 and j=0 , token at board[0][0]

# while loop till token reaches board[3][3]
while cur_pos != (3, 3):
# calling function to roll dice
    dice_roll = roll_dice()
    print("Dice Roll:", dice_roll)
# calling the move_token func and putting it inside new variable
    new_pos = move_token(cur_pos, dice_roll)
# removing token from previous position and updating with new 
    board[cur_pos[0]][cur_pos[1]] = " "
    board[new_pos[0]][new_pos[1]] = token

# printing the board again
    for row in board:
        print(row)
# updating the position of the board (new pos becomes current pos)
    cur_pos = new_pos

print("your token has reached the end of the board (^-^)")



print("!!!TREASURE HUNT GAME!!!")
print("Welcome to the treasure hunt game!")
print("There are 12 rooms in grid form:")
rooms = [["1", "2", "3", "4"],  #rooms where keys are treasure are hidden
         ["5", "6", "7", "8"],
         ["9", "10", "11", "12"]]
print(rooms)
print("There is one treasure hunter, two keys, and one treasure.")
print("find the keys and the treasure")
print("REMEMBER ! treasure can only be found after keys")

# to genetrate the first room treasure hunter will be in
current_room = random.choice(range(1, 13))
print("You, the treasure hunter, are currently in room:", current_room)

# counter for below while loop
keys_found = 0
treasure_found = False

# runs when both conditions have not been met 
while not (keys_found == 2 and treasure_found):
# keeps asking again about rooms to visit 
    visit_room = input("Which room number would you like to visit? (e.g., 1 - 12): ")
# wrongs guesses and right guesses   
    if visit_room == "1":
        print("Wrong room.")
    elif visit_room == "2":
        print("You found a key! Find both keys and treasure.")
        keys_found = keys_found + 1 # keys increases by one
    elif visit_room == "3":
        print("Wrong room.")
    elif visit_room == "4":
        print("Wrong room.")
    elif visit_room == "5":
        if keys_found != 2:
            print("wrong room :(")
            treasure_found = False   # when keys not found treasure remains false
        else:    
            print("You found the treasure!")
            treasure_found = True   # treasure becomes True
    elif visit_room == "6":
        print("Wrong room.")
    elif visit_room == "7":
        print("Wrong room.")
    elif visit_room == "8":
        print("Wrong room.")
    elif visit_room == "9":
        print("Wrong room.")
    elif visit_room == "10":
        print("Wrong room.")
    elif visit_room == "11":
        print("You found a key ! find both keys and treasure")
        keys_found = keys_found + 1 # keys increases by one
    elif visit_room == "12":
        print("Wrong room.")
    else:
        print("Invalid input.")
        
print("Congrats!!! You found both keys and the treasure (^-^)")


