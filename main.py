"""
XOX game for player vs computer."""

import sys
import random

field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
v1_c = [[0, 0], [1, 0], [2, 0]]
v2_c = [[0, 1], [1, 1], [2, 1]]
v3_c = [[0, 2], [1, 2], [2, 2]]
h1_c = [[0, 0], [0, 1], [0, 2]]
h2_c = [[1, 0], [1, 1], [1, 2]]
h3_c = [[2, 0], [2, 1], [2, 2]]
dr_c = [[0, 0], [1, 1], [2, 2]]
dl_c = [[0, 2], [1, 1], [2, 0]]

corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
sides = [[0, 1], [1, 0], [1, 2], [2, 1]]
all = [[0, 0], [0, 2], [2, 0], [2, 2], [0, 1], [1, 0], [1, 2], [2, 1]]
optionx = [" xx", "xx ", "x x"]
optiono = [" oo", "oo ", "o o"]

directions = []
player_turns = []
rule_1 = []
rule_2 = []


def show():
    print(f"\n\t   0   1   2")
    print(f"\t0  {field[0][0]} | {field[0][1]} | {field[0][2]}")
    print(f"\t  ---+---+---")
    print(f"\t1  {field[1][0]} | {field[1][1]} | {field[1][2]}")
    print(f"\t  ---+---+---")
    print(f"\t2  {field[2][0]} | {field[2][1]} | {field[2][2]}")


def player_turn():
    while True:
        print("Please chose line number 0...2 or press (Q) to quit.")
        y = input(">: ")
        if y.lower() == "q":
            sys.exit()
        elif y.isdigit() and int(y) in range(0, 3):
            y = int(y)
        else:
            print("Please input digit in range 0...2 or press (Q) to quit.")
            continue

        print("Please chose column number 0...2 or press (Q) to quit.")
        x = input(">: ")
        if x.lower() == "q":
            sys.exit()
        elif x.isdigit() and int(x) in range(0, 3):
            x = int(x)
        else:
            print("Please input digit in range 0...2 or press (Q) to quit.")
            continue

        if field[y][x] == " ":
            player_turns.append([y, x])
            return [y, x]

        else:
            print("Please chose another cell.")
            continue

