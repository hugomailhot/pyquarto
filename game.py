# !/usr/bin/env python
# encoding: utf-8

from board import Board
from player import HumanPlayer, ComputerPlayer


class Game():
    """This class is responsible for managing the flow of a game
    and hosting players and the board."""

    def __init__(self):
        self.board = Board()
        pass

    def _human_comp_str_is_valid(self, human_comp_str):
        """Determine whether human_comp_str is well-formed."""
        return human_comp_str in ('h', 'c')

    def choose_player(self, player_name):
        player_human_comp = input(
            f'Is player {player_name} a human or a computer? [h/c]: '
        ).lower().strip()

        if not self._human_comp_str_is_valid(player_human_comp):
            print("Please choose either 'h' for human or 'c' for computer")
            return self.choose_player(player_name)

        if player_human_comp == 'h':
            return HumanPlayer(player_name)
        else:
            return ComputerPlayer(player_name)

    def play(self):
        while not self.board.winning():
            self.picked_piece = self.current_player.play(self)
            self._switch_current_player()
        self.end_game()

    def _switch_current_player(self):
        if self.current_player == self.player_a:
            self.current_player = self.player_b
        else:
            self.current_player = self.player_a

    def start_game(self):
        print('\n-=-=-=- Time to play! -=-=-=-\n')
        self.player_a = self.choose_player('A')
        self.player_b = self.choose_player('B')
        self.current_player = self.player_a
        self.picked_piece = self.current_player.pick(self.board)
        self.play()

    def end_game(self):
        print(f'\n-=-=-=- Player {self.current_player.name} wins! -=-=-=-\n')

