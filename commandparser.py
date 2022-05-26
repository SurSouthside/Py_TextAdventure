#!/usr/bin/env python3

class CommandParser:

    def __init__(self):
        #self._game_status = ''
        self._valid_exploration_commands = ['help', 'status']
        self._valid_battle_commands = ['help', 'status']
        self._valid_shop_commands = ['help', 'status']

    def get_game_status(self):
        return self.game_status

    def parse_exploration_commands(self):
        return ''

    def parse_battle_commands(self):
        return ''

    def parse_shop_commands(self):
        return ''

    def parse_command(self, command, game_status):
        print("You entered: " + command)
