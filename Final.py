import textwrap
import sys
import os
import time
import random
screen_width = 100

# To see the maze, visit https://drive.google.com/file/d/1K98vkqbeeqJedcoV2yes1Tpy59kTOxO3/view?usp=sharing

# os.startfile("MapWGrid.png")

def readOut(speechVar):
    for character in speechVar:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)


# https://savagelegend.com/misc-resources/classic-riddles-1-100/
# https://riddlesdb.com/hard/
# https://www.riddles.com/what-am-i-riddles
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
    "My first two letters signify a male, the first three letters a female, the first four a great man, and all of me represents a great woman, what am I?",
    "With no wings, I fly. With no eyes, I see. With no arms, I climb. More frightening than any beast, stronger than any foe. I am cunning, ruthless, and tall; in the end, I rule all. What am I?",
    "The higher I climb, the hotter I engage, I can not escape my crystal cage. What am I?",
    "Double my number, I'm less than a score, half of my number is less than four. Add one to my double when bakers are near, days of the week are still greater, I fear. What am I?",
    "Large as a mountain, small as a pea, Endlessly swimming in a waterless sea. What am I?",
    "A dagger thrust at my own heart, Dictates the way I'm swayed. Left I stand, and right I yield, To the twisting of the blade. What am I?",
    "Weight in my belly, Trees on my back, Nails in my ribs, Feet I do lack. What am I?"
    ]

riddle_A = ["Nothing", "Man", "E", "River", "Tomorrow Future", "The Stars", "N", "A Coffin", "Charcoal", "Corn", "Fire", "Iron", "Wine", "Wind", "Time", "Icicle", "Echo", "Water", "Barrel", "Reflection", "Silence", "Wholesome", "Egg", "Ton", "Thorn", "Pearl", "Footsteps", "Fish", "Air", "Mailbox", "Envelope", "Heroine", "Imagination", "Mercury", "Six 6", "Asteroid", "Lock", "Ship Boat"]

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

# readOut("Hello, welcome to the haunted time maze!\nIn this game, you will be given a certain amount of time to complete the maze.\nEach move will deduct from your remaining time.\nAt random points along the maze, you will be presented with riddles.\nIf you answer a riddle incorrectly, some time will be deducted.\nIf you do not complete the maze in time, it is game over.\nIf you wish to solve the puzzle in the least number of moves, it will take 68 moves!\nGood Luck!\n")
def rand_gen():
    return int(random.randint(1,6))
time_rem = 0
def start_screen():
    global time_rem
    readOut("Hello, what is your name?")
    name = input("")
    readOut("Hello "+ name + ", welcome to the haunted time maze!\nIn this game, you will be given a certain amount of time to complete the maze.\nEach move will deduct from your remaining time.\nAt random points along the maze, you will be presented with riddles.\nIf you answer a riddle incorrectly, some time will be deducted.\nIf you do not complete the maze in time, it is game over.\nIf you wish to solve the puzzle in the least number of moves, it will take 68 moves!\nGood Luck!\n")
    readOut("What difficulty level would you like to experience?\nEasy, Medium or Hard?")
    diff = input("Enter a difficulty. ")
    if diff.upper() == "EASY":
        time_rem = 250
    elif diff.upper() == "MEDIUM":
        time_rem = 200
    elif diff.upper() == "HARD":
        time_rem = 120
start_screen()

unsolved = True
current_pos_let = "H"
current_pos_num = "1"
def maze():
    global time_rem
    global current_pos_let
    global current_pos_num
    global unsolved
    while unsolved:
        readOut("You have " + str(time_rem) + " months remaining.\n")
        readOut("Your current position is " + current_pos_let + current_pos_num+"\n")
        avail_moves = move_set[abc_list.index(current_pos_let)][int(current_pos_num)-1]
        if avail_moves == "L":
            avail_words = "Left"
        if avail_moves == "D":
            avail_words = "Down"
        if avail_moves == "DL":
            avail_words = "Down or Left"
        if avail_moves == "RL":
            avail_words = "Right or Left"
        if avail_moves == "RD":
            avail_words = "Right or Down"
        if avail_moves == "RDL":
            avail_words = "Right, Left, or Down"
        if avail_moves == "U":
            avail_words = "Up"
        if avail_moves == "UL":
            avail_words = "Up or Left"
        if avail_moves == "UD":
            avail_words = "Up or Down"
        if avail_moves == "UDL":
            avail_words = "Up, Down, or Left"
        if avail_moves == "UR":
            avail_words = "Up or Right"
        if avail_moves == "URL":
            avail_words = "Up, Right, or Left"
        if avail_moves == "URD":
            avail_words = "Up, Right, or Down"
        readOut("Where would you like to go?\nYou can move: " + avail_words +"\n")
        move_inp = input("Enter a move choice.\n")
        if move_inp.upper() == "LEFT" or move_inp.upper() == "RIGHT" or move_inp.upper() == "UP" or move_inp.upper() == "DOWN":
            move_inp = move_inp[:1].upper()
        if move_inp.upper() == "EXIT":
            exit()
        while move_inp not in list(avail_moves):
            readOut("Sorry, you cannot move there.\n")
            move_inp = input("You can move: " + avail_words + "\n")
            if move_inp.upper() == "LEFT" or move_inp.upper() == "RIGHT" or move_inp.upper() == "UP" or move_inp.upper() == "DOWN":
                move_inp = move_inp[:1].upper()
        if current_pos_let == "H" and current_pos_num == "15":
            if move_inp == "U":
                readOut("You have won the game!")
                unsolved = False
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
    
