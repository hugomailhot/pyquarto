# !/usr/bin/env python
# encoding: utf-8


from abc import ABC
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

