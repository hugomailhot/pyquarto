# !/usr/bin/env python
# encoding: utf-8


from abc import ABC, abstractmethod
fro copy import deepcopy
from itertools import product
import time

from coordinates import Coordinates


class Player(ABC):

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    @abstractmethod
    def play(self, game):
        """Choose where to place a piece and put it on the board.

        Arguments
        ---------
        game: Game

        Returns
        -------
        Piece picked for next player.
        """


class ComputerPlayer(Player):

    def __init__(self, name, max_depth):
        self.max_depth = depth
        super().__init__(name)

    def play(self, game):
        turns_scores = self.get_possible_turns_and_scores(game)

        # Choose square to play and piece to pick with best minimax score
        square, piece = max(turns_scores.items(), key=operator.itemgetter(1))
        game.board.put(game.picked_piece, square)

        return piece

    def choose_square(self, piece, board):
        print(board.get_available_squares())
        return board.get_available_squares()[0]

    def get_possible_turns_and_scores(self, game):
        turns_scores = {}
        possible_turns = list(
            product(game.get_available_squares, game.get_available_pieces)
        )

        for coord, piece in possible_turns(game):
            new_game = deepcopy(game)
            new_game.board.put(new_game.picked_piece, coord)
            new_game.picked_piece = piece

            turns[(coord, piece)] = self.minimax(
                new_game, self.max_depth, True
            )

        return turns_scores

    def pick(self, board):
        available_pieces = board.get_available_pieces()
        first_piece = list(available_pieces.values())[0]
        return first_piece

    def minimax(self, game, depth, maximizing):
        """Compute best move, assuming opponent plays optimally.

        Arguments
        ---------
        game: pyquarto.Game
            Current game state
        depth: int
            Depth levels left to recursively go down

        Returns
        -------
        int:
            Score of current game state
        """
        if game.board.winning() or depth == 0:
            return self.score(game)

        if maximizing:
            best_score = -100


    def score(self, game):
        """Compute game state quality evaluation score.

        If the game is not in an end state, return the number of lines
        with 3 pieces on them.

        Arguments
        ---------
        game: pyquarto.Game
            Current game state.

        Returns
        -------
        int
        """
        if game.board.winning():
            if game.current_player == game.ai_player:
                return 100
            else:
                return -100
        else:
            return 0


class HumanPlayer(Player):

    def _coord_str_is_valid(self, coord_str):
        """Determine if coord_str is well-formed.

        To be well-formed is to have one letter and one integer, respectively
        in the ranges a-d and 1-4.

        Arguments
        ---------
        coord_str: str

        Returns
        -------
        Bool
        """
        coord_str = coord_str
        if len(coord_str) != 2:
            return False
        col, row = coord_str[0], coord_str[1]
        if not all((col.isalpha(), row.isnumeric())):
            return False
        if not col in ('a', 'b', 'c', 'd'):
            return False
        if not 1 <= int(row) <= 4:
            return False
        return True

    def _piece_id_str_is_valid(self, piece_id_str):
        """Determine if piece_id_str is well-formed.

        To be well-formed is to have a single numeric character in the
        range 1-16.
        """
        if not piece_id_str.isnumeric():
            return False
        piece_id = int(piece_id_str)
        if not 1 <= piece_id <= 16:
            return False
        return True

    def play(self, game):
        coords = self.choose_square(piece, board)
        game.board.put(game.picked_piece, coords)

        return self.pick(game.board)

    def choose_square(self, piece, board):
        print(board)
        print(f'Choose where to place your piece. Your piece is: {piece}')

        coord_str = (
            input('Your choice (e.g. b3): ').lower().strip().replace(' ', '')
        )

        if not self._coord_str_is_valid(coord_str):
            print('Your choice was malformed! Please enter a single letter '
                  'between a and d and a single integer between 1 and 4. '
                  "For example, 'a4' or 'c2'\n")
            time.sleep(1)
            return self.choose_square(piece, board)

        x, y = coord_str[0], int(coord_str[1])

        return Coordinates(x, y)

    def pick(self, board):
        print('-- Available pieces --')
        avail_pieces = board.get_available_pieces()
        for piece_id, piece in avail_pieces.items():
            print(f'{piece_id}:{piece}')
        piece_id_str = input('Choose a piece (e.g. 4): ').strip()

        if not self._piece_id_str_is_valid(piece_id_str):
            print('Your choice in invalid! Please enter a single integer '
                  'between 1 and 16.\n')
            time.sleep(1)
            return self.pick(board)

        piece_id = int(piece_id_str)
        return board.pieces[piece_id]

