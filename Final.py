import textwrap
import sys
import os
import time
import random
screen_width = 100

# To see the maze, visit

os.startfile("MapWGrid.png")

def readOut(speechVar):
    for character in speechVar:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)


# https://savagelegend.com/misc-resources/classic-riddles-1-100/
# https://riddlesdb.com/hard/
riddle_Q = [
    "I am greater than God and more evil than the devil. The poor have me, the rich need me and if you eat me you’ll die. What am I?",
    "I walks on four legs in the morning, two legs at noon and three legs in the evening. What am I?",
    "I am the beginning of the end, and the end of time and space. I am essential to creation, and I surround every place. What am I?",
    "What always runs but never walks, often murmurs, never talks, has a bed but never sleeps, has a mouth but never eats?",
    "I never was, am always to be. No one ever saw me, nor ever will. And yet I am the confidence of all, To live and breath on this terrestrial ball. What am I?",
    "At night they come without being fetched. By day they are lost without being stolen. What are they?",
    "What is in seasons, seconds, centuries and minutes but not in decades, years or days?",
    "The one who makes it, sells it. The one who buys it, never uses it. The one that uses it never knows that he’s using it. What is it?",
    "What’s black when you get it, red when you use it, and white when you’re all through with it?",
    "You throw away the outside and cook the inside. Then you eat the outside and throw away the inside. What did you eat?",
    "I am always hungry, I must always be fed, The finger I touch, Will soon turn red. What am I?",
    "Ripped from my mother’s womb, Beaten and burned, I become a blood thirsty killer. What am I?",
    "When young, I am sweet in the sun. When middle-aged, I make you happy. When old, I am valued more than ever. What am I?",
    "I am all about, but cannot be seen, can be captured, cannot be held, no throat, but can be heard. What am I?",
    "Until I am measured I am not known. Yet how you miss me when I have flown. What am I?",
    "Glittering points that downward thrust, Sparkling spears that never rust. What am I?",
    "You heard me before, yet you hear me again, Then I die, ’till you call me again. What am I?",
    "Three lives have I. Gentle enough to soothe the skin,Light enough to caress the sky, Hard enough to crack rocks. What am I?",
    "It cannot be seen, it weighs nothing, but when put into a barrel, it makes it lighter. What is it?",
    "You saw me where I never was and where I could not be. And yet within that very place, my face you often see. What am I?",
    "Say my name and I disappear. What am I?",
    "What is it that after you take away the whole, some still remains?",
    "A box without hinges, lock or key, yet golden treasure lies within. What is it?",
    "Forward I’m heavy, but backwards I’m not. What am I?",
    "Soft and fragile is my skin, I get my growth in mud. I’m dangerous as much as pretty, for if not careful, I draw blood.",
    "I live in water. If you cut my head I’m at your door, If you cut my tail I’m fruit, If you cut both I’m with you What am I?",
    "The more of me you take, the more you leave behind. What am I?",
    "Alive without breath, As cold as death, Clad in mail never clinking, Never thirsty, ever drinking. What am I?",
    "Die without me, Never thank me. Walk right through me, never feel me. Always watching, never speaking. Always lurking, never seen.",
    "I am a seven letter word containing thousands of letters. What am I?",
    "I start and end with the letter E, yet I only have one letter, what am I?",
    "My first two letters signify a male, the first three letters a female, the first four a great man, and all of me represents a great woman, what am I?"
    ]

riddle_A = ["Nothing", "Man", "E", "A River", "Tomorrow Future", "The Stars", "N", "A Coffin", "Charcoal", "Corn", "Fire", "Iron", "Wine", "Wind", "Time", "Icicle", "Echo", "Water", "Barrel", "Reflection", "Silence", "Wholesome", "Egg", "Ton", "Thorn", "Pearl", "Footsteps", "Fish", "Air", "Mailbox", "Envelope", "Heroine"]

abc_list = list("ABCDEFGHIJKLMNO")

