import random
import time

board = list(range(0, 10))  # 3x3 board for the game
game_on = 1  # 1=game runs or 0=game stops
who_wins = ""  # who wins the game? x or o? or draw?

p1wins = 0  # P1 score count
p2wins = 0  # P2 score count
draws = 0  # Draw count

gamerounds = 0  # all game rounds
turns = 0  # turn num in a game
whos_first = 0  # which player is first 1 or 2


def new_game():  # new game. resets a lot of things
    global board
    global turns
    global gamerounds
    global game_on
    board = [" "]*10
    gamerounds += 1
    turns = 1
    game_on = 1
    random_player_first()
    show()


def random_player_first():
    global whos_first
    whos_first = random.randint(1, 2)


def end_game():  # end game. add score count
    global p1wins
    global p2wins
    global draws
    if who_wins == "x":
        p1wins += 1
    elif who_wins == "o":
        p2wins += 1
    elif who_wins == "draw":
        draws += 1
    win_message()


def reset_scores():  # reset scores
    global p1wins
    global p2wins
    global draws
    global gamerounds
    global turns
    board = range(0, 10)
    gamerounds = 0
    turns = 0
    p1wins = 0
    p2wins = 0
    draws = 0
    print(" Resetting scores, please wait...")
    time.sleep(2)


def win_message():
    if who_wins == "x":
        print("\033[1;31m", "Player1 wins!!!", "\033[0m")
        time.sleep(2)
    elif who_wins == "o":
        print("\033[1;32m", "Player2 wins!!!", "\033[0m")
        time.sleep(2)
    elif who_wins == "draw":
        print(" It's a draw!!!")
        time.sleep(2)


def check_line(char, spot1, spot2, spot3):  # checks if 3 index of list is equal
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True


def check_win(char):  # checks each row for win, or draw at round number 9
    global game_on
    global who_wins
    if check_line(char, 1, 2, 3):
        who_wins = char
        game_on = 0
    elif check_line(char, 4, 5, 6):
        who_wins = char
        game_on = 0
    elif check_line(char, 7, 8, 9):
        who_wins = char
        game_on = 0
    elif check_line(char, 1, 4, 7):
        who_wins = char
        game_on = 0
    elif check_line(char, 2, 5, 8):
        who_wins = char
        game_on = 0
    elif check_line(char, 3, 6, 9):
        who_wins = char
        game_on = 0
    elif check_line(char, 1, 5, 9):
        who_wins = char
        game_on = 0
    elif check_line(char, 3, 5, 7):
        who_wins = char
        game_on = 0
    elif turns == 10:
        who_wins = "draw"
        game_on = 0


def check_win_ai(char):  # checks each row for win option for AI
    if check_line(char, 1, 2, 3):
        return True
    elif check_line(char, 4, 5, 6):
        return True
    elif check_line(char, 7, 8, 9):
        return True
    elif check_line(char, 1, 4, 7):
        return True
    elif check_line(char, 2, 5, 8):
        return True
    elif check_line(char, 3, 6, 9):
        return True
    elif check_line(char, 1, 5, 9):
        return True
    elif check_line(char, 3, 5, 7):
        return True


def player_input():  # keyoard input only from 1-9
    while True:
            try:
                x = int(input(" Select a spot: "))
                if x in range(1, 10):
                    return x
                    break
                else:
                    print(" Please use numbers only between 1-9!")
                    continue
            except ValueError:
                print(" Please use the number keys, from 1-9!")
                continue


def p1_turn():  # P1 input, checks if the spot is taken
    print("\033[1;31m", "Player1 turn!", "\033[0m")
    newspot = player_input()
    if board[newspot] != "x" and board[newspot] != "o":
        board[newspot] = "x"
    else:
        print (" You can't put your 'x' there, it is already taken!")
        p1_turn()


def p2_turn():  # P2 input, checks if the spot is taken
    print("\033[1;32m", "Player2 turn!", "\033[0m")
    newspot = player_input()
    if board[newspot] != "x" and board[newspot] != "o":
        board[newspot] = "o"
    else:
        print (" You can't put your 'o' there, it is already taken!")
        p2_turn()


def ai_turn_easy():  # Player against AI
    AI = random.randint(1, 9)
    if board[AI] != "x" and board[AI] != "o":
        board[AI] = "o"
    else:
        ai_turn_easy()


