#!/usr/bin/env python3

import json
import os


class CommandParser:

    def __init__(self):
        self._game_status = ''
        # self._valid_exploration_commands = ['help', 'status']
        # self._valid_battle_commands = ['help', 'status']
        # self._valid_shop_commands = ['help', 'status']
        # print(__file__)
        # print(os.path.dirname(__file__))
        # print(os.path.join(os.path.dirname(__file__), 'assets', 'command_list.json'))
        # self._commands = open(r'D:\Python_Apps\Python_TextAdventure\py_textadventure\assets\command_list.json')
        self._commands = open((os.path.join(os.path.dirname(__file__), 'assets', 'command_list.json')))
        self._command_list = json.load(self._commands)

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
        for i in self._command_list['exploration_commands']:
            print(i)
