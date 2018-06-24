# !/usr/bin/env python
# encoding: utf-8


from abc import ABC, abstractmethod
import time

from coordinates import Coordinates


class Player(ABC):

    @abstractmethod
    def choose_square(self, piece, board):
        """Choose where to place a piece.

        Arguments
        ---------
        piece: Piece
        board: Board

        Returns
        -------
        Coordinates
        """
        pass

    @abstractmethod
    def pick(self, board):
        """Pick a piece from the available ones on the board.

        Arguments
        ---------
        board: Board

        Returns
        -------
        Int, used as piece identifier in the board.
        """
        pass

    def place(self, piece, board):
        """Choose where to place a piece and put it on the board.

        Arguments
        ---------
        piece: Piece
        board: Board

        Returns
        -------
        Coordinates.
        """
        coord = self.choose_square(piece, board)
        board.put(piece, coord)


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
        if not all(col.isalpha(), row.isnumeric()):
            return False
        if not col in ('a', 'b', 'c', 'd'):
            return False
        if not 1 <= row <= 4:
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
        print(board.list_available_pieces())
        piece_id_str = input('Choose a piece (e.g. 4): ').strip()

        if not self._piece_id_str_is_valid(piece_id_str):
            print('Your choice in invalid! Please enter a single integer '
                  'between 1 and 16.\n')
            time.sleep(1)
            return self.pick(board)

        piece_id = int(piece_id_str)
        return board.pieces[piece_id]