def enemy_turn():
    # versatile strategy:
    if len(rule_1) != 0:
        for p in rule_1:
            if field[p[0]][p[1]] == " ":
                print(f"Computer's choice is [{p[0]},{p[1]}].")
                return [p[0], p[1]]
    # -----------------------------------
    elif len(rule_2) != 0:
        for p in rule_2:
            if field[p[0]][p[1]] == " ":
                print(f"Computer's choice is [{p[0]},{p[1]}].")
                return [p[0], p[1]]

    # round 1 strategy (complete)
    if counter == 1 and first == "computer":
        print("Computer's choice is [1,1]. Right in the center!")
        return [1, 1]
    # -----------------------------------
    elif counter == 1 and first == "player":
        if player_turns[0] == [1, 1]:
            p = random.choice(corners)
            print(f"Computer's choice is [{p[0]},{p[1]}].")
            return [p[0], p[1]]
        elif player_turns[0] in corners:
            print("Computer's choice is [1,1]. Right in the center!")
            return [1, 1]
        elif player_turns[0] in sides:
            print("Computer's choice is [1,1]. Right in the center!")
            return [1, 1]

    # round 2 strategy
    if counter == 2 and first == "computer":

        y = player_turns[0][0]
        x = player_turns[0][1]
        far_y = []
        far_x = []
        to_hit_list = []

        if y == 0:
            far_y.append(2)
        elif y == 1:
            far_y.append(0)
            far_y.append(2)
        elif y == 2:
            far_y.append(0)

        if x == 0:
            far_x.append(2)
        elif x == 1:
            far_x.append(0)
            far_x.append(2)
        elif x == 2:
            far_x.append(0)

        if len(far_x) > len(far_y):
            for p in far_x:
                to_hit_list.append([far_y[0], p])

        if len(far_x) < len(far_y):
            for p in far_y:
                to_hit_list.append([far_x[0], p])

        for p in to_hit_list:
            if field[p[0]][p[1]] == " ":
                print(f"Computer's choice is [{p[0]},{p[1]}].")
                far_y = []
                far_x = []
                to_hit_list = []
                return [p[0], p[1]]

        for p in all:
            if field[p[0]][p[1]] == " ":
                print(f"Computer's choice is [{p[0]},{p[1]}].")
                far_y = []
                far_x = []
                to_hit_list = []
                return [p[0], p[1]]
    # -----------------------------------
    if (counter == 2 and first == "player") and player_turns[0] == [1, 1]: #1
        for p in corners:
            if field[p[0]][p[1]] == " ":
                print(f"Computer's choice is [{p[0]},{p[1]}].")
                return [p[0], p[1]]

        for p in sides:
            if field[p[0]][p[1]] == " ":
                print(f"Computer's choice is [{p[0]},{p[1]}].")
                return [p[0], p[1]]

    if (counter == 2 and first == "player") and player_turns[0] in corners: #2
        y = player_turns[0][0]
        x = player_turns[0][1]
        far_y = []
        far_x = []

        if y == 0:
            far_y.append(2)
        elif y == 2:
            far_y.append(0)

        if x == 0:
            far_x.append(2)
        elif x == 2:
            far_x.append(0)

        if field[far_y[0]][far_x[0]] == " ":
            return [far_y[0], far_x[0]]
        else:
            for p in all:
                if field[p[0]][p[1]] == " ":
                    print(f"Computer's choice is [{p[0]},{p[1]}].")
                    far_y = []
                    far_x = []
                    return [p[0], p[1]]

    if (counter == 2 and first == "player") and (player_turns[0] in sides and player_turns[1] in corners):  # 3
        y = player_turns[1][0]
        x = player_turns[1][1]
        far_y = []
        far_x = []

        if y == 0:
            far_y.append(2)
        elif y == 2:
            far_y.append(0)

        if x == 0:
            far_x.append(2)
        elif x == 2:
            far_x.append(0)

        if field[far_y[0]][far_x[0]] == " ":
            return [far_y[0], far_x[0]]
        else:
            for p in all:
                if field[p[0]][p[1]] == " ":
                    print(f"Computer's choice is [{p[0]},{p[1]}].")
                    far_y = []
                    far_x = []
                    return [p[0], p[1]]

    if (counter == 2 and first == "player") and (player_turns[0] in sides and player_turns[1] in sides):  # 3
        for p in corners:
            if field[p[0]][p[1]] == " ":
                print(f"Computer's choice is [{p[0]},{p[1]}].")
                return [p[0], p[1]]

        for p in sides:
            if field[p[0]][p[1]] == " ":
                print(f"Computer's choice is [{p[0]},{p[1]}].")
                return [p[0], p[1]]

    # round 3 and more strategy
    if counter > 2 and first == "computer":
        y = player_turns[-1][0]
        x = player_turns[-1][1]
        far_y = []
        far_x = []
        to_hit_list = []

        if y == 0:
            far_y.append(2)
        elif y == 1:
            far_y.append(0)
            far_y.append(2)
        elif y == 2:
            far_y.append(0)

        if x == 0:
            far_x.append(2)
        elif x == 1:
            far_x.append(0)
            far_x.append(2)
        elif x == 2:
            far_x.append(0)

        if len(far_x) > len(far_y):
            for p in far_x:
                to_hit_list.append([far_y[0], p])

        if len(far_x) < len(far_y):
            for p in far_y:
                to_hit_list.append([far_x[0], p])

        for p in to_hit_list:
            if field[p[0]][p[1]] == " ":
                print(f"Computer's choice is [{p[0]},{p[1]}].")
                far_y = []
                far_x = []
                to_hit_list = []
                return [p[0], p[1]]

        for p in all:
            if field[p[0]][p[1]] == " ":
                print(f"Computer's choice is [{p[0]},{p[1]}].")
                far_y = []
                far_x = []
                to_hit_list = []
                return [p[0], p[1]]
    # -----------------------------------
    if (counter > 2 and first == "player") and player_turns[0] == [1, 1]:  # 1
        for p in corners:
            if field[p[0]][p[1]] == " ":
                print(f"Computer's choice is [{p[0]},{p[1]}].")
                return [p[0], p[1]]

        for p in sides:
            if field[p[0]][p[1]] == " ":
                print(f"Computer's choice is [{p[0]},{p[1]}].")
                return [p[0], p[1]]

    if (counter > 2 and first == "player") and (player_turns[0] in corners or player_turns[0] in sides):  # 2
        for p in corners:
            if field[p[0]][p[1]] == " ":
                print(f"Computer's choice is [{p[0]},{p[1]}].")
                return [p[0], p[1]]

        for p in sides:
            if field[p[0]][p[1]] == " ":
                print(f"Computer's choice is [{p[0]},{p[1]}].")
                return [p[0], p[1]]

    # -----------------------------------

