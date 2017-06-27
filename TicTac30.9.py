""""By default, implement a 2 player version, where players can take moves after each other
using the numerical keyboard. As an extra feature, you can implement an AI who you can help
with and some more interactive control."""

import random
import time

board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #3x3 board for the game
ingame = 1 # 1=game runs or 0=game stops
win = () #who wins the game? x or o? or draw?

P1wins = 0 #P1 score count
P2wins = 0 #P2 score count
draws = 0 #Draw count

gamerounds = 0 #all game rounds
rounds = 0 #turn num in a game
firstplayer = 0 #which player is first 1 or 2

def newGame(): #new game. resets a lot of things
    global board
    global rounds
    global gamerounds
    global rounds
    global ingame
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    gamerounds += 1
    rounds = 1
    ingame = 1
    whichPlayerfirst()
    show()

def whichPlayerfirst():
    global firstplayer
    firstplayer = random.randint(1,2)

def endGame(): #end game. add score count
    global P1wins
    global P2wins
    global draws
    if win == "x":
        P1wins += 1
    elif win == "o":
        P2wins += 1
    elif win == "draw":
        draws += 1
    winMessage()

def resetScores(): #reset scores
    global P1wins
    global P2wins
    global draws
    global gamerounds
    global rounds
    global board
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    gamerounds = 0
    rounds =  0
    P1wins = 0
    P2wins = 0
    draws = 0
    print(" Resetting scores, please wait...")
    time.sleep(2)

def winMessage():
    if win == "x":
        print("\033[1;31m","Player1 wins!!!","\033[0m")
        time.sleep(2)
    elif win == "o":
        print("\033[1;32m","Player2 wins!!!","\033[0m")
        time.sleep(2)
    elif win == "draw":
        print(" It's a draw!!!")
        time.sleep(2)

def checkLine(char, spot1, spot2, spot3): #checks if 3 index of list is equal
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True

def checkWin(char): #checks each row for win, or draw at round number 9
    global ingame
    global win
    if checkLine(char, 1, 2, 3):
        win = char
        ingame = 0
    elif checkLine(char, 4, 5, 6):
        win = char
        ingame = 0
    elif checkLine(char, 7, 8, 9):
        win = char
        ingame = 0
    elif checkLine(char, 1, 4, 7):
        win = char
        ingame = 0
    elif checkLine(char, 2, 5, 8):
        win = char
        ingame = 0
    elif checkLine(char, 3, 6, 9):
        win = char
        ingame = 0
    elif checkLine(char, 1, 5, 9):
        win = char
        ingame = 0
    elif checkLine(char, 3, 5, 7):
        win = char
        ingame = 0
    elif rounds == 10:
        win = "draw"
        ingame = 0

def checkWinAI(char): #checks each row for win option for AI
    if checkLine(char, 1, 2, 3):
        return True
    elif checkLine(char, 4, 5, 6):
        return True
    elif checkLine(char, 7, 8, 9):
        return True
    elif checkLine(char, 1, 4, 7):
        return True
    elif checkLine(char, 2, 5, 8):
        return True
    elif checkLine(char, 3, 6, 9):
        return True
    elif checkLine(char, 1, 5, 9):
        return True
    elif checkLine(char, 3, 5, 7):
        return True


def playerInput(): #keyoard input only from 1-9
    while True:
            try:
                x = int(input(" Select a spot: "))
                if x in range(1,10):
                    return x
                    break
                else:
                    print(" Please use numbers only between 1-9!")
                    continue
            except ValueError:
                print(" Please use the number keys, from 1-9!")
                continue

def p1Turn(): #P1 input, checks if the spot is taken
    print("\033[1;31m","Player1 turn!","\033[0m")
    newspot = playerInput()
    if board[newspot] != "x" and board[newspot] != "o":
        board[newspot] = "x"
    else:
        print (" You can't put your 'x' there, it is already taken!")
        p1Turn()

def p2Turn(): #P2 input, checks if the spot is taken
    print("\033[1;32m","Player2 turn!","\033[0m")
    newspot = playerInput()
    if board[newspot] != "x" and board[newspot] != "o":
        board[newspot] = "o"
    else:
        print (" You can't put your 'o' there, it is already taken!")
        p2Turn()

def AIturn(): # Player against AI
    AI = random.randint (1,9)
    if board[AI] != "x" and board[AI] != "o":
        board[AI] = "o"
    else:
        AIturn()

def AIturnHARD(): # Player against AI HARD MODE
    AI = random.randint (1,9)
    for i in range(1,10):
        if board[i] == " ":
            board[i] = "o"
            if checkWinAI("o") == True:
                board[i] = "o"
                return
            else:
                board[i] = " "
    for i in range(1,10):
        if board[i] == " ":
            board[i] = "x"
            if checkWinAI("x") == True:
                board[i] = "o"
                return
            else:
                board[i] = " "
    if board[AI] != "x" and board[AI] != "o":
        board[AI] = "o"
    else:
        AIturnHARD()

