import random
import time

win_rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

board = list(range(0, 10))  # 3x3 board for the game


score_sets = {
    "game_on": 1,
    "gamerounds": 0,
    "turns": 0,
    "whos_first": 0,
    "who_wins": "",
    "p1wins": 0,
    "p2wins": 0,
    "draws": 0,
    "level": 0,
    "percentage": 0,
}


def new_game():  # new game. resets a lot of things, choose first player
    global board
    board = [" "] * 10
    score_sets["gamerounds"] += 1
    score_sets["turns"] = 1
    score_sets["game_on"] = 1
    print ("Which player should start the game? P1: Player1 P2: Player2 R: Randomly selected ")
    while True:
        starting_player = input()
        if starting_player == "P1" or starting_player == "p1":
            score_sets["whos_first"] = 1
            break
        elif starting_player == "P2" or starting_player == "p2":
            score_sets["whos_first"] = 2
            break
        elif starting_player == "R" or starting_player == "r":
            score_sets["whos_first"] = random.randint(1, 2)
            break
    show()


def new_game_random_first(): # new game. resets a lot of things, set first player RANDOMLY
    global board
    board = [" "] * 10
    score_sets["gamerounds"] += 1
    score_sets["turns"] = 1
    score_sets["game_on"] = 1
    score_sets["whos_first"] = random.randint(1, 2)
    show()


def story_mode():
    score_sets["percentage"] = 0
    score_sets["level"] = 1
    while score_sets["level"] != 6:
        while True:
            new_game_random_first()
            game(player_turn, ai_turn_hard, "x", "o", score_sets["percentage"])
            if score_sets["who_wins"] == "x":
                score_sets["percentage"] += 25
                score_sets["level"] += 1
                break
    print (" Congratulations, you have completed the Story mode!")
    time.sleep(2)
    score_sets["level"] = 0
    main_menu()


def end_game():  # end game. add score count
    if score_sets["who_wins"] == "x":
        score_sets["p1wins"] += 1
    elif score_sets["who_wins"] == "o":
        score_sets["p2wins"] += 1
    elif score_sets["who_wins"] == "draw":
        score_sets["draws"] += 1
    win_message()


def reset_scores():  # reset scores
    board = range(0, 10)
    score_sets["gamerounds"] = 0
    score_sets["turns"] = 0
    score_sets["p1wins"] = 0
    score_sets["p2wins"] = 0
    score_sets["draws"] = 0
    print(" Resetting scores, please wait...")
    time.sleep(2)


def win_message():
    if score_sets["who_wins"] == "x":
        print("\033[1;31m", "Player1 wins!!!", "\033[0m")
    elif score_sets["who_wins"] == "o":
        print("\033[1;32m", "Player2 wins!!!", "\033[0m")
    elif score_sets["who_wins"] == "draw":
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
    for row in win_rows:
        if check_line(char, row):
            score_sets["who_wins"] = char
            score_sets["game_on"] = 0
            return
    if score_sets["turns"] == 10:
        score_sets["who_wins"] = "draw"
        score_sets["game_on"] = 0
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


def player_turn(char, percentage):  # Player input, checks if the spot is taken
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
    score_sets["turns"] += 1
    check_win(char)
    show()


def ai_turn_easy(char, percentage):  # Player against AI
    print("\033[1;36m", "AI turn!", "\033[0m")
    time.sleep(1)
    print("\033[1;36m", "AI is thinking...", "\033[0m")
    time.sleep(2)
    while True:
        AI = random.randint(1, 9)
        if use_free_spot(AI, "o"):
            break
    end_turn("o")


def ai_turn_hard(char, percentage):  # Player against AI HARD MODE
    print("\033[1;36m", "AI turn!", "\033[0m")
    time.sleep(1)
    print("\033[1;36m", "AI is thinking...(for real)", "\033[0m")
    time.sleep(2)
    ai_pick_spot_hard(percentage)
    end_turn("o")


