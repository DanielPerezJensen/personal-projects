PAWN = 1
KNIGHT = 3.2
BISHOP = 3.3
ROOK = 5.2
QUEEN = 9.6
KING = 3.5

point_piece_dict = {
    PAWN: "P",
    KNIGHT: "K",
    BISHOP: "B",
    ROOK: "R",
    QUEEN: "Q",
    KING: "+",
    None: "."
}


def init():

    init_board = [[ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK],
                  [PAWN, PAWN, PAWN, PAWN, PAWN, PAWN, PAWN, PAWN],
                  [None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None],
                  [PAWN, PAWN, PAWN, PAWN, PAWN, PAWN, PAWN, PAWN],
                  [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]]

    init_colors = [["B", "B", "B", "B", "B", "B", "B", "B"],
                   ["B", "B", "B", "B", "B", "B", "B", "B"],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   ["W", "W", "W", "W", "W", "W", "W", "W"],
                   ["W", "W", "W", "W", "W", "W", "W", "W"]]

    return init_board, init_colors


def calculate_board_value(board_state, board_colors, player="W"):

    black_value = 0
    white_value = 0

    for i, row in enumerate(board_state):
        for j, value in enumerate(row):
            if value is not None:
                if board_colors[i][j] == "W":
                    white_value += value
                elif board_colors[i][j] == "B":
                    black_value += value

    if player == "W":
        return white_value - black_value
    elif player == "B":
        return black_value - white_value


def render(board_state):

    for row in board_state:
        for i in range(len(row)):
            print(point_piece_dict[row[i]], end=" ")
        print()


def main():

    initial_board_state, initial_board_colors = init()
    render(initial_board_state)


if __name__ == "__main__":
    main()