def AIturnGOD(): # Player against AI GOD MODE
    AI = random.randint (1,9)
    if board[5] != "x" and board [5] != "o":
        board[5] = "o"
        return
    for i in range(1, 10):
        if board[i] == " ":
            board[i] = "o"
            if checkWinAI("o") == True:
                board[i] = "o"
                return
            else:
                board[i] = " "
    for i in range(1, 10):
        if board[i] == " ":
            board[i] = "x"
            if checkWinAI("x") == True:
                board[i] = "o"
                return
            else:
                board[i] = " "
    if firstplayer == 1 and rounds == 2: # if P1 first and center is taken, try to hit corners
        for i in (1, 3, 7, 9):
            if board[i] == " ":
                board[i] = "o"
                return
    if firstplayer == 1 and rounds == 4: # if P1 first, try to hit corners
        if board[2] == "x" and board[4] == "x":
            if board[1] == " ":
                board[1] = "o"
                return
        if board[2] == "x" and board[6] == "x":
            if board[3] == " ":
                board[3] = "o"
                return
        if board[8] == "x" and board[4] == "x":
            if board[7] == " ":
                board[7] = "o"
                return
        if board[8] == "x" and board[6] == "x":
            if board[9] == " ":
                board[9] = "o"
                return
        elif board[5] == "o" or board[5] == "x": # if P1 first, try to hit corners
            for i in (1, 3, 7, 9):
                if board[i] == " ":
                    board[i] = "o"
                    return

    if firstplayer == 2 and rounds == 3: # if AI starts first winrate is 100% :) good luck!
        if board[1] == "x" or board[2] == "x":
            board[9] = "o"
            return
        if board[3] == "x" or board[6] == "x":
            board[7] = "o"
            return
        if board[9] == "x" or board[8] == "x":
            board[1] = "o"
            return
        if board[7] == "x" or board[4] == "x":
            board[3] = "o"
            return     
    if rounds == 5:
        if board[1] == "x":
            if board[6] == " ":
                board[6] = "o"
                return
            elif board[8] == " ":
                board[8] = "o"
                return
        if board[3] == "x":
            if board[4] == " ":
                board[4] = "o"
                return
            elif board[8] == " ":
                board[8] = "o"
                return
        if board[9] == "x":
            if board[2] == " ":
                board[2] = "o"
                return
            elif board[4] == " ":
                board[4] = "o"
                return
        if board[7] == "x":
            if board[2] == " ":
                board[2] = "o"
                return
            elif board[6] == " ":
                board[6] = "o"
                return
    if board[AI] != "x" and board[AI] != "o":
        board[AI] = "o"
    else:
        AIturnGOD()

def playerVSplayer(): #Game for player vs player
    global rounds
    if firstplayer == 1: #P1 first
        while True:
            if ingame == 1:
                p1Turn()
                rounds = rounds + 1
                checkWin("x")
                show()
            if ingame == 1:
                p2Turn()
                rounds = rounds + 1
                checkWin("o")
                show()
            else:
                endGame()
                break
    if firstplayer == 2: #P2 first
        while True:
            if ingame == 1:
                p2Turn()
                rounds = rounds + 1
                checkWin("o")
                show()
            if ingame == 1:
                p1Turn()
                rounds = rounds + 1
                checkWin("x")
                show()
            else:
                endGame()
                break

def playerVSai(): #Game for player vs AI
    global rounds
    if firstplayer == 1: #P1 first
        while True:
            if ingame == 1:
                p1Turn()
                rounds = rounds + 1
                checkWin("x")
                show()
            if ingame == 1:
                print("\033[1;36m","AI turn!","\033[0m")
                time.sleep(1)
                print("\033[1;36m","AI is thinking...","\033[0m")
                time.sleep(2)
                AIturn()
                rounds = rounds + 1
                checkWin("o")
                show()
            else:
                endGame()
                break
    if firstplayer == 2: #P2 first
        while True:
            if ingame == 1:
                print("\033[1;36m","AI turn!","\033[0m")
                time.sleep(1)
                print("\033[1;36m","AI is thinking...","\033[0m")
                time.sleep(2)
                AIturn()
                rounds = rounds + 1
                checkWin("o")
                show()
            if ingame == 1:
                p1Turn()
                rounds = rounds + 1
                checkWin("x")
                show()
            else:
                endGame()
                break

def playerVSaiHARDMODE(): #Game for player vs AI HARD MODE!
    global rounds
    if firstplayer == 1: #P1 first
        while True:
            if ingame == 1:
                p1Turn()
                rounds = rounds + 1
                checkWin("x")
                show()
            if ingame == 1:
                print("\033[1;36m","AI turn!","\033[0m")
                time.sleep(1)
                print("\033[1;36m","AI is thinking...(for real)","\033[0m")
                time.sleep(2)
                AIturnHARD()
                rounds = rounds + 1
                checkWin("o")
                show()
            else:
                endGame()
                break
    if firstplayer == 2: #P2 first
        while True:
            if ingame == 1:
                print("\033[1;36m","AI turn!","\033[0m")
                time.sleep(1)
                print("\033[1;36m","AI is thinking...(for real)","\033[0m")
                time.sleep(2)
                AIturnHARD()
                rounds = rounds + 1
                checkWin("o")
                show()
            if ingame == 1:
                p1Turn()
                rounds = rounds + 1
                checkWin("x")
                show()
            else:
                endGame()
                break

