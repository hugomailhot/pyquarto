# !/usr/bin/env python
# encoding: utf-8

from pyquarto.board import Board
from pyquarto.coordinates import Coordinates
from pyquarto.piece import Piece


all_pieces = [
    Piece(size='short', color='white', shape='round', top='flat'),
    Piece(size='short', color='white', shape='round', top='hollow'),
    Piece(size='short', color='white', shape='square', top='flat'),
    Piece(size='short', color='white', shape='square', top='hollow'),
    Piece(size='short', color='black', shape='round', top='flat'),
    Piece(size='short', color='black', shape='round', top='hollow'),
    Piece(size='short', color='black', shape='square', top='flat'),
    Piece(size='short', color='black', shape='square', top='hollow'),
    Piece(size='tall', color='white', shape='round', top='flat'),
    Piece(size='tall', color='white', shape='round', top='hollow'),
    Piece(size='tall', color='white', shape='square', top='flat'),
    Piece(size='tall', color='white', shape='square', top='hollow'),
    Piece(size='tall', color='black', shape='round', top='flat'),
    Piece(size='tall', color='black', shape='round', top='hollow'),
    Piece(size='tall', color='black', shape='square', top='flat'),
    Piece(size='tall', color='black', shape='square', top='hollow'),
]


def test_count_quasicomplete_lines():
    b = Board()

    assert b.count_quasicomplete_lines() == 0

    b.put(all_pieces[0], Coordinates('a', 1))
    b.put(all_pieces[1], Coordinates('a', 2))
    b.put(all_pieces[2], Coordinates('a', 3))

    assert b.count_quasicomplete_lines() == 1

    b.put(all_pieces[3], Coordinates('b', 1))
    b.put(all_pieces[4], Coordinates('c', 1))

    assert b.count_quasicomplete_lines() == 2

    b.put(all_pieces[6], Coordinates('b', 2))
    b.put(all_pieces[7], Coordinates('b', 3))
    b.put(all_pieces[8], Coordinates('c', 2))
    b.put(all_pieces[9], Coordinates('c', 3))

    assert b.count_quasicomplete_lines() == 7


def test_display():
    # TODO: fix the inequality problem in these assert statements
    # Empty board
    empty_board_str = """
┌──────┬──────┬──────┬──────┐
│ None │ None │ None │ None │
├──────┼──────┼──────┼──────┤
│ None │ None │ None │ None │
├──────┼──────┼──────┼──────┤
│ None │ None │ None │ None │
├──────┼──────┼──────┼──────┤
│ None │ None │ None │ None │
└──────┴──────┴──────┴──────┘
""".strip()

    # assert str(Board()) == empty_board_str

    # With some pieces
    b = Board()
    b.put(b.pieces[1], Coordinates('a', 1))
    b.put(b.pieces[2], Coordinates('b', 4))

    nonempty_board_str = """
┌──────┬──────┬──────┬──────┐
│ sBrf │ None │ None │ None │
├──────┼──────┼──────┼──────┤
│ None │ None │ None │ sBrH │
├──────┼──────┼──────┼──────┤
│ None │ None │ None │ None │
├──────┼──────┼──────┼──────┤
│ None │ None │ None │ None │
└──────┴──────┴──────┴──────┘
""".strip()

    # assert str(b) == nonempty_board_str


def test_lines():
    expected_lines = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
    ]
    # TODO: finish this!

def test_put_updates_available_pieces():
    coord1 = Coordinates('a', 1)
    piece1 = Piece(size='short', color='white', shape='round', top='hollow')
    coord2 = Coordinates('b', 4)
    piece2 = Piece(size='tall', color='black', shape='square', top='flat')

    b = Board()
    b.put(piece1, coord1)
    b.put(piece2, coord2)

    expected_availables_pieces = set(all_pieces) - set([piece1, piece2])

    assert set(b.get_available_pieces().values()) == expected_availables_pieces


def test_put_updates_squares():
    coord1 = Coordinates('a', 1)
    piece1 = Piece(size='short', color='white', shape='round', top='hollow')
    coord2 = Coordinates('b', 4)
    piece2 = Piece(size='tall', color='black', shape='square', top='flat')

    b = Board()
    b.put(piece1, coord1)
    b.put(piece2, coord2)

    expected_squares = [
        [piece1, None, None, None],
        [None  , None, None, piece2],
        [None  , None, None, None],
        [None  , None, None, None]
    ]

    assert b.squares == expected_squares



