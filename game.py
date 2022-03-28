#!/usr/bin/env python3

from player import Player
from characterclass import CharacterClass


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
                class_choice = CharacterClass('Fighter')
                print("You selected Fighter")
            case '2':
                class_choice = CharacterClass('Mage')
                print("You selected Mage")
            case '31':
                class_choice = CharacterClass('Thief')
                print("You selected Thief")

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