def ai_pick_spot_hard(percentage):
    while True:
        lucky_number = range(1, 100)
        AI = random.randint(1, 9)
        if lucky_number in range(1, percentage):
            while True:
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


def ai_turn_god(char, percentage):  # Player against AI GOD MODE
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
        if score_sets["turns"] == 2:  # if P1 first and center is taken, try to hit corners
            for i in (1, 3, 7, 9):
                if board[i] == " ":
                    board[i] = "o"
                    return
        if score_sets["turns"] == 4:  # if P1 first, try to hit corners
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

        if score_sets["turns"] == 3:  # if AI starts first winrate is 100% :) good luck!
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
        if score_sets["turns"] == 5:
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


def game(player_one, player_two, char_one, char_two, percentage=None):
    if score_sets["whos_first"] == 1:
        while True:
            if score_sets["game_on"] == 1:
                player_one(char_one, percentage)
            if score_sets["game_on"] == 1:
                player_two(char_two, percentage)
            else:
                end_game()
                return
    if score_sets["whos_first"] == 2:  # P2 first
        while True:
            if score_sets["game_on"] == 1:
                player_two(char_two, percentage)
            if score_sets["game_on"] == 1:
                player_one(char_one, percentage)
            else:
                end_game()
                return


def show():
    print ("\033c")
    print (
        " ",
        "\033[1;30;46m ",
        "       ",
        "\033[0m"
        "\033[1;30;44m ",
        "       ",
        "\033[0m"
        "\033[1;30;46m ",
        "       ",
        "\033[0m",
        "         ****  ",
        "1",
        "|",
        "2",
        "|",
        "3")
    print (
        " ", "\033[1;30;46m ", "", "\033[0m"
        "\033[1;30;46m ", board[1], "\033[0m"
        "\033[1;30;46m ", "", "\033[0m"
        "\033[1;30;44m ", "", "\033[0m"
        "\033[1;30;44m ", board[2], "\033[0m"
        "\033[1;30;44m ", "", "\033[0m"
        "\033[1;30;46m ", "", "\033[0m"
        "\033[1;30;46m ", board[3], "\033[0m"
        "\033[1;30;46m ", "", "\033[0m", "         KEYS  ", "4", "|", "5", "|", "6")
    print (
        " ",
        "\033[1;30;46m ",
        "       ",
        "\033[0m"
        "\033[1;30;44m ",
        "       ",
        "\033[0m"
        "\033[1;30;46m ",
        "       ",
        "\033[0m",
        "         ****  ",
        "7",
        "|",
        "8",
        "|",
        "9")
    print (
        " ",
        "\033[1;30;44m ",
        "       ",
        "\033[0m"
        "\033[1;30;46m ",
        "       ",
        "\033[0m"
        "\033[1;30;44m ",
        "       ",
        "\033[0m")
    print (" ", "\033[1;30;44m ", "", "\033[0m"
           "\033[1;30;44m ", board[4], "\033[0m"
           "\033[1;30;44m ", "", "\033[0m"
           "\033[1;30;46m ", "", "\033[0m"
           "\033[1;30;46m ", board[5], "\033[0m"
           "\033[1;30;46m ", "", "\033[0m"
           "\033[1;30;44m ", "", "\033[0m"
           "\033[1;30;44m ", board[6], "\033[0m"
           "\033[1;30;44m ", "", "\033[0m", "         Games : " +
           str(score_sets["gamerounds"]))
    print (" ", "\033[1;30;44m ", "       ", "\033[0m""\033[1;30;46m ", "       ",
           "\033[0m""\033[1;30;44m ", "       ", "\033[0m", "         Turn  : " + str(score_sets["turns"]))
    print (" ",
           "\033[1;30;46m ",
           "       ",
           "\033[0m"
           "\033[1;30;44m ",
           "       ",
           "\033[0m"
           "\033[1;30;46m ",
           "       ",
           "\033[0m",
           "\033[1;31m",
           "        Player1 wins:",
           "\033[0m" + str(score_sets["p1wins"]))
    print (" ", "\033[1;30;46m ", "", "\033[0m"
           "\033[1;30;46m ", board[7], "\033[0m"
           "\033[1;30;46m ", "", "\033[0m"
           "\033[1;30;44m ", "", "\033[0m"
           "\033[1;30;44m ", board[8], "\033[0m"
           "\033[1;30;44m ", "", "\033[0m"
           "\033[1;30;46m ", "", "\033[0m"
           "\033[1;30;46m ", board[9], "\033[0m"
           "\033[1;30;46m ", "", "\033[0m", "\033[1;32m", "        Player2 wins:", "\033[0m" +
           str(score_sets["p2wins"]))
    print (" ", "\033[1;30;46m ", "       ", "\033[0m""\033[1;30;44m ", "       ",
           "\033[0m""\033[1;30;46m ", "       ", "\033[0m", "         Draws: " + str(score_sets["draws"]))
    print ("\n")

    if score_sets["level"] > 0:
        print ("   STORYMODE")
        print ("    Level:"  "%s" "\n" % (score_sets["level"]))


