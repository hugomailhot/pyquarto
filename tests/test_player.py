# !/usr/bin/env python
# encoding: utf-8

from pyquarto.board import Board
from pyquarto.coordinates import Coordinates
from pyquarto.game import Game
from pyquarto.player import ComputerPlayer


def initialize_game():
    """Game fixture to be used in tests."""
    game = Game()
    game.player_a = ComputerPlayer('A', max_depth=1)
    game.player_b = ComputerPlayer('B', max_depth=1)
    game.ai_player = game.player_a
    game.current_player = game.player_a

    return game

def test_finds_winning_move():
    """If given a winning piece, places it on winning square."""
    # build multiple board with one line of 3 related pieces
    # every time give a 4th related piece
    # assert that after playing,
    # board.winning() == True
    game = initialize_game()
    game.board.put(game.board.pieces[1], Coordinates('a', 1))
    game.board.put(game.board.pieces[2], Coordinates('a', 2))
    game.board.put(game.board.pieces[3], Coordinates('a', 3))

    game.picked_piece = game.board.pieces[4]

    game.current_player.play(game)

    print(game.board)

    assert game.board.winning() == True

    game = initialize_game()
    game.board.put(game.board.pieces[1], Coordinates('a', 1))
    game.board.put(game.board.pieces[2], Coordinates('b', 2))
    game.board.put(game.board.pieces[3], Coordinates('c', 3))

    game.picked_piece = game.board.pieces[4]

    game.current_player.play(game)

    print(game.board)

    assert game.board.winning() == True

    game = initialize_game()
    game.board.put(game.board.pieces[1], Coordinates('a', 1))
    game.board.put(game.board.pieces[2], Coordinates('b', 1))
    game.board.put(game.board.pieces[3], Coordinates('c', 1))

    game.picked_piece = game.board.pieces[4]

    game.current_player.play(game)

    print(game.board)

    assert game.board.winning() == True