def playerVSaiGODMODE(): #Game for player vs AI GOD MODE!!!! GOOD LUCK!
    global rounds
    if firstplayer == 1: #P1 first
        while True:
            if ingame == 1:
                p1Turn()
                rounds = rounds + 1
                checkWin("x")
                show()
            if ingame == 1:
                print("\033[1;36m","AI turn!","\033[0m")
                time.sleep(1)
                print("\033[1;36m","AI is thinking...(like a God!!!)","\033[0m")
                time.sleep(2)
                AIturnGOD()
                rounds = rounds + 1
                checkWin("o")
                show()
            else:
                endGame()
                break
    if firstplayer == 2: #P2 first
        while True:
            if ingame == 1:
                print("\033[1;36m","AI turn!","\033[0m")
                time.sleep(1)
                print("\033[1;36m","AI is thinking...(like a God!!!)","\033[0m")
                time.sleep(2)
                AIturnGOD()
                rounds = rounds + 1
                checkWin("o")
                show()
            if ingame == 1:
                p1Turn()
                rounds = rounds + 1
                checkWin("x")
                show()
            else:
                endGame()
                break

def show():
    print ("\033c")
    print (" ","\033[1;30;46m ","       ","\033[0m""\033[1;30;44m ","       ","\033[0m""\033[1;30;46m ","       ","\033[0m","         ****  ","1", "|","2","|","3")
    print (" ","\033[1;30;46m ","","\033[0m""\033[1;30;46m ",board[1],"\033[0m""\033[1;30;46m ","","\033[0m""\033[1;30;44m ","","\033[0m""\033[1;30;44m ",board[2],"\033[0m""\033[1;30;44m ","","\033[0m""\033[1;30;46m ","","\033[0m""\033[1;30;46m ",board[3],"\033[0m""\033[1;30;46m ","","\033[0m","         KEYS  ","4", "|","5","|","6")
    print (" ","\033[1;30;46m ","       ","\033[0m""\033[1;30;44m ","       ","\033[0m""\033[1;30;46m ","       ","\033[0m","         ****  ","7", "|","8","|","9")
    print (" ","\033[1;30;44m ","       ","\033[0m""\033[1;30;46m ","       ","\033[0m""\033[1;30;44m ","       ","\033[0m")
    print (" ","\033[1;30;44m ","","\033[0m""\033[1;30;44m ",board[4],"\033[0m""\033[1;30;44m ","","\033[0m""\033[1;30;46m ","","\033[0m""\033[1;30;46m ",board[5],"\033[0m""\033[1;30;46m ","","\033[0m""\033[1;30;44m ","","\033[0m""\033[1;30;44m ",board[6],"\033[0m""\033[1;30;44m ","","\033[0m", "         Games : " + str(gamerounds))
    print (" ","\033[1;30;44m ","       ","\033[0m""\033[1;30;46m ","       ","\033[0m""\033[1;30;44m ","       ","\033[0m","         Turn  : " + str(rounds))
    print (" ","\033[1;30;46m ","       ","\033[0m""\033[1;30;44m ","       ","\033[0m""\033[1;30;46m ","       ","\033[0m","\033[1;31m","        Player1 wins:","\033[0m" + str(P1wins))
    print (" ","\033[1;30;46m ","","\033[0m""\033[1;30;46m ",board[7],"\033[0m""\033[1;30;46m ","","\033[0m""\033[1;30;44m ","","\033[0m""\033[1;30;44m ",board[8],"\033[0m""\033[1;30;44m ","","\033[0m""\033[1;30;46m ","","\033[0m""\033[1;30;46m ",board[9],"\033[0m""\033[1;30;46m ","","\033[0m","\033[1;32m","        Player2 wins:","\033[0m" + str(P2wins))
    print (" ","\033[1;30;46m ","       ","\033[0m""\033[1;30;44m ","       ","\033[0m""\033[1;30;46m ","       ","\033[0m","         Draws: " + str(draws))
    print ("\n")

while True: #main Game loop
    show()
    gameChoose = input(" Choose a game mode! \n   P: Player vs. Player \n   A1: Player vs. AI (Easy) \n   A2: Player vs. AI (Hard) \n   A3: Player vs. AI (God Mode) \n   R: Reset scores \n   E: Exit \n")
    if gameChoose == "a1" or gameChoose == "A1":
        newGame()
        playerVSai()
    elif gameChoose == "a2" or gameChoose == "A2":
        newGame()
        playerVSaiHARDMODE()
    elif gameChoose == "a3" or gameChoose == "A3":
        newGame()
        playerVSaiGODMODE()
    elif gameChoose == "p" or gameChoose == "P":
        newGame()  
        playerVSplayer()
    elif gameChoose == "r" or gameChoose == "R":
        resetScores()
        continue
    elif gameChoose == "e" or gameChoose == "E":
        print (" Thanks for playing!")
        time.sleep(2)
        print (" Shutting down...")
        time.sleep(2)
        print ("\033c")
        break
    else:
        continue
