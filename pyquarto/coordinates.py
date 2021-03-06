# !/usr/bin/env python
# encoding: utf-8


class Coordinates():
    """Represents board coordinates.

    This class hides the zero-index matrix board coordinates to the
    user and instead offers an alphanumeric coordinates system
    much like the one used in chess: columns are letters starting
    at 'a', rows are integers starting at '1'. All conversions from
    one system to the other are handled in here, so that neither
    the user of the Board class need to worry about it.
    """

    def __init__(self, x, y, raw_values=False):
        """

        Arguments
        ---------
        x: str
            single letter in [a, b, c, d]
        y: int
            ranges from 1 to 4
        raw_values: bool
            If set to True, assign x and y directly without preprocessing.
        """
        self.char_int_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
        self.int_char_map = {y: x for x, y in self.char_int_map.items()}
        if raw_values:
            self.x, self.y = x, y
        else:
            self.x, self.y = self.from_alphanumeric(x, y)

    def __repr__(self):
        x, y = self.to_alphanumeric()
        return f'({x}, {y})'

    def from_alphanumeric(self, x, y):
        x = self.char_int_map[x]
        y -= 1
        return (x, y)

    def to_alphanumeric(self):
        x = self.int_char_map[self.x]
        y = self.y + 1
        return (x, y)

    def to_matrix_coordinates(self):
        return (self.x, self.y)