def main_menu():
    while True:  # main Game loop
        show()
        print ("Choose a game mode!\n".rjust(40))
        print ("   S: Singleplayer")
        print ("   M: Multiplayer")
        print ("   R: Reset scores")
        print ("   E: Exit")
        game_choose = input()
        if game_choose == "S" or game_choose == "s":
            single_player()
        elif game_choose == "M" or game_choose == "m":
            multiplayer()
        elif game_choose == "r" or game_choose == "R":
            reset_scores()
        elif game_choose == "e" or game_choose == "E":
            print (" Thanks for playing!")
            time.sleep(2)
            print (" Shutting down...")
            time.sleep(2)
            print ("\033c")
            break


def single_player():
    while True:  # main Game loop
        show()
        print ("Singleplayer mode\n".rjust(40))
        print ("""In story mode you can play against AI. You start from level 1 and
each time you beat AI you can reach the next level.The game get's
harder level by level. Try to reach level 5! The game picks first
player randomly. Good luck!:\n""")
        print ("S: Story mode\n")
        print ("""In this section you can choose from different AI types, by hardness:\n""")
        print ("A1: Player vs. AI (Easy)")
        print ("A2: Player vs. AI (Hard)")
        print ("A3: Player vs. AI (God Mode)\n")
        print ("M: Main menu")
        print ("R: Reset scores")
        print ("E: Exit")
        game_choose = input()
        if game_choose == "a1" or game_choose == "A1":
            new_game()
            game(player_turn, ai_turn_easy, "x", "o")
        elif game_choose == "a2" or game_choose == "A2":
            new_game()
            game(player_turn, ai_turn_hard, "x", "o", 20)
        elif game_choose == "a3" or game_choose == "A3":
            new_game()
            game(player_turn, ai_turn_god, "x", "o")
        elif game_choose == "S" or game_choose == "s":
            story_mode()
        elif game_choose == "M" or game_choose == "m":
            main_menu()
        elif game_choose == "r" or game_choose == "R":
            reset_scores()
            main_menu()
        elif game_choose == "e" or game_choose == "E":
            print (" Thanks for playing!")
            time.sleep(2)
            print (" Shutting down...")
            time.sleep(2)
            print ("\033c")
            break


def multiplayer():
    while True:  # main Game loop
        show()
        print ("Multiplayer mode\n".rjust(40))
        print ("P: Player vs. Player\n")
        print ("M: Main menu")
        print ("R: Reset scores")
        print ("E: Exit")
        game_choose = input()
        if game_choose == "p" or game_choose == "P":
            new_game()
            game(player_turn, player_turn, "x", "o")
        elif game_choose == "r" or game_choose == "R":
            reset_scores()
        elif game_choose == "M" or game_choose == "m":
            main_menu()
        elif game_choose == "e" or game_choose == "E":
            print (" Thanks for playing!")
            time.sleep(2)
            print (" Shutting down...")
            time.sleep(2)
            print ("\033c")
            break


main_menu()
