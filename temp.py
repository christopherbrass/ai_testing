# transition function

# TODO: errors/error handling
# TODO: comment functionc and classes
# TODO: deep copy for board
# TODO: map out game loop in start_game()?

# TODO: Restructure for single game??? cleaner


class game_state:
    """
    board, curr player, score, which game
    """

    def __init__(self, board):
        self.board = board

    def __str__(self):
        return f""


class agent:
    """
    which game, side, piece?, .nextMove(board), ai method
    """

    def __init__(self, board, piece):
        self.board = board

    def __str__(self):
        return f""


class game_master:
    """
    facilitates turns, keeps score, validates moves, which game
    """

    def __init__(self, game_to_play: str = "tic_tac_toe") -> None:
        self.game_to_play = game_to_play
        self.game_over_codes = {
            0: "Game Not Over",
            1: "Player 1 Wins",
            2: "Player 2 Wins",
            3: "Tie",
        }
        if self.game_to_play == "tic_tac_toe":
            self.board = [[" "] * 3] * 3
            self.player_1 = agent(game_to_play="tic_tac_toe", piece="x")
            self.player_2 = agent(game_to_play="tic_tac_toe", piece="o")
            self.winning_lines = [
                [(0, 0), (1, 0), (2, 0)],
                [(0, 1), (1, 1), (2, 1)],
                [(0, 2), (1, 2), (2, 2)],
                [(0, 0), (0, 1), (0, 2)],
                [(1, 0), (1, 1), (1, 2)],
                [(2, 0), (2, 1), (2, 2)],
                [(0, 0), (1, 1), (2, 2)],
                [(2, 0), (1, 1), (0, 2)],
            ]
        elif self.game_to_play == "connect_four":
            self.board = [[" "] * 7] * 6
            pass
        else:
            # error?
            pass

    def __str__(self):
        return f""

    def start_game(self):
        # check exist players
        # alternate turns while validating moves and checking for game over
        # game loop?
        if self.game_to_play == "tic_tac_toe":
            # error if players dont exist
            while self.is_game_over() == 0:
                # request player 1 move
                # validate move
                # check game over -> continue?
                # request player 2 move
                # validate move
                pass
            pass
        elif self.game_to_play == "connect_four":
            pass

    def is_game_over(self) -> int:
        if self.game_to_play == "tic_tac_toe":
            # Are there any empty spaces? -> 0
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        return 0

            # 3 in-a-row player_1? -> 1
            for line in self.winning_lines:
                if (
                    self.board[line[0][0]][line[0][1]] == self.player_1.piece
                    and self.board[line[1][0]][line[1][1]] == self.player_1.piece
                    and self.board[line[2][0]][line[2][1]] == self.player_1.piece
                ):
                    return 1

            # 3 in-a-row player_2? -> 2
            for line in self.winning_lines:
                if (
                    self.board[line[0][0]][line[0][1]] == self.player_2.piece
                    and self.board[line[1][0]][line[1][1]] == self.player_2.piece
                    and self.board[line[2][0]][line[2][1]] == self.player_2.piece
                ):
                    return 2

            # else -> 3
            return 3

        elif self.game_to_play == "connect_four":
            pass


# rules per game and for system
# System:
# Player 1 goes first

# Tic-Tac-Toe Rules:
# x goes first
#
# 2
# 1
# 0
#  0 1 2


# sample play
gm = game_master(game_to_play="tic_tac_toe")
gm.start_game()
