# Author: Eric Tolson
# Description: This code contains a class, HasamiShogiGame,
# that contains the necessary data members and methods to play the game Hasami Shogi.

class HasamiShogiGame:
    """Represents a game of Hasami Shogi"""
    def __init__(self):
        """Constructor for HasamiShogiGame class. Takes no parameters.
        Initializes all required data members as private"""
        self._board = [[["a1", "r"], ["a2", "r"], ["a3", "r"], ["a4", "r"], ["a5", "r"], ["a6", "r"], ["a7", "r"], ["a8", "r"], ["a9", "r"]],
                       [["b1", ""], ["b2", ""], ["b3", ""], ["b4", ""], ["b5", ""], ["b6", ""], ["b7", ""], ["b8", ""], ["b9", ""]],
                       [["c1", ""], ["c2", ""], ["c3", ""], ["c4", ""], ["c5", ""], ["c6", ""], ["c7", ""], ["c8", ""], ["c9", ""]],
                       [["d1", ""], ["d2", ""], ["d3", ""], ["d4", ""], ["d5", ""], ["d6", ""], ["d7", ""], ["d8", ""], ["d9", ""]],
                       [["e1", ""], ["e2", ""], ["e3", ""], ["e4", ""], ["e5", ""], ["e6", ""], ["e7", ""], ["e8", ""], ["e9", ""]],
                       [["f1", ""], ["f2", ""], ["f3", ""], ["f4", ""], ["f5", ""], ["f6", ""], ["f7", ""], ["f8", ""], ["f9", ""]],
                       [["g1", ""], ["g2", ""], ["g3", ""], ["g4", ""], ["g5", ""], ["g6", ""], ["g7", ""], ["g8", ""], ["g9", ""]],
                       [["h1", ""], ["h2", ""], ["h3", ""], ["h4", ""], ["h5", ""], ["h6", ""], ["h7", ""], ["h8", ""], ["h9", ""]],
                       [["i1", "b"], ["i2", "b"], ["i3", "b"], ["i4", "b"], ["i5", "b"], ["i6", "b"], ["i7", "b"], ["i8", "b"], ["i9", "b"]]]
        self._active_player = "BLACK"
        self._inactive_player = "RED"
        self._game_state = "UNFINISHED"
        self._captured_red_pawns = 0
        self._captured_black_pawns = 0

    def get_board(self):
        """Returns board"""
        return self._board

    def set_board(self, updated_board):
        """Updates board"""
        self._board = updated_board

    def get_active_player(self):
        """Returns active player"""
        return self._active_player

    def get_inactive_player(self):
        """Returns inactive player"""
        return self._inactive_player

    def set_inactive_player(self, updated_player):
        """Update active player"""
        self._inactive_player = updated_player

    def set_active_player(self, updated_player):
        """Update active player"""
        self._active_player = updated_player

    def get_game_state(self):
        """Returns game state"""
        return self._game_state

    def set_game_state(self, updated_game_state):
        """Update game state"""
        self._game_state = updated_game_state

    def get_captured_red_pawns(self):
        """Returns captured red pawns"""
        return self._captured_red_pawns

    def set_captured_red_pawns(self):
        """Updates captured red pawns"""
        self._captured_red_pawns += 1

    def get_captured_black_pawns(self):
        """Returns captured black pawns"""
        return self._captured_black_pawns

    def set_captured_black_pawns(self):
        """Updates captured red pawns"""
        self._captured_black_pawns += 1

    def get_num_captured_pieces(self, color):
        if color == "BLACK":
            return self.get_captured_black_pawns()
        elif color == "RED":
            return self.get_captured_red_pawns()

    def update_players(self):
        """Changes active player for next turn"""
        if self.get_active_player() == "BLACK":
            self.set_active_player("RED")
            self.set_inactive_player("BLACK")
        elif self.get_active_player() == "RED":
            self.set_active_player("BLACK")
            self.set_inactive_player("RED")

    def print_board(self):
        """Prints board"""
        board = self.get_board()
        for row in board:
            for cell in row:
                print(cell, end='\t')
            print()

    def get_square_occupant(self, pos):
        """Takes alphanumeric board position and returns
        the occupant, 'RED', 'BLACK', 'NONE', or 'NOT ON BOARD'"""
        board = self.get_board()
        color = None
        for row in board:
            for cell in row:
                if cell[0] == pos:
                    color = cell[1]
        if color == "r":
            return "RED"
        elif color == "b":
            return "BLACK"
        elif color == "":
            return "NONE"
        elif color is None:
            return "NOT ON BOARD"

    def legal_move_positions(self, start_pos, end_pos):
        """Takes start and end position for a move and
        determines if they are valid"""
        if self.get_square_occupant(start_pos) == self.get_active_player():
            if self.get_square_occupant(end_pos) == "NONE":
                return True
            else:
                return False

    def legal_move_path(self, start_pos, end_pos):
        """Takes a start and end position for a move and
        determines if the path of movement is valid"""
        if start_pos[0] == end_pos[0]:
            if start_pos[1] != end_pos[1]:  # if move is horizontal
                return True
            else:
                return False
        elif start_pos[0] != end_pos[0]:
            if start_pos[1] == end_pos[1]:  # if move is vertical
                return True
            else:  # if move is neither
                return False

    def legal_move_clear(self, start_pos, end_pos):
        """Takes a start and end position for a move and
        determines if the path of movement is clear"""
        if start_pos[0] == end_pos[0]:  # if the move is horizontal
            if int(start_pos[1]) < int(end_pos[1]):   # if move is to the right
                count = int(start_pos[1]) + 1
                while count < int(end_pos[1]):
                    occupant = self.get_square_occupant(start_pos[0] + str(count))
                    if occupant != "NONE":
                        return False
                    count += 1
                return True
            elif int(start_pos[1]) > int(end_pos[1]):  # if move is to the left
                count = int(start_pos[1]) - 1
                while count > int(end_pos[1]):
                    occupant = self.get_square_occupant(start_pos[0] + str(count))
                    if occupant != "NONE":
                        return False
                    count -= 1
                return True
        elif start_pos[1] == end_pos[1]:  # if the move is vertical
            if ord(start_pos[0]) < ord(end_pos[0]):   # if the move is down the board
                count = ord(start_pos[0]) + 1
                while count < ord(end_pos[0]):
                    occupant = self.get_square_occupant(chr(count) + start_pos[1])
                    if occupant != "NONE":
                        return False
                    count += 1
                return True
            if ord(start_pos[0]) > ord(end_pos[0]):   # if the move is up the board
                count = ord(start_pos[0]) - 1
                while count > ord(end_pos[0]):
                    occupant = self.get_square_occupant(chr(count) + start_pos[1])
                    if occupant != "NONE":
                        return False
                    count -= 1
                return True

    def legal_move(self, start_pos, end_pos):
        """Takes two parameters, a starting and ending position.
        Returns True if the move is legal or False if not."""
        if self.legal_move_positions(start_pos, end_pos) is not True:
            return False
        elif self.legal_move_path(start_pos, end_pos) is not True:
            return False
        elif self.legal_move_clear(start_pos, end_pos) is not True:
            return False
        else:
            return True

    def move_piece(self, start_pos, end_pos):
        """Takes two parameters, start and end position. Updates start square
        and end square to reflect piece moving for legal move."""
        board = self.get_board()
        color = None
        for row in board:  # removes color from starting square
            for cell in row:
                if cell[0] == start_pos:
                    color = cell[1]
                    cell[1] = ""
        for row in board:  # adds color to ending square
            for cell in row:
                if cell[0] == end_pos:
                    cell[1] = color
        self.set_board(board)  # update board with change

    def capture_piece(self, pos):
        """Removes color from board square and updates captured piece data."""
        board = self.get_board()
        color = None
        for row in board:
            for cell in row:
                if cell[0] == pos:
                    color = cell[1]
                    cell[1] = ""
        self.set_board(board)
        if color == "r":
            self.set_captured_red_pawns()
        elif color == "b":
            self.set_captured_black_pawns()

    def horizontal_captures(self, end_pos):
        """Takes one parameter, the end position of a moved piece.
        Checks if there are horizontal captures and captures pieces
        if so."""
        increase = int(end_pos[1]) + 1  # checks captures to the right
        right_capture = []
        while self.get_square_occupant(end_pos[0] + str(increase)) == self.get_inactive_player():
            right_capture.append(end_pos[0] + str(increase))
            increase += 1
            if self.get_square_occupant(end_pos[0] + str(increase)) == self.get_active_player():
                for pos in right_capture:
                    self.capture_piece(pos)
        decrease = int(end_pos[1]) - 1  # checks captures to the left
        left_capture = []
        while self.get_square_occupant(end_pos[0] + str(decrease)) == self.get_inactive_player():
            left_capture.append(end_pos[0] + str(decrease))
            decrease -= 1
            if self.get_square_occupant(end_pos[0] + str(decrease)) == self.get_active_player():
                for pos in left_capture:
                    self.capture_piece(pos)

    def vertical_captures(self, end_pos):
        """Takes one parameter, the end position of a moved piece.
        Checks if there are vertical captures and captures pieces
        if so."""
        increase = ord(end_pos[0]) + 1  # checks captures down the board
        down_capture = []
        while self.get_square_occupant(chr(increase) + end_pos[1]) == self.get_inactive_player():
            down_capture.append(chr(increase) + end_pos[1])
            increase += 1
            if self.get_square_occupant(chr(increase) + end_pos[1]) == self.get_active_player():
                for pos in down_capture:
                    self.capture_piece(pos)
        decrease = ord(end_pos[0]) - 1  # checks captures up the board
        up_capture = []
        while self.get_square_occupant(chr(decrease) + end_pos[1]) == self.get_inactive_player():
            up_capture.append(chr(decrease) + end_pos[1])
            decrease -= 1
            if self.get_square_occupant(chr(decrease) + end_pos[1]) == self.get_active_player():
                for pos in up_capture:
                    self.capture_piece(pos)

    def corner_captures(self, end_pos):
        """Takes one parameter, the end position of a moved piece.
        Checks if there are corner captures and captures pieces
        if so."""
        if end_pos == "b1":
            if self.get_square_occupant("a2") == self.get_active_player():
                if self.get_square_occupant("a1") == self.get_inactive_player():
                    self.capture_piece("a1")
        elif end_pos == "a2":
            if self.get_square_occupant("b1") == self.get_active_player():
                if self.get_square_occupant("a1") == self.get_inactive_player():
                    self.capture_piece("a1")
        elif end_pos == "b9":
            if self.get_square_occupant("a8") == self.get_active_player():
                if self.get_square_occupant("a9") == self.get_inactive_player():
                    self.capture_piece("a9")
        elif end_pos == "a8":
            if self.get_square_occupant("b9") == self.get_active_player():
                if self.get_square_occupant("a9") == self.get_inactive_player():
                    self.capture_piece("a9")
        elif end_pos == "h1":
            if self.get_square_occupant("i2") == self.get_active_player():
                if self.get_square_occupant("i1") == self.get_inactive_player():
                    self.capture_piece("i1")
        elif end_pos == "i2":
            if self.get_square_occupant("h1") == self.get_active_player():
                if self.get_square_occupant("i1") == self.get_inactive_player():
                    self.capture_piece("i1")
        elif end_pos == "h9":
            if self.get_square_occupant("i8") == self.get_active_player():
                if self.get_square_occupant("i9") == self.get_inactive_player():
                    self.capture_piece("i9")
        elif end_pos == "i8":
            if self.get_square_occupant("h9") == self.get_active_player():
                if self.get_square_occupant("i9") == self.get_inactive_player():
                    self.capture_piece("i9")

    def total_captures(self, end_pos):
        """Takes one parameter, the end position of a moved piece.
        Makes all possible captures for that move."""
        self.horizontal_captures(end_pos)
        self.vertical_captures(end_pos)
        self.corner_captures(end_pos)

    def is_game_over(self):
        """Takes no parameters. Checks total captured pieces
        for each color and updates game state if one is 8."""
        if self.get_captured_red_pawns() >= 8:
            self.set_game_state("BLACK WINS")
            print(self.get_game_state())
        elif self.get_captured_black_pawns() >= 8:
            self.set_game_state("RED WINS")
            print(self.get_game_state())

    def make_move(self, start_pos, end_pos):
        """Takes two parameters, a starting and ending position.
        Determines if the move is legal, and if so makes the move, captures pieces
        if possible, and updates the relevant data members.
        Returns False if illegal move or game is won and True otherwise"""
        if self.get_game_state() != "UNFINISHED":  # if the game is finished
            print("GAME OVER")
            return False
        elif self.legal_move(start_pos, end_pos) is not True:  # if the move is not legal
            print("ILLEGAL MOVE")
            return False
        else:
            self.move_piece(start_pos, end_pos)  # move piece if game is unfinished and move is legal
            self.total_captures(end_pos)  # capture pieces if possible
            self.update_players()
            self.print_board()
            print(str(self.get_captured_red_pawns()) + " CAPTURED RED PAWNS")
            print(str(self.get_captured_black_pawns()) + " CAPTURED BLACK PAWNS")
            print(self.get_active_player() + "'S TURN")
            self.is_game_over()
            return True