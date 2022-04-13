#!/usr/bin/env python3

import os

from player import Player


class Game:

    def __init__(self, state):
        self._state = state
        self._player = Player('')
        self._available_game_states = ['started', 'new', 'continued']
        self._game_state = ''
        self._available_game_statuses = ['exploration', 'battle', 'shopping']
        self._game_status = ''

    def process_new_game(self):
        the_player = Player('Default')
        char_name = input("Enter your character's name:")
        print("Character name: " + char_name)
        print("Select your character's class")
        print("1. Fighter")
        print("2. Mage")
        print("3. Thief")
        class_choice = input()
        match class_choice:
            case '1':
                print("You selected Fighter")
                the_player.create_character(char_name, 'Fighter')
            case '2':
                print("You selected Mage")
                the_player.create_character(char_name, 'Mage')
            case '3':
                print("You selected Thief")
                the_player.create_character(char_name, 'Thief')
        return the_player

    def enter_game_loop(self):
        self._game_status = 'exploration'
        print('Game loop entered')
        print('You are now in ' + self._game_status + ' mode. Type help for a list of available commands.')

    def start_new_game(self):
        os.system('cls')
        print('New Game started')
        self.enter_game_loop()

    def start_game(self):
        self._game_state = 'started'
        print("Welcome to Text Adventure")
        print("Select An Option:")
        print("1. New Game")
        print("2. Continue")
        start_screen_choice = input()
        if start_screen_choice == '1':
            self._game_state = 'new'
            print("New Game selected")
            player = self.process_new_game()
            print(player)
            self._player = player
            self.start_new_game()
        elif start_screen_choice == '2':
            print("Continue selected")
        else:
            print("Option not recognized")