def check_result():
    # Check if win is possible for any line
    v1 = field[0][0] + field[1][0] + field[2][0]
    v2 = field[0][1] + field[1][1] + field[2][1]
    v3 = field[0][2] + field[1][2] + field[2][2]
    h1 = field[0][0] + field[0][1] + field[0][2]
    h2 = field[1][0] + field[1][1] + field[1][2]
    h3 = field[2][0] + field[2][1] + field[2][2]
    dr = field[0][0] + field[1][1] + field[2][2]
    dl = field[0][2] + field[1][1] + field[2][0]

    directions = ['v1', "v2", "v3", "h1", "h2", "h3", "dr", "dl"]

    if "x" in v1 and "o" in v1:
        directions.remove("v1")
    if "x" in v2 and "o" in v2:
        directions.remove("v2")
    if "x" in v3 and "o" in v3:
        directions.remove("v3")
    if "x" in h1 and "o" in h1:
        directions.remove("h1")
    if "x" in h2 and "o" in h2:
        directions.remove("h2")
    if "x" in h3 and "o" in h3:
        directions.remove("h3")
    if "x" in dr and "o" in dr:
        directions.remove("dr")
    if "x" in dl and "o" in dl:
        directions.remove("dl")

    # Check rule #1 can be applied

    if (v1 in optionx and first == "computer") or (v1 in optiono and first == "player"):
        for point in v1_c:
            print(point)
            if field[point[0]][point[1]] == " ":
                rule_1.append(point)
    if (v2 in optionx and first == "computer") or (v2 in optiono and first == "player"):
        for point in v2_c:
            if field[point[0]][point[1]] == " ":
                rule_1.append(point)
    if (v3 in optionx and first == "computer") or (v3 in optiono and first == "player"):
        for point in v3_c:
            if field[point[0]][point[1]] == " ":
                rule_1.append(point)
    if (h1 in optionx and first == "computer") or (h1 in optiono and first == "player"):
        for point in h1_c:
            if field[point[0]][point[1]] == " ":
                rule_1.append(point)
    if (h2 in optionx and first == "computer") or (h2 in optiono and first == "player"):
        for point in h2_c:
            if field[point[0]][point[1]] == " ":
                rule_1.append(point)
    if (h3 in optionx and first == "computer") or (h3 in optiono and first == "player"):
        for point in h3_c:
            if field[point[0]][point[1]] == " ":
                rule_1.append(point)
    if (dr in optionx and first == "computer") or (dr in optiono and first == "player"):
        for point in dr_c:
            if field[point[0]][point[1]] == " ":
                rule_1.append(point)
    if (dl in optionx and first == "computer") or (dl in optiono and first == "player"):
        for point in dl_c:
            if field[point[0]][point[1]] == " ":
                rule_1.append(point)

    # Check rule #2 can be applied

    if (v1 in optionx and first == "player") or (v1 in optiono and first == "computer"):
        for point in v1_c:
            if field[point[0]][point[1]] == " ":
                rule_2.append(point)
    if (v2 in optionx and first == "player") or (v2 in optiono and first == "computer"):
        for point in v2_c:
            if field[point[0]][point[1]] == " ":
                rule_2.append(point)
    if (v3 in optionx and first == "player") or (v3 in optiono and first == "computer"):
        for point in v3_c:
            if field[point[0]][point[1]] == " ":
                rule_2.append(point)
    if (h1 in optionx and first == "player") or (h1 in optiono and first == "computer"):
        for point in h1_c:
            if field[point[0]][point[1]] == " ":
                rule_2.append(point)
    if (h2 in optionx and first == "player") or (h2 in optiono and first == "computer"):
        for point in h2_c:
            if field[point[0]][point[1]] == " ":
                rule_2.append(point)
    if (h3 in optionx and first == "player") or (h3 in optiono and first == "computer"):
        for point in h3_c:
            if field[point[0]][point[1]] == " ":
                rule_2.append(point)
    if (dr in optionx and first == "player") or (dr in optiono and first == "computer"):
        for point in dr_c:
            if field[point[0]][point[1]] == " ":
                rule_2.append(point)
    if (dl in optionx and first == "player") or (dl in optiono and first == "computer"):
        for point in dl_c:
            if field[point[0]][point[1]] == " ":
                rule_2.append(point)

    # Check if there is winning line
    if v1 == "xxx" or v2 == "xxx":
        return "x"
    if v3 == "xxx" or h1 == "xxx":
        return "x"
    if h2 == "xxx" or h3 == "xxx":
        return "x"
    if dr == "xxx" or dl == "xxx":
        return "x"

    if v1 == "ooo" or v2 == "ooo":
        return "o"
    if v3 == "ooo" or h1 == "ooo":
        return "o"
    if h2 == "ooo" or h3 == "ooo":
        return "o"
    if dr == "ooo" or dl == "ooo":
        return "o"

    if len(directions) == 0:
        return "END"
    if len(directions) > 0:
        return "CONTINUE"

