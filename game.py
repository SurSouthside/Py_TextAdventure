#!/usr/bin/env python3

from player import Player
from characterclass import CharacterClass
from character import Character


class Game:
    game_states = ['started', 'new', 'continued']

    def __init__(self, state):
        self._state = state

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
                print(the_player)
            case '2':
                print("You selected Mage")
                the_player.create_character(char_name, 'Mage')
            case '3':
                print("You selected Thief")
                the_player.create_character(char_name, 'Thief')

    def start_game(self):
        print("Welcome to Text Adventure")
        print("Select An Option:")
        print("1. New Game")
        print("2. Continue")
        start_screen_choice = input()
        if start_screen_choice == '1':
            print("New Game selected")
            the_player = self.process_new_game()
        elif start_screen_choice == '2':
            print("Continue selected")
        else:
            print("Option not recognized")

