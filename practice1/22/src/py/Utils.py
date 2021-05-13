import Move
import IsCanMove


class Position:
    path = IsCanMove.IsCanMove.PATH

    def __init__(self, x, y):
        self.x = x
        self.y = y


maze = [
    "####B######################",
    "# #       #   #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   ###   #   #",
    "# ############# ### # # # #",
    "# ###       # # ### # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
]

moves_all = []


def create_move(position, move):
    global moves_all

    x = position.x
    y = position.y

    new_move = None

    if move == Move.Move.LEFT:
        new_move = Position(x - 1, y)
    elif move == Move.Move.RIGHT:
        new_move = Position(x + 1, y)
    elif move == Move.Move.DOWN:
        new_move = Position(x, y - 1)
    else:
        new_move = Position(x, y + 1)

    moves_all.append(new_move)
    return new_move


def check_position(labyrinth, x, y):
    global moves_all

    # x = столбец, y = строка
    if len(labyrinth) < y:
        return IsCanMove.IsCanMove.END

    if len(labyrinth[y]) < x:
        return IsCanMove.IsCanMove.END

    for move in moves_all:
        if move.x == x and move.y == y:
            return IsCanMove.IsCanMove.END

    if labyrinth[y][x] == '#':
        return IsCanMove.IsCanMove.END
    elif labyrinth[y][x] != ' ':
        return IsCanMove.IsCanMove.EXIT
    else:
        return IsCanMove.IsCanMove.PATH


def loop(labyrinth, exits, positions):
    moved = []
    for i in range(0, len(positions)):
        info = [check_position(labyrinth, positions[i].x - 1, positions[i].y),
                check_position(labyrinth, positions[i].x + 1, positions[i].y),
                check_position(labyrinth, positions[i].x, positions[i].y - 1),
                check_position(labyrinth, positions[i].x, positions[i].y + 1)]

        offset = 0
        for j in range(0, len(info)):
            if info[j] == IsCanMove.IsCanMove.PATH:
                moved.append(create_move(positions[i], Move.Move(j - offset)))
            elif info[j] == IsCanMove.IsCanMove.EXIT:
                exits.append(create_move(positions[i], Move.Move(j - offset)))
            if j % 3 == 0 and j > 0:
                offset += 3

    if len(moved) > 0:
        return loop(labyrinth, exits, moved)
    else:
        return


def calculate(labyrinth, x, y):
    result = []
    loop(labyrinth, result, [Position(x, y)])
    return result