moveset_A = ["UR", "RD", "UR", "URD", "RD", "UR", "UD", "RD", "UR", "UD", "URD", "UD", "RD", "U", "RD"]
moveset_B = ["RL", "UL", "DL", "RL", "L", "UL", "RD", "UL", "DL", "R", "RL", "R", "RL", "UR", "RDL", ]
moveset_C = ["RL", "U", "RD", "UL", "RD", "D", "UL", "RD", "UR", "DL", "RL", "RL", "RL", "RL", "RL", "RL", ]
moveset_D = ["URL", "UD", "UDL", "D", "URL", "UD", "UD", "RDL", "RL", "UR", "DL", "RL", "UL", "DL", "RL",]
moveset_E = ["L", "UR", "UD", "RD", "RL", "UR", "URD", "UD", "LD", "RL", "UR", "ULD", "URD", "D", "RL"]
moveset_F = ["UR", "DL", "UR", "DL", "UL", "DL", "L", "UR", "UD", "DL", "L", "UR", "RDL", "UR", "DL" ]
moveset_G = ["RL", "R", "RL", "UR", "UDL", "UD", "UD", "LD", "U", "U", "URD", "RDL", "L", "UL", "RD" ]
moveset_H = ["L", "RL", "RL", "L", "UL", "UD", "RD", "UR", "UD", "UD", "LD", "RL", "UR", "UD", "UL"]
moveset_I = ["U", "RDL", "RL", "UR", "UD", "RD", "RL", "URL", "RD", "UR", "RD", "RL", "UL", "RD", "R" ]
moveset_J = ["UR", "LD", "RL", "RL", "R", "RL", "RL", "L", "RL", "L", "URL", "LD", "UR", "DL", "RL"]
moveset_K = ["URL", "UD", "LD", "RL", "URL", "LD", "UL", "RD", "UL", "RD", "L", "UR", "LD", "UR", "LD"]
moveset_L = ["RL", "UR", "UR", "RD", "UL", "UD", "UD", "LD", "UR", "LD", "UR", "LD", "U", "ULD", "RD" ]
moveset_M = ["UL", "LD", "UR", "UD", "RD", "UR", "URD", "RD", "URL", "UD", "DL", "U", "UDR", "RD", "RL" ]
moveset_N = ["UR", "D", "UL", "RD", "RL", "RL", "RL", "L", "UL", "UD", "UD", "UD", "LD", "UL", "RLD" ]
moveset_O = ["UL", "UD", "UD", "LD", "UL", "LD", "UL", "UD", "UD", "UD", "UD", "UD", "UD", "UD", "LD" ]
move_set = [moveset_A, moveset_B, moveset_C,
            moveset_D, moveset_E, moveset_F, moveset_G, moveset_H, moveset_I, moveset_J, moveset_K, moveset_L, moveset_M, moveset_N, moveset_O, ]

readOut("Hello, welcome to the haunted time maze!\nIn this game, you will be given a certain amount of time to complete the maze.\nEach move will deduct from your remaining time.\nAt random points along the maze, you will be presented with riddles.\nIf you answer a riddle incorrectly, some time will be deducted.\nIf you do not complete the maze in time, it is game over.\nIf you wish to solve the puzzle in the least number of moves, it will take 68 moves!\nGood Luck!\n")
def rand_gen():
    return int(random.randint(1,6))

time_rem = 200
unsolved = True
current_pos_let = "H"
current_pos_num = "1"
def maze():
    global current_pos_let
    global current_pos_num
    global time_rem
    while unsolved:
        readOut("You have " + str(time_rem) + " months remaining.\n")
        readOut("Your current position is " + current_pos_let + current_pos_num+"\n")
        avail_moves = move_set[abc_list.index(current_pos_let)][int(current_pos_num)-1]
        readOut("Where would you like to go?\nYou can move: " + str(avail_moves)+"\n")
        move_inp = input("Enter U, R, D, or L.\n")
        while move_inp not in list(avail_moves):
            readOut("\nSorry, you cannot move there.\n")
            move_inp = input("Enter U, R, D, or L.\n")
        if move_inp == "L":
            current_pos_let = abc_list[abc_list.index(current_pos_let)-1] 
        if move_inp == "R":
            current_pos_let = abc_list[abc_list.index(current_pos_let)+1]
        if move_inp == "U":
            current_pos_num = str(int(current_pos_num) + 1)
        if move_inp == "D":
            current_pos_num = str(int(current_pos_num) - 1)
        time_rem = time_rem - random.randint(1,4)
        if rand_gen() == 4:
            readOut("Oh you've come across the cosmic riddler. He asks you:\n")
            rand_Rid = random.randint(1, len(riddle_A))
            readOut(riddle_Q[rand_Rid])
            rid_inp = input("")
            if rid_inp.upper() in riddle_A[rand_Rid].upper() or riddle_A[rand_Rid].upper() in rid_inp.upper():
                readOut("You are correct, the fates ares are on your side.\n")
                riddle_A.pop(rand_Rid)
                riddle_Q.pop(rand_Rid)
            else:
                readOut("You have been bested, and for your blunder you will suffer.\n")
                time_taken = random.randint(2, 7)
                time_rem = time_rem - time_taken
                readOut(str(time_taken) + " months have been taken away from your journey.\n")
                riddle_A.pop(rand_Rid)
                riddle_Q.pop(rand_Rid)
                
    
maze()