def ai_turn_hard():  # Player against AI HARD MODE
    AI = random.randint(1, 9)
    for i in range(1, 10):
        if board[i] == " ":
            board[i] = "o"
            if check_win_ai("o"):
                board[i] = "o"
                return
            else:
                board[i] = " "
    for i in range(1, 10):
        if board[i] == " ":
            board[i] = "x"
            if check_win_ai("x"):
                board[i] = "o"
                return
            else:
                board[i] = " "
    if board[AI] != "x" and board[AI] != "o":
        board[AI] = "o"
    else:
        ai_turn_hard()


def ai_turn_god():  # Player against AI GOD MODE
    AI = random.randint(1, 9)
    if board[5] != "x" and board[5] != "o":
        board[5] = "o"
        return
    for i in range(1, 10):
        if board[i] == " ":
            board[i] = "o"
            if check_win_ai("o"):
                board[i] = "o"
                return
            else:
                board[i] = " "
    for i in range(1, 10):
        if board[i] == " ":
            board[i] = "x"
            if check_win_ai("x"):
                board[i] = "o"
                return
            else:
                board[i] = " "
    if whos_first == 1 and turns == 2:  # if P1 first and center is taken, try to hit corners
        for i in (1, 3, 7, 9):
            if board[i] == " ":
                board[i] = "o"
                return
    if whos_first == 1 and turns == 4:  # if P1 first, try to hit corners
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
        elif board[5] == "o" or board[5] == "x":  # if P1 first, try to hit corners
            for i in (1, 3, 7, 9):
                if board[i] == " ":
                    board[i] = "o"
                    return

    if whos_first == 2 and turns == 3:  # if AI starts first winrate is 100% :) good luck!
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
    if turns == 5:
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
        ai_turn_god()

def player_vs_player():  # Game for player vs player
    global turns
    if whos_first == 1:  # P1 first
        while True:
            if game_on == 1:
                p1_turn()
                turns = turns + 1
                check_win("x")
                show()
            if game_on == 1:
                p2_turn()
                turns = turns + 1
                check_win("o")
                show()
            else:
                end_game()
                break
    if whos_first == 2:  # P2 first
        while True:
            if game_on == 1:
                p2_turn()
                turns = turns + 1
                check_win("o")
                show()
            if game_on == 1:
                p1_turn()
                turns = turns + 1
                check_win("x")
                show()
            else:
                end_game()
                break


def player_vs_ai_easy():  # Game for player vs AI
    global turns
    if whos_first == 1:  # P1 first
        while True:
            if game_on == 1:
                p1_turn()
                turns = turns + 1
                check_win("x")
                show()
            if game_on == 1:
                print("\033[1;36m", "AI turn!", "\033[0m")
                time.sleep(1)
                print("\033[1;36m", "AI is thinking...", "\033[0m")
                time.sleep(2)
                ai_turn_easy()
                turns = turns + 1
                check_win("o")
                show()
            else:
                end_game()
                break
    if whos_first == 2:  # P2 first
        while True:
            if game_on == 1:
                print("\033[1;36m", "AI turn!", "\033[0m")
                time.sleep(1)
                print("\033[1;36m", "AI is thinking...", "\033[0m")
                time.sleep(2)
                ai_turn_easy()
                turns = turns + 1
                check_win("o")
                show()
            if game_on == 1:
                p1_turn()
                turns = turns + 1
                check_win("x")
                show()
            else:
                end_game()
                break


def player_vs_ai_hard():  # Game for player vs AI HARD MODE!
    global turns
    if whos_first == 1:  # P1 first
        while True:
            if game_on == 1:
                p1_turn()
                turns = turns + 1
                check_win("x")
                show()
            if game_on == 1:
                print("\033[1;36m", "AI turn!", "\033[0m")
                time.sleep(1)
                print("\033[1;36m", "AI is thinking...(for real)", "\033[0m")
                time.sleep(2)
                ai_turn_hard()
                turns = turns + 1
                check_win("o")
                show()
            else:
                end_game()
                break
    if whos_first == 2:  # P2 first
        while True:
            if game_on == 1:
                print("\033[1;36m", "AI turn!", "\033[0m")
                time.sleep(1)
                print("\033[1;36m", "AI is thinking...(for real)", "\033[0m")
                time.sleep(2)
                ai_turn_hard()
                turns = turns + 1
                check_win("o")
                show()
            if game_on == 1:
                p1_turn()
                turns = turns + 1
                check_win("x")
                show()
            else:
                end_game()
                break


