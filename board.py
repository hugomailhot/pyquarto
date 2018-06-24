# !/usr/bin/env python
# encoding: utf-8

from terminaltables import SingleTable

from exceptions import PieceNotAvailable, SquareNotAvailable
from piece import Piece


class Board():

    def __init__(self):
        self.squares = [[None] * 4 for _ in range(4)]
        self.pieces = self._generate_pieces()
        self.piece_id = {piece: idx for idx, piece in self.pieces.items()}

    def __str__(self):
        data = [[str(piece) for piece in row] for row in self.squares]
        table = SingleTable(data)
        table.inner_heading_row_border = False
        table.inner_row_border = True
        return table.table

    def _generate_pieces(self):
        pieces = {}
        i = 1
        for size in ('short', 'tall'):
            for color in ('black', 'white'):
                for shape in ('round', 'square'):
                    for top in ('flat', 'hollow'):
                        pieces[i] = Piece(size, color, shape, top)
                        i += 1
        return pieces

    def _lines(self):
        lines = []
        # horizontal lines
        for y in range(4):
            lines.append([self.squares[x][y] for x in range(4)])

        # vertical lines
        for x in range(4):
            lines.append([self.squares[x][y] for y in range(4)])

        # diagonals
        lines.append([self.squares[x][x] for x in range(4)])
        lines.append([self.squares[x][x-3] for x in range(4)])

        return lines

    def count_quasicomplete_lines(self):
        """Returns number of lines with only one available square.

        This is useful for an AI trying to maximize chances of mistakes by
        a human player.
        """
        count = 0
        for line in self._lines():
            if line.count(None) == 1:
                count += 1
        return count

    def get_available_pieces(self):
        """Returns dict of idx: piece pairs."""
        return {idx: piece for idx, piece in self.piece.items()
                if piece.available}

    def get_available_squares(self):
        """Returns list of Coordinates instances."""
        available_coordinates = []
        for x in range(4):
            for y in range(4):
                if self.square is None:
                    coord = Coordinates(x, y, raw_values=True)
                    available_coordinates.append(coord)
        return available_coordinates

    def put(self, piece, coord):
        """Place piece at given coordinates.

        Arguments
        ---------
        piece: Piece
        coord: Coordinates
            Where on the board to put the piece
        """
        piece_id = self.piece_id[piece]

        if not self.pieces[piece_id].available:
            raise PieceNotAvailable()
        if self.squares[coord.x][coord.y] is not None:
            raise SquareNotAvailable()

        self.squares[coord.x][coord.y] = self.pieces[piece_id]
        self.pieces[piece_id].available = False

    def winning(self):
        for l in self._lines():
            if not any(x is None for x in l):  # No empty square
                if any([l[0].size == l[1].size == l[2].size == l[3].size,
                        l[0].color == l[1].color == l[2].color == l[3].color,
                        l[0].shape == l[1].shape == l[2].shape == l[3].shape,
                        l[0].top == l[1].top == l[2].top == l[3].top]):
                    return True
        return False

