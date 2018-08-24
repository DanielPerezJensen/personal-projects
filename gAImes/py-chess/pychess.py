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


class PyChess():

    def __init__(self):

        back_line = [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]
        self.board = [back_line,
                      [PAWN, PAWN, PAWN, PAWN, PAWN, PAWN, PAWN, PAWN],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [PAWN, PAWN, PAWN, PAWN, PAWN, PAWN, PAWN, PAWN],
                      back_line]

        self.colors = [["B", "B", "B", "B", "B", "B", "B", "B"],
                       ["B", "B", "B", "B", "B", "B", "B", "B"],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       ["W", "W", "W", "W", "W", "W", "W", "W"],
                       ["W", "W", "W", "W", "W", "W", "W", "W"]]

        self.current_player = "W"
        self.current_round = 1

    def calculate_board_value(self):

        self.white_value = 0
        self.black_value = 0

        for i, row in enumerate(self.board):
            for j, piece in enumerate(row):
                if piece is not None:
                    if self.colors[i][j] == "W":
                        self.white_value += piece
                    else:
                        self.black_value += piece

    def render(self):

        for row in self.board:
            for i in range(len(row)):
                print(point_piece_dict[row[i]], end=" ")
            print()

    def switch(self):

        if self.current_player == "W":
            self.current_player = "B"
        else:
            self.current_player = "W"


chess = PyChess()
chess.render()
