import random
import time

win_rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

board = list(range(0, 10))  # 3x3 board for the game

"""game_on = 1  # 1=game runs or 0=game stops
gamerounds = 0  # all game rounds
turns = 0  # turn num in a game
whos_first = 0  # which player is first 1 or 2
who_wins = ""  # who wins the game? x or o? or draw?
p1wins = 0  # P1 score count
p2wins = 0  # P2 score count
draws = 0  # Draw count"""
"
score_sets = {
            "game_on": 1,
            "gamerounds": 0
            "turns": 0
            "whos_first": 0
            "who_wins": ""
            "p1wins": 0
            "p2wins": 0
            "draws": 0
            }


def new_game():  # new game. resets a lot of things...
    global board
    board = [" "]*10
    score_sets["gamerounds"] += 1
    score_sets["turns"] = 1
    score_sets["game_on"] = 1
    random_player_first()
    show()


def random_player_first():
    score_sets["whos_first"] = random.randint(1, 2)


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
    gamerounds, turns, p1wins, p2wins, draws = 0, 0, 0, 0, 0
    print(" Resetting scores, please wait...")
    time.sleep(2)


def win_message():
    if who_wins == "x":
        print("\033[1;31m", "Player1 wins!!!", "\033[0m")
    elif who_wins == "o":
        print("\033[1;32m", "Player2 wins!!!", "\033[0m")
    elif who_wins == "draw":
        print(" It's a draw!!!")
    time.sleep(2)


def use_free_spot(spot, char):
    if board[spot] == " ":
        board[spot] = char
        return True


def check_line(char, row):  # checks if 3 index of list is equal
    if board[row[0]] == char and board[row[1]] == char and board[row[2]] == char:
        return True


def check_win(char):  # checks each row for win, or draw at round number 9
    global game_on
    global who_wins
    for row in win_rows:
        if check_line(char, row):
            who_wins = char
            game_on = 0
            return
    if turns == 10:
        who_wins = "draw"
        game_on = 0
        return


def check_win_ai(char):  # checks each row for win option for AI
    for row in win_rows:
        if check_line(char, row):
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


def player_turn(char):  # Player input, checks if the spot is taken
    while True:
        if char == "x":
            print("\033[1;31m", "Player1 turn!", "\033[0m")
        else:
            print("\033[1;32m", "Player2 turn!", "\033[0m")
        newspot = player_input()
        if use_free_spot(newspot, char):
            end_turn(char)
            break
        else:
            print (" You can't put your '%s' there, it is already taken!" % (char))


def end_turn(char):
    global turns
    turns += 1
    check_win(char)
    show()


def ai_turn_easy(char):  # Player against AI
    print("\033[1;36m", "AI turn!", "\033[0m")
    time.sleep(1)
    print("\033[1;36m", "AI is thinking...", "\033[0m")
    time.sleep(2)
    while True:
        AI = random.randint(1, 9)
        if use_free_spot(AI, "o"):
            break
    end_turn("o")


def ai_turn_hard(char):  # Player against AI HARD MODE
    ok_spot = 0
    print("\033[1;36m", "AI turn!", "\033[0m")
    time.sleep(1)
    print("\033[1;36m", "AI is thinking...(for real)", "\033[0m")
    time.sleep(2)
    ai_pick_spot_hard()
    end_turn("o")


def ai_pick_spot_hard():
    while True:
        AI = random.randint(1, 9)
        for i in range(1, 10):
            if use_free_spot(i, "o"):
                if check_win_ai("o"):
                    board[i] = "o"
                    return
                else:
                    board[i] = " "
            if use_free_spot(i, "x"):
                if check_win_ai("x"):
                    board[i] = "o"
                    return
                else:
                    board[i] = " "
        if use_free_spot(AI, "o"):
            return


def ai_turn_god(char):  # Player against AI GOD MODE
    print("\033[1;36m", "AI turn!", "\033[0m")
    time.sleep(1)
    print("\033[1;36m", "AI is thinking...(like a God!!!)", "\033[0m")
    time.sleep(2)
    ai_pick_spot_god()
    end_turn("o")


def ai_pick_spot_god():
    while True:
        AI = random.randint(1, 9)
        if use_free_spot(5, "o"):
            return
        for i in range(1, 10):
            if use_free_spot(i, "o"):
                if check_win_ai("o"):
                    board[i] = "o"
                    return
                else:
                    board[i] = " "
            if use_free_spot(i, "x"):
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
        if whos_first == 2 and turns == 5:
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
        if use_free_spot(AI, "o"):
            return


def game(player_one, player_two):
    new_game()
    if whos_first == 1:
        while True:
            if game_on == 1:
                player_one("x")
            if game_on == 1:
                player_two("o")
            else:
                end_game()
                return
    if whos_first == 2:  # P2 first
        while True:
            if game_on == 1:
                player_two("o")
            if game_on == 1:
                player_one("x")
            else:
                end_game()
                return


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
    print(who_wins)
    print(game_on)
    print(board)


def main_menu():
    while True:  # main Game loop
        show()
        print ("Choose a game mode!")
        print ("   P: Player vs. Player")
        print ("   A1: Player vs. AI (Easy)")
        print ("   A2: Player vs. AI (Hard)")
        print ("   A3: Player vs. AI (God Mode)")
        print ("   R: Reset scores")
        print ("   E: Exit")
        gameChoose = input()
        if gameChoose == "a1" or gameChoose == "A1":
            game(player_turn, ai_turn_easy)
        elif gameChoose == "a2" or gameChoose == "A2":
            game(player_turn, ai_turn_hard)
        elif gameChoose == "a3" or gameChoose == "A3":
            game(player_turn, ai_turn_god)
        elif gameChoose == "p" or gameChoose == "P":
            game(player_turn, player_turn)
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


main_menu()
