# !/usr/bin/env python
# encoding: utf-8


class Piece():

    def __init__(self, size, color, shape, top):
        self.size = size
        self.color = color
        self.shape = shape
        self.top = top
        self.available = True

    def __eq__(self, other):
        if not isinstance(other, Piece):
            return False
        return all([self.size == other.size,
                    self.color == other.color,
                    self.shape == other.shape,
                    self.top == other.top])

    def __hash__(self):
        return hash(repr(self))

    def __repr__(self):
        return f'{self.size} {self.color} {self.shape} {self.top}'

    def __str__(self):
        size = 's' if self.size == 'short' else 'T'
        color = 'w' if self.color == 'white' else 'B'
        shape = 'r' if self.shape == 'round' else 'S'
        top = 'f' if self.top == 'flat' else 'H'
        return f'{size}{color}{shape}{top}'