print("\nXOX, by Dmytro Ievdokymov yedmitry@gmail.com who started to learn Phyton 2 months ago")
input("\nPress 'Enter' to begin...")

show()
counter = 0

result = random.choice(["player", "computer"])
# result = "player"

if result == "computer":
    comp = "x"
    user = "o"
    first = "computer"
    print("\nComputer comes first.")
elif result == "player":
    comp = "o"
    user = "x"
    first = "player"
    print("\nPlayer comes first.")

while True:
    counter += 1

    print(f"\nROUND# {counter} ______________________")
    directions = []
    rule_1 = []
    rule_2 = []
    check = check_result()

    if result == "computer":
        turn=enemy_turn()
        field[turn[0]][turn[1]] = comp
    elif result == "player":
        turn=player_turn()
        field[turn[0]][turn[1]] = user

    show()

    directions = []
    rule_1 = []
    rule_2 = []
    check = check_result()

    if check == "END":
        print("\nNo moves left. Game is over!")
        break

    elif check == "PLAYER":
        print("\nYou won. Game is over!")
        break

    elif check == "COMPUTER":
        print("\nYou lost. Game is over!")
        break

    if result == "computer":
        turn=player_turn()
        field[turn[0]][turn[1]] = user
    elif result == "player":
        turn=enemy_turn()
        field[turn[0]][turn[1]] = comp
    show()

    directions = []
    rule_1 = []
    rule_2 = []
    check = check_result()

    if check == "END":
        print("\nNo moves left. Game is over!")
        break

    if check == "o" and result == "computer":
        print("\nYou won. Game is over!")
        break

    elif check == "o" and result == "player":
        print("\nYou lost. Game is over!")
        break

    elif check == "x" and result == "player":
        print("\nYou won. Game is over!")
        break

    elif check == "x" and result == "computer":
        print("\nYou lost. Game is over!")
        break