def player_vs_ai_god():  # Game for player vs AI GOD MODE!!!! GOOD LUCK!
    global turns
    if whos_first == 1:  # P1 first
        while True:
            if game_on == 1:
                p1_turn()
                turns = turns + 1
                check_win("x")
                show()
            if game_on == 1:
                print("\033[1;36m", "AI turn!", "\033[0m")
                time.sleep(1)
                print("\033[1;36m", "AI is thinking...(like a God!!!)", "\033[0m")
                time.sleep(2)
                ai_turn_god()
                turns = turns + 1
                check_win("o")
                show()
            else:
                end_game()
                break
    if whos_first == 2:  # P2 first
        while True:
            if game_on == 1:
                print("\033[1;36m", "AI turn!", "\033[0m")
                time.sleep(1)
                print("\033[1;36m", "AI is thinking...(like a God!!!)", "\033[0m")
                time.sleep(2)
                ai_turn_god()
                turns = turns + 1
                check_win("o")
                show()
            if game_on == 1:
                p1_turn()
                turns = turns + 1
                check_win("x")
                show()
            else:
                end_game()
                break


def show():
    print ("\033c")
    print (" ", "\033[1;30;46m ", "       ", "\033[0m""\033[1;30;44m ", "       ", "\033[0m""\033[1;30;46m ", "       ", "\033[0m", "         ****  ", "1", "|", "2","|","3")
    print (" ","\033[1;30;46m ","","\033[0m""\033[1;30;46m ",board[1],"\033[0m""\033[1;30;46m ","","\033[0m""\033[1;30;44m ","","\033[0m""\033[1;30;44m ",board[2],"\033[0m""\033[1;30;44m ","","\033[0m""\033[1;30;46m ","","\033[0m""\033[1;30;46m ",board[3],"\033[0m""\033[1;30;46m ","","\033[0m","         KEYS  ","4", "|","5","|","6")
    print (" ","\033[1;30;46m ","       ","\033[0m""\033[1;30;44m ","       ","\033[0m""\033[1;30;46m ","       ","\033[0m","         ****  ","7", "|","8","|","9")
    print (" ","\033[1;30;44m ","       ","\033[0m""\033[1;30;46m ","       ","\033[0m""\033[1;30;44m ","       ","\033[0m")
    print (" ","\033[1;30;44m ","","\033[0m""\033[1;30;44m ",board[4],"\033[0m""\033[1;30;44m ","","\033[0m""\033[1;30;46m ","","\033[0m""\033[1;30;46m ",board[5],"\033[0m""\033[1;30;46m ","","\033[0m""\033[1;30;44m ","","\033[0m""\033[1;30;44m ",board[6],"\033[0m""\033[1;30;44m ","","\033[0m", "         Games : " + str(gamerounds))
    print (" ","\033[1;30;44m ","       ","\033[0m""\033[1;30;46m ","       ","\033[0m""\033[1;30;44m ","       ","\033[0m","         Turn  : " + str(turns))
    print (" ","\033[1;30;46m ","       ","\033[0m""\033[1;30;44m ","       ","\033[0m""\033[1;30;46m ","       ","\033[0m","\033[1;31m","        Player1 wins:","\033[0m" + str(p1wins))
    print (" ","\033[1;30;46m ","","\033[0m""\033[1;30;46m ",board[7],"\033[0m""\033[1;30;46m ","","\033[0m""\033[1;30;44m ","","\033[0m""\033[1;30;44m ",board[8],"\033[0m""\033[1;30;44m ","","\033[0m""\033[1;30;46m ","","\033[0m""\033[1;30;46m ",board[9],"\033[0m""\033[1;30;46m ","","\033[0m","\033[1;32m","        Player2 wins:","\033[0m" + str(p2wins))
    print (" ","\033[1;30;46m ","       ","\033[0m""\033[1;30;44m ","       ","\033[0m""\033[1;30;46m ","       ","\033[0m","         Draws: " + str(draws))
    print ("\n")


while True:  # main Game loop
    show()
    gameChoose = input(" Choose a game mode! \n   P: Player vs. Player \n   A1: Player vs. AI (Easy) \n   A2: Player vs. AI (Hard) \n   A3: Player vs. AI (God Mode) \n   R: Reset scores \n   E: Exit \n")
    if gameChoose == "a1" or gameChoose == "A1":
        new_game()
        player_vs_ai_easy()
    elif gameChoose == "a2" or gameChoose == "A2":
        new_game()
        player_vs_ai_hard()
    elif gameChoose == "a3" or gameChoose == "A3":
        new_game()
        player_vs_ai_god()
    elif gameChoose == "p" or gameChoose == "P":
        new_game()
        player_vs_player()
    elif gameChoose == "r" or gameChoose == "R":
        reset_scores()
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
